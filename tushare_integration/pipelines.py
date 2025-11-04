# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import datetime
import logging

import pandas as pd
import yaml
from scrapy.exceptions import DropItem

from tushare_integration.db_engine import DatabaseEngineFactory
from tushare_integration.settings import TushareIntegrationSettings


class BasePipeline(object):
    def __init__(self, settings: TushareIntegrationSettings, *args, **kwargs):
        self.settings: TushareIntegrationSettings = settings
        self.schema: dict = {}

    def get_schema(self, schema: str):
        with open(f"tushare_integration/schema/{schema}.yaml", "r", encoding="utf-8") as f:
            self.schema = yaml.safe_load(f.read())

        return self.schema

    def open_spider(self, spider):
        self.schema = self.get_schema(spider.get_schema_name())

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            settings=TushareIntegrationSettings.model_validate(
                yaml.safe_load(open('config_prod.yaml', 'r', encoding='utf8').read())
            )
        )


class TushareIntegrationFillNAPipeline(BasePipeline):
    @staticmethod
    def get_default_by_data_type(data_type: str):
        if data_type is None:
            raise ValueError("data_type is None")

        match data_type:
            case "str":
                return ""
            case "float":
                return 0.0
            case "int":
                return 0
            case "number":
                return 0.0
            case "date":
                return "1970-01-01"
            case "datetime":
                return "1970-01-01 00:00:00"
            case 'json':
                return '{}'
            case _:
                raise ValueError(f"Unsupported data_type: {data_type}")

    def process_item(self, item, spider):
        try:
            data: pd.DataFrame = item["data"]

            # 检查数据是否为空
            if data is None:
                logging.warning(f"Spider {spider.name} 获取的数据为None")
                raise DropItem(f"数据为None")
            
            if len(data) == 0:
                logging.warning(f"Spider {spider.name} 获取的数据为空")
                raise DropItem(f"数据为空")

            logging.info(f"Spider {spider.name} 获取到 {len(data)} 条数据")

            for column in self.schema["columns"]:
                if column.get("default", None) is None:
                    column["default"] = self.get_default_by_data_type(column["data_type"])
                
                # 检查字段是否存在于数据中
                if column["name"] not in data.columns:
                    # 如果字段不存在，添加一个默认值的列
                    data[column["name"]] = column["default"]
                    logging.warning(f"Spider {spider.name} 字段 '{column['name']}' 在API返回的数据中不存在，已使用默认值 '{column['default']}'")
                else:
                    # 需要特殊处理NaT,Pandas的fillna方法不支持NaT
                    try:
                        data[column["name"]] = data[column["name"]].replace({pd.NaT: None}).fillna(column["default"])
                    except Exception as e:
                        logging.error(f"Spider {spider.name} 处理字段 '{column['name']}' 时出错: {e}")
                        raise

            return item
        except Exception as e:
            logging.error(f"Spider {spider.name} 在TushareIntegrationFillNAPipeline中处理数据时出错: {e}")
            raise


class TransformDTypePipeline(BasePipeline):
    def process_item(self, item, spider):
        try:
            data = item["data"]
            
            for column in self.schema["columns"]:
                # 检查字段是否存在于数据中
                if column["name"] not in data.columns:
                    logging.warning(f"Spider {spider.name} 字段 '{column['name']}' 在API返回的数据中不存在，跳过类型转换")
                    continue
                    
                try:
                    match column["data_type"]:
                        case "str":
                            data[column["name"]] = data[column["name"]].astype(str)
                        case "float":
                            data[column["name"]] = data[column["name"]].astype(float)
                        case "int":
                            data[column["name"]] = data[column["name"]].astype(int)
                        case "number":
                            data[column["name"]] = data[column["name"]].astype(float)
                        case "date":
                            data[column["name"]] = pd.to_datetime(data[column["name"]], format='mixed', errors='coerce').dt.date
                            data[column["name"]] = data[column["name"]].replace({pd.NaT: pd.to_datetime('1971-01-01').date()})
                        case "datetime":
                            data[column["name"]] = pd.to_datetime(data[column["name"]])
                        case 'json':
                            data[column["name"]] = data[column["name"]].apply(lambda x: '{}' if pd.isna(x) else x)
                        case _:
                            raise ValueError(f"Unsupported data_type: {column['data_type']}")
                except Exception as e:
                    logging.error(f"Spider {spider.name} 转换字段 '{column['name']}' 为类型 {column['data_type']} 时出错: {e}")
                    raise
                    
            logging.info(f"Spider {spider.name} 数据类型转换完成")
            return item
        except Exception as e:
            logging.error(f"Spider {spider.name} 在TransformDTypePipeline中处理数据时出错: {e}")
            raise


class TushareIntegrationDataPipeline(BasePipeline):
    def __init__(self, settings, *args, **kwargs) -> None:
        super().__init__(settings, *args, **kwargs)

        self.db_engine = DatabaseEngineFactory.create(self.settings)

        self.table_name: str = ""
        self.truncate: bool = False

    def open_spider(self, spider):
        super().open_spider(spider)
        self.table_name = spider.get_table_name()
        logging.info(f"Spider {spider.name} 开始处理数据，目标表: {self.table_name}")

    def process_item(self, item, spider):
        try:
            data: pd.DataFrame = item["data"]

            if data.empty:
                logging.warning(f"Spider {spider.name} 数据为空，跳过数据库操作")
                return item

            logging.info(f"Spider {spider.name} 准备写入 {len(data)} 条数据到表 {self.table_name}")

            if (primary_key := self.schema.get("primary_key", None)) is not None and len(primary_key) > 0:
                # 去重处理
                before_count = len(data)
                data = data.drop_duplicates(subset=primary_key, keep="last")
                after_count = len(data)
                if before_count != after_count:
                    logging.info(f"Spider {spider.name} 去重前: {before_count} 条，去重后: {after_count} 条")
                
                # 执行upsert操作
                try:
                    self.db_engine.upsert(self.table_name, schema=self.schema, data=data)
                    logging.info(f"Spider {spider.name} 成功upsert {after_count} 条数据到表 {self.table_name}")
                except Exception as e:
                    logging.error(f"Spider {spider.name} upsert数据到表 {self.table_name} 时出错: {e}")
                    raise
            else:
                # 执行insert操作
                try:
                    self.db_engine.insert(self.table_name, schema=self.schema, data=data)
                    logging.info(f"Spider {spider.name} 成功insert {len(data)} 条数据到表 {self.table_name}")
                except Exception as e:
                    logging.error(f"Spider {spider.name} insert数据到表 {self.table_name} 时出错: {e}")
                    raise

            return item
        except Exception as e:
            logging.error(f"Spider {spider.name} 在TushareIntegrationDataPipeline中处理数据时出错: {e}")
            raise


class RecordLogPipeline(BasePipeline):
    def __init__(self, settings, *args, **kwargs) -> None:
        super().__init__(settings, *args, **kwargs)

        self.db_engine = DatabaseEngineFactory.create(self.settings)

        self.table_name: str = "tushare_integration_log"

        self.count: int = 0
        self.start_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.create_log_table()

    def create_log_table(self):
        try:
            # 创建tushare_integration_log表
            schema = {
                'primary_key': ['batch_id'],
                'columns': [
                    {
                        'name': 'batch_id',
                        'data_type': 'str',
                        'comment': '批次ID',
                    },
                    {
                        'name': 'spider_name',
                        'data_type': 'str',
                        'comment': '爬虫名称',
                    },
                    {
                        'name': 'description',
                        'data_type': 'str',
                        'comment': '描述',
                    },
                    {
                        'name': 'count',
                        'data_type': 'int',
                        'comment': '数量',
                    },
                    {
                        'name': 'start_time',
                        'data_type': 'datetime',
                        'comment': '开始时间',
                    },
                    {
                        'name': 'end_time',
                        'data_type': 'datetime',
                        'comment': '结束时间',
                    },
                ],
            }

            self.db_engine.create_table(self.table_name, schema)
            
            # 创建empty_data_dates表，用于记录返回空数据的日期
            empty_dates_schema = {
                'primary_key': ['trade_date', 'spider_name'],
                'columns': [
                    {
                        'name': 'trade_date',
                        'data_type': 'date',
                        'comment': '交易日期',
                    },
                    {
                        'name': 'spider_name',
                        'data_type': 'str',
                        'comment': '爬虫名称',
                    },
                    {
                        'name': 'create_time',
                        'data_type': 'datetime',
                        'comment': '创建时间',
                    },
                ],
            }
            
            self.db_engine.create_table("empty_data_dates", empty_dates_schema)
            logging.info("空数据日期记录表创建成功")
        except Exception as e:
            logging.error(f"创建日志表时出错: {e}")
            raise

    def open_spider(self, spider):
        try:
            super().open_spider(spider)
            self.start_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.count = 0
            logging.info(f"Spider {spider.name} 开始运行，开始时间: {self.start_time}")
        except Exception as e:
            logging.error(f"Spider {spider.name} 在RecordLogPipeline.open_spider中出错: {e}")
            raise

    def close_spider(self, spider):
        try:
            end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            logging.info(f"Spider {spider.name} 运行结束，结束时间: {end_time}，处理数据量: {self.count}")
            
            statistics_data = pd.DataFrame(
                [
                    {
                        "batch_id": spider.settings.get("BATCH_ID", ''),
                        "spider_name": spider.name,
                        "description": self.schema.get("name", ""),
                        "count": self.count,
                        "start_time": self.start_time,
                        "end_time": end_time,
                    }
                ]
            )

            statistics_data[['start_time', 'end_time']] = statistics_data[['start_time', 'end_time']].apply(pd.to_datetime)

            self.db_engine.insert(self.table_name, self.schema, statistics_data)
            logging.info(f"Spider {spider.name} 运行记录已保存到日志表")
        except Exception as e:
            logging.error(f"Spider {spider.name} 在RecordLogPipeline.close_spider中出错: {e}")
            raise

    def process_item(self, item, spider):
        try:
            self.count += len(item["data"])
            return item
        except Exception as e:
            logging.error(f"Spider {spider.name} 在RecordLogPipeline.process_item中出错: {e}")
            raise
