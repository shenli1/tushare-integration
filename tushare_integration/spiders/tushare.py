import datetime
import json
import logging

import pandas as pd
import requests
import scrapy
import yaml

from tushare_integration.constants import DEFAULT_START_DATE
from tushare_integration.db_engine import DatabaseEngineFactory, DBEngine
from tushare_integration.items import TushareIntegrationItem
from tushare_integration.settings import TushareIntegrationSettings


class TushareSpider(scrapy.Spider):
    name: str
    api_name: str
    schema: dict = {}
    spider_settings: TushareIntegrationSettings  # 不能直接叫settings，会覆盖掉scrapy的settings
    db_engine: DBEngine

    custom_settings: dict = {}

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.schema = self.get_schema()

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super().from_crawler(crawler, *args, **kwargs)
        spider.spider_settings = TushareIntegrationSettings.model_validate(
            yaml.safe_load(open('config_prod.yaml', 'r', encoding='utf8').read())
        )
        spider.create_table()
        return spider

    def create_table(self):
        logging.info(f"quest {self.name}: create table {self.get_table_name()}")

        self.db_engine = DatabaseEngineFactory.create(self.spider_settings)
        self.db_engine.create_table(self.get_table_name(), self.schema)

    def get_schema(self):
        with open(f"tushare_integration/schema/{self.get_schema_name()}.yaml", "r", encoding="utf-8") as f:
            return yaml.safe_load(f.read())

    def start_requests(self):
        yield self.get_scrapy_request()

    def parse(self, response, **kwargs):
        try:
            item = self.parse_response(response, **kwargs)

            if item['data'] is None or len(item['data']) == 0:
                logging.warning(f"Spider {self.name} 获取的数据为空")
                return

            logging.info(f"Spider {self.name} 获取到 {len(item['data'])} 条数据")
            return item
        except Exception as e:
            logging.error(f"Spider {self.name} 解析响应时出错: {e}")
            raise

    def parse_response(self, response, **kwargs):
        try:
            resp = json.loads(response.text)

            if resp["code"] != 0:
                logging.error(f"Spider {self.name} 请求 {self.get_api_name()} 失败: {resp['msg']}")
                raise RuntimeError(resp['msg'])

            data_items = resp["data"]["items"]
            data_fields = resp["data"]["fields"]
            data_count = len(data_items)
            
            logging.info(f"Spider {self.name} API返回 {data_count} 条数据，字段: {data_fields}")
            
            return TushareIntegrationItem(data=pd.DataFrame(data=data_items, columns=data_fields))
        except Exception as e:
            logging.error(f"Spider {self.name} 解析API响应时出错: {e}")
            raise

    def get_db_engine(self):
        return self.db_engine

    def get_scrapy_request(self, params: dict | None = None, meta: dict | None = None):
        if not params:
            params = {}

        if not meta:
            meta = {}

        logging.info(f"Requesting {self.get_api_name()} with params: {params}")

        return scrapy.Request(
            url=self.spider_settings.tushare_url,
            method="POST",
            body=json.dumps(
                {
                    "api_name": self.get_api_name(),
                    "token": self.spider_settings.tushare_token,
                    "params": params,
                    "fields": self.load_fields(),
                }
            ),
            headers={
                "Content-Type": "application/json",
            },
            meta={
                'api_name': self.get_api_name(),
                'params': params,
            }
            | meta,
        )

    # 搞个函数，直接使用requests发起请求
    def request_with_requests(self, params: dict | None = None, meta: dict | None = None) -> TushareIntegrationItem:
        logging.info(f"Requesting {self.get_api_name()} with params: {params}")
        response = requests.post(
            url=self.spider_settings.tushare_url,
            json={
                "api_name": self.get_api_name(),
                "token": self.spider_settings.tushare_token,
                "params": params,
                "fields": self.load_fields(),
            },
            headers={
                "Content-Type": "application/json",
            },
        )

        return self.parse_response(response)

    def load_fields(self):
        return ",".join([column["name"] for column in self.schema["columns"]])

    def get_schema_name(self):
        return self.name

    def get_api_name(self):
        if hasattr(self, 'api_name') and self.api_name:
            return self.api_name
        return self.name.split("/")[-1]

    def get_table_name(self) -> str:
        if self.custom_settings and self.custom_settings.get("TABLE_NAME"):
            return self.custom_settings.get("TABLE_NAME", '')
        return self.name.split("/")[-1]


class DailySpider(TushareSpider):
    name: str
    custom_settings = {"TABLE_NAME": "daily", "TRADE_DATE_FIELD": "trade_date"}

    # 固定的空数据日期记录表名，所有接口共用
    EMPTY_DATES_TABLE = "empty_data_dates"

    def open_spider(self):
        """在spider打开时创建空数据日期记录表"""
        try:
            conn = self.get_db_engine()
            db_name = self.spider_settings.database.db_name
            
            conn.query_df(f"""
                CREATE TABLE IF NOT EXISTS {db_name}.{self.EMPTY_DATES_TABLE} (
                    trade_date DATE PRIMARY KEY,
                    spider_name VARCHAR(255),
                    create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            logging.info(f"Spider {self.name} 空数据日期记录表已准备就绪")
        except Exception as e:
            logging.warning(f"Spider {self.name} 创建空数据日期记录表时出错: {e}")

    def start_requests(self):
        try:
            min_cal_date = self.custom_settings.get("MIN_CAL_DATE", DEFAULT_START_DATE)
            conn = self.get_db_engine()
            db_name = self.spider_settings.database.db_name

            # 查询需要获取数据的交易日，排除已有数据和已知空数据的日期
            empty_dates_table = "empty_data_dates"
            cal_dates = conn.query_df(
                f"""
                    SELECT DISTINCT cal_date
                    FROM {db_name}.trade_cal
                    WHERE cal_date NOT IN (SELECT `{self.custom_settings.get('TRADE_DATE_FIELD', 'trade_date')}` FROM {db_name}.{self.get_table_name()})
                      AND is_open = 1
                      AND cal_date >= '{min_cal_date}'
                      AND cal_date <= today()
                      AND exchange = 'SSE'
                      AND cal_date NOT IN (
                          SELECT trade_date 
                              FROM {db_name}.{empty_dates_table} 
                              WHERE spider_name = '{self.name}'
                      )
                    ORDER BY cal_date
                    """  # 期货交易日历共享同一张表，所以这里过滤SSE
            )

            if cal_dates.empty:
                return

            trade_dates = [cal_date.strftime("%Y%m%d") for cal_date in cal_dates["cal_date"]]

            for trade_date in trade_dates:
                yield self.get_scrapy_request(
                    params={self.custom_settings.get('TRADE_DATE_FIELD', 'trade_date'): trade_date},
                    meta={'trade_date': trade_date}
                )
        except Exception as e:
            logging.error(f"Spider {self.name} 在start_requests中出错: {e}")
            logging.exception("异常详细信息:")
            raise

    def parse(self, response, **kwargs):
        try:
            item = self.parse_response(response, **kwargs)
            trade_date = kwargs.get('trade_date', response.meta.get('trade_date', ''))

            if item['data'] is None or len(item['data']) == 0:
                # 记录返回空数据的日期
                logging.warning(f"Spider {self.name} {trade_date} 获取的数据为空，记录该日期")
                try:
                    conn = self.get_db_engine()
                    db_name = self.spider_settings.database.db_name
                    # 使用固定的空数据日期记录表名，所有接口共用
                    empty_dates_table = "empty_data_dates"
                    
                    # 创建DataFrame用于插入
                    empty_data = pd.DataFrame({
                        'trade_date': [pd.to_datetime(trade_date, format='%Y%m%d').date()],
                        'spider_name': [self.name],
                        'create_time': [datetime.datetime.now()]
                    })
                    
                    # 使用insert方法插入数据（ClickHouse会自动处理重复）
                    conn.insert(empty_dates_table, schema={'primary_key': ['trade_date', 'spider_name']}, data=empty_data)
                    logging.info(f"Spider {self.name} 记录空数据日期: {trade_date}")
                except Exception as e:
                    logging.error(f"Spider {self.name} 记录空数据日期时出错: {e}")
                return

            logging.info(f"Spider {self.name} {trade_date} 获取到 {len(item['data'])} 条数据")
            return item
        except Exception as e:
            logging.error(f"Spider {self.name} 解析响应时出错: {e}")
            raise


class TSCodeSpider(TushareSpider):
    name: str
    custom_settings = {'BASIC_TABLE': 'stock_basic'}

    def start_requests(self):
        table_name = self.custom_settings.get('BASIC_TABLE')
        conn = self.get_db_engine()
        db_name = self.spider_settings.database.db_name

        ts_codes = conn.query_df(f"SELECT ts_code FROM {db_name}.{table_name}")

        for ts_code in ts_codes['ts_code']:
            yield self.get_scrapy_request(params={"ts_code": ts_code})


class FinancialReportSpider(TushareSpider):
    name: str
    api_name = "financial_report"

    def start_requests(self):
        # 如果积分大于5000，使用vip接口
        if self.spider_settings.tushare_point >= 5000:
            return self.request_with_vip()
        else:
            return self.request_with_ts_code()

    @staticmethod
    def get_all_period():
        # 获取所有的period
        periods = []
        for year in range(1990, datetime.datetime.now().year + 1):
            for end_date in [f"{year}0331", f"{year}0630", f"{year}0930", f"{year}1231"]:
                periods.append(end_date)
        return periods

    def request_with_vip(self):
        # 每次全量同步即可，30年的数据只有4*30*12=1440次请求
        # 尽管实测半个小时同步完，但是毕竟离线数据，慢点也无妨，后期如果需要再进行优化

        if self.custom_settings.get('HAS_VIP', True):
            self.api_name = self.api_name + "_vip"
        for period in self.get_all_period():
            # 三大报表需要按照report_type分别请求
            if self.api_name.startswith(("income", "balance", "cashflow")):
                for report_type in range(1, 13):
                    params = {"period": period, "report_type": str(report_type)}
                    yield self.get_scrapy_request(params)
            else:
                # 其他报表只需要按period请求即可
                params = {"period": period}
                yield self.get_scrapy_request(params)

    def request_with_ts_code(self):
        # 按ts_code取数据，每次取一个股票的全量，几千次请求
        conn = self.get_db_engine()
        db_name = self.spider_settings.database.db_name
        ts_codes = conn.query_df(f' SELECT ts_code FROM {db_name}.stock_basic')['ts_code']

        for ts_code in ts_codes:
            params = {"ts_code": ts_code, "limit": 2000}
            yield self.get_scrapy_request(params)
