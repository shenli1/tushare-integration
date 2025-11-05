# Tushare Integration 数据库说明书

**生成时间**: 2025-11-05 22:44:49

## 目录

- [股票-基础信息](#股票-基础信息)
- [股票-财务数据](#股票-财务数据)
- [股票-行情数据](#股票-行情数据)
- [股票-市场数据](#股票-市场数据)
- [股票-资金流向](#股票-资金流向)
- [股票-融资融券](#股票-融资融券)
- [股票-涨跌停](#股票-涨跌停)
- [股票-特殊数据](#股票-特殊数据)
- [指数-基础信息](#指数-基础信息)
- [指数-行情数据](#指数-行情数据)
- [指数-SW分类](#指数-sw分类)
- [指数-同花顺](#指数-同花顺)
- [指数-中信](#指数-中信)
- [期货-基础信息](#期货-基础信息)
- [期货-行情数据](#期货-行情数据)

---

## 股票-基础信息 {#股票-基础信息}

本分类共包含 **10** 个数据表。

### 表列表

- [stock_basic](#stock-basic) - 基础信息
- [trade_cal](#trade-cal) - 交易日历
- [namechange](#namechange) - 股票曾用名
- [hs_const](#hs-const) - 沪深股通成份股
- [stock_company](#stock-company) - 上市公司基本信息
- [new_share](#new-share) - IPO新股列表
- [stk_managers](#stk-managers) - 上市公司管理层
- [stk_rewards](#stk-rewards) - 管理层薪酬和持股
- [bak_basic](#bak-basic) - 备用列表
- [stk_premarket](#stk-premarket) - 股本情况（盘前）

### stock_basic

**表名**: `stock_basic` | **说明**: 基础信息 | **主键**: `ts_code`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | TS代码 |
| `symbol` | VARCHAR(255) | 255 | `` | 股票代码 |
| `name` | VARCHAR(255) | 255 | `` | 股票名称 |
| `area` | VARCHAR(255) | 255 | `` | 地域 |
| `industry` | VARCHAR(255) | 255 | `` | 所属行业 |
| `fullname` | VARCHAR(255) | 255 | `` | 股票全称 |
| `enname` | VARCHAR(255) | 255 | `` | 英文全称 |
| `cnspell` | VARCHAR(255) | 255 | `` | 拼音缩写 |
| `market` | VARCHAR(255) | 255 | `` | 市场类型 |
| `exchange` | VARCHAR(255) | 255 | `` | 交易所代码 |
| `curr_type` | VARCHAR(255) | 255 | `` | 交易货币 |
| `list_status` | VARCHAR(255) | 255 | `` | 上市状态 L上市 D退市 P暂停上市 |
| `list_date` | DATE | - | `1970-01-01` | 上市日期 |
| `delist_date` | DATE | - | `1970-01-01` | 退市日期 |
| `is_hs` | VARCHAR(255) | 255 | `` | 是否沪 |
| `act_name` | VARCHAR(255) | 255 | `` | 实控人名称 |
| `act_ent_type` | VARCHAR(255) | 255 | `` | 实控人企业性质 |

---

### trade_cal

**表名**: `trade_cal` | **说明**: 交易日历 | **主键**: `cal_date`, `exchange`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `exchange` | VARCHAR(255) | 255 | `` | 交易所 SSE上交所 SZSE深交所 |
| `cal_date` | DATE | - | `1970-01-01` | 日历日期 |
| `is_open` | INTEGER | - | `0` | 是否交易 0休市 1交易 |
| `pretrade_date` | DATE | - | `1970-01-01` | 上一个交易日 |

---

### namechange

**表名**: `namechange` | **说明**: 股票曾用名 | **主键**: `ts_code`, `name`, `ann_date` | **依赖表**: `stock/basic/stock_basic`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | TS代码 |
| `name` | VARCHAR(255) | 255 | `` | 证券名称 |
| `start_date` | DATE | - | `1970-01-01` | 开始日期 |
| `end_date` | DATE | - | `1970-01-01` | 结束日期 |
| `ann_date` | DATE | - | `1970-01-01` | 公告日期 |
| `change_reason` | VARCHAR(255) | 255 | `` | 变更原因 |

---

### hs_const

**表名**: `hs_const` | **说明**: 沪深股通成份股 | **主键**: `ts_code`, `hs_type`, `in_date` | **依赖表**: `stock/basic/stock_basic`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | TS代码 |
| `hs_type` | VARCHAR(255) | 255 | `` | 沪深港通类型SH沪SZ深 |
| `in_date` | DATE | - | `1970-01-01` | 纳入日期 |
| `out_date` | DATE | - | `1970-01-01` | 剔除日期 |
| `is_new` | VARCHAR(255) | 255 | `` | 是否最新 |

---

### stock_company

**表名**: `stock_company` | **说明**: 上市公司基本信息 | **主键**: `ts_code` | **依赖表**: `stock/basic/stock_basic`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | 股票代码 |
| `exchange` | VARCHAR(255) | 255 | `` | 交易所代码SSE上交所 SZSE深交所 HKEX港交所 |
| `chairman` | VARCHAR(255) | 255 | `` | 法人代表 |
| `com_name` | VARCHAR(255) | 255 | `` | 公司全称 |
| `com_id` | VARCHAR(255) | 255 | `` | 统一社会信用代码 |
| `manager` | VARCHAR(255) | 255 | `` | 总经理 |
| `secretary` | VARCHAR(255) | 255 | `` | 董秘 |
| `reg_capital` | DOUBLE | - | `0.0` | 注册资本 |
| `setup_date` | DATE | - | `1970-01-01` | 注册日期 |
| `province` | VARCHAR(255) | 255 | `` | 所在省份 |
| `city` | VARCHAR(255) | 255 | `` | 所在城市 |
| `introduction` | VARCHAR(255) | 255 | `` | 公司介绍 |
| `website` | VARCHAR(255) | 255 | `` | 公司主页 |
| `email` | VARCHAR(255) | 255 | `` | 电子邮件 |
| `office` | VARCHAR(255) | 255 | `` | 办公室 |
| `ann_date` | DATE | - | `1970-01-01` | 公告日期 |
| `business_scope` | VARCHAR(255) | 255 | `` | 经营范围 |
| `employees` | INTEGER | - | `0` | 员工人数 |
| `main_business` | VARCHAR(255) | 255 | `` | 主要业务及产品 |

---

### new_share

**表名**: `new_share` | **说明**: IPO新股列表 | **主键**: `ts_code`, `sub_code` | **依赖表**: `stock/basic/stock_basic`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | TS股票代码 |
| `sub_code` | VARCHAR(255) | 255 | `` | 申购代码 |
| `name` | VARCHAR(255) | 255 | `` | 名称 |
| `ipo_date` | DATE | - | `1970-01-01` | 上网发行日期 |
| `issue_date` | DATE | - | `1970-01-01` | 上市日期 |
| `amount` | DOUBLE | - | `0.0` | 发行总量（万股） |
| `market_amount` | DOUBLE | - | `0.0` | 上网发行总量（万股） |
| `price` | DOUBLE | - | `0.0` | 发行价格 |
| `pe` | DOUBLE | - | `0.0` | 市盈率 |
| `limit_amount` | DOUBLE | - | `0.0` | 个人申购上限（万股） |
| `funds` | DOUBLE | - | `0.0` | 募集资金（亿元） |
| `ballot` | DOUBLE | - | `0.0` | 中签率 |

---

### stk_managers

**表名**: `stk_managers` | **说明**: 上市公司管理层 | **主键**: `ts_code`, `ann_date`, `name`, `title` | **依赖表**: `stock/basic/stock_basic`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | TS股票代码 |
| `ann_date` | DATE | - | `1970-01-01` | 公告日期 |
| `name` | VARCHAR(255) | 255 | `` | 姓名 |
| `gender` | VARCHAR(255) | 255 | `` | 性别 |
| `lev` | VARCHAR(255) | 255 | `` | 岗位类别 |
| `title` | VARCHAR(255) | 255 | `` | 岗位 |
| `edu` | VARCHAR(255) | 255 | `` | 学历 |
| `national` | VARCHAR(255) | 255 | `` | 国籍 |
| `birthday` | VARCHAR(255) | 255 | `` | 出生年份 |
| `begin_date` | DATE | - | `1970-01-01` | 上任日期 |
| `end_date` | DATE | - | `1970-01-01` | 离任日期 |
| `resume` | VARCHAR(255) | 255 | `` | 个人简历 |

---

### stk_rewards

**表名**: `stk_rewards` | **说明**: 管理层薪酬和持股 | **主键**: `ts_code`, `ann_date`, `name`, `title` | **依赖表**: `stock/basic/stock_basic`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | TS股票代码 |
| `ann_date` | DATE | - | `1970-01-01` | 公告日期 |
| `end_date` | DATE | - | `1970-01-01` | 报告期 |
| `name` | VARCHAR(255) | 255 | `` | 姓名 |
| `title` | VARCHAR(255) | 255 | `` | 职务 |
| `reward` | DOUBLE | - | `0.0` | 报酬 |
| `hold_vol` | DOUBLE | - | `0.0` | 持股数 |

---

### bak_basic

**表名**: `bak_basic` | **说明**: 备用列表 | **主键**: `ts_code`, `trade_date` | **依赖表**: `stock/basic/stock_basic`, `stock/basic/trade_cal`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `ts_code` | VARCHAR(16) | 16 | `` | TS股票代码 |
| `name` | VARCHAR(255) | 255 | `` | 股票名称 |
| `industry` | VARCHAR(255) | 255 | `` | 行业 |
| `area` | VARCHAR(255) | 255 | `` | 地域 |
| `pe` | DOUBLE | - | `0.0` | 市盈率（动） |
| `float_share` | DOUBLE | - | `0.0` | 流通股本（万） |
| `total_share` | DOUBLE | - | `0.0` | 总股本（万） |
| `total_assets` | DOUBLE | - | `0.0` | 总资产（万） |
| `liquid_assets` | DOUBLE | - | `0.0` | 流动资产（万） |
| `fixed_assets` | DOUBLE | - | `0.0` | 固定资产（万） |
| `reserved` | DOUBLE | - | `0.0` | 公积金 |
| `reserved_pershare` | DOUBLE | - | `0.0` | 每股公积金 |
| `eps` | DOUBLE | - | `0.0` | 每股收益 |
| `bvps` | DOUBLE | - | `0.0` | 每股净资产 |
| `pb` | DOUBLE | - | `0.0` | 市净率 |
| `list_date` | DATE | - | `1970-01-01` | 上市日期 |
| `undp` | DOUBLE | - | `0.0` | 未分配利润 |
| `per_undp` | DOUBLE | - | `0.0` | 每股未分配利润 |
| `rev_yoy` | DOUBLE | - | `0.0` | 收入同比（%） |
| `profit_yoy` | DOUBLE | - | `0.0` | 利润同比（%） |
| `gpr` | DOUBLE | - | `0.0` | 毛利率（%） |
| `npr` | DOUBLE | - | `0.0` | 净利润率（%） |
| `holder_num` | INTEGER | - | `0` | 股东人数 |

---

### stk_premarket

**表名**: `stk_premarket` | **说明**: 股本情况（盘前） | **主键**: `ts_code`, `trade_date` | **依赖表**: `stock/basic/stock_basic`, `stock/basic/trade_cal`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `ts_code` | VARCHAR(16) | 16 | `` | TS股票代码 |
| `total_share` | DOUBLE | - | `0.0` | 总股本 |
| `float_share` | DOUBLE | - | `0.0` | 流通股本 |
| `pre_close` | DOUBLE | - | `0.0` | 昨日收盘价 |
| `up_limit` | DOUBLE | - | `0.0` | 涨停价 |
| `down_limit` | DOUBLE | - | `0.0` | 跌停价 |

---

## 股票-财务数据 {#股票-财务数据}

本分类共包含 **10** 个数据表。

### 表列表

- [income](#income) - 利润表
- [balancesheet](#balancesheet) - 资产负债表
- [cashflow](#cashflow) - 现金流量表
- [forecast](#forecast) - 业绩预告
- [express](#express) - 业绩快报
- [fina_indicator](#fina-indicator) - 财务指标数据
- [fina_audit](#fina-audit) - 财务审计意见
- [fina_mainbz](#fina-mainbz) - 主营业务构成
- [dividend](#dividend) - 分红送股
- [disclosure_date](#disclosure-date) - 财报披露计划

### income

**表名**: `income` | **说明**: 利润表 | **主键**: `ts_code`, `ann_date`, `f_ann_date`, `end_date`, `report_type`, `update_flag` | **依赖表**: `stock/basic/stock_basic`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | TS代码 |
| `ann_date` | DATE | - | `1970-01-01` | 公告日期 |
| `f_ann_date` | DATE | - | `1970-01-01` | 实际公告日期 |
| `end_date` | DATE | - | `1970-01-01` | 报告期 |
| `report_type` | VARCHAR(16) | 16 | `` | 报告类型 1合并报表 2单季合并 3调整单季合并表 4调整合并报表 5调整前合并报表 6母公司报表 7母公司单季表 8 母公司调整单季表 9母公司调整表 10母公司调整前报表 11调整前合并报表 12母公司调整前报表 |
| `comp_type` | VARCHAR(255) | 255 | `` | 公司类型(1一般工商业2银行3保险4证券) |
| `end_type` | VARCHAR(255) | 255 | `` | 报告期类型 |
| `basic_eps` | DOUBLE | - | `0.0` | 基本每股收益 |
| `diluted_eps` | DOUBLE | - | `0.0` | 稀释每股收益 |
| `total_revenue` | DOUBLE | - | `0.0` | 营业总收入 |
| `revenue` | DOUBLE | - | `0.0` | 营业收入 |
| `int_income` | DOUBLE | - | `0.0` | 利息收入 |
| `prem_earned` | DOUBLE | - | `0.0` | 已赚保费 |
| `comm_income` | DOUBLE | - | `0.0` | 手续费及佣金收入 |
| `n_commis_income` | DOUBLE | - | `0.0` | 手续费及佣金净收入 |
| `n_oth_income` | DOUBLE | - | `0.0` | 其他经营净收益 |
| `n_oth_b_income` | DOUBLE | - | `0.0` | 加:其他业务净收益 |
| `prem_income` | DOUBLE | - | `0.0` | 保险业务收入 |
| `out_prem` | DOUBLE | - | `0.0` | 减:分出保费 |
| `une_prem_reser` | DOUBLE | - | `0.0` | 提取未到期责任准备金 |
| `reins_income` | DOUBLE | - | `0.0` | 其中:分保费收入 |
| `n_sec_tb_income` | DOUBLE | - | `0.0` | 代理买卖证券业务净收入 |
| `n_sec_uw_income` | DOUBLE | - | `0.0` | 证券承销业务净收入 |
| `n_asset_mg_income` | DOUBLE | - | `0.0` | 受托客户资产管理业务净收入 |
| `oth_b_income` | DOUBLE | - | `0.0` | 其他业务收入 |
| `fv_value_chg_gain` | DOUBLE | - | `0.0` | 加:公允价值变动净收益 |
| `invest_income` | DOUBLE | - | `0.0` | 加:投资净收益 |
| `ass_invest_income` | DOUBLE | - | `0.0` | 其中:对联营企业和合营企业的投资收益 |
| `forex_gain` | DOUBLE | - | `0.0` | 加:汇兑净收益 |
| `total_cogs` | DOUBLE | - | `0.0` | 营业总成本 |
| `oper_cost` | DOUBLE | - | `0.0` | 减:营业成本 |
| `int_exp` | DOUBLE | - | `0.0` | 减:利息支出 |
| `comm_exp` | DOUBLE | - | `0.0` | 减:手续费及佣金支出 |
| `biz_tax_surchg` | DOUBLE | - | `0.0` | 减:营业税金及附加 |
| `sell_exp` | DOUBLE | - | `0.0` | 减:销售费用 |
| `admin_exp` | DOUBLE | - | `0.0` | 减:管理费用 |
| `fin_exp` | DOUBLE | - | `0.0` | 减:财务费用 |
| `assets_impair_loss` | DOUBLE | - | `0.0` | 减:资产减值损失 |
| `prem_refund` | DOUBLE | - | `0.0` | 退保金 |
| `compens_payout` | DOUBLE | - | `0.0` | 赔付总支出 |
| `reser_insur_liab` | DOUBLE | - | `0.0` | 提取保险责任准备金 |
| `div_payt` | DOUBLE | - | `0.0` | 保户红利支出 |
| `reins_exp` | DOUBLE | - | `0.0` | 分保费用 |
| `oper_exp` | DOUBLE | - | `0.0` | 营业支出 |
| `compens_payout_refu` | DOUBLE | - | `0.0` | 减:摊回赔付支出 |
| `insur_reser_refu` | DOUBLE | - | `0.0` | 减:摊回保险责任准备金 |
| `reins_cost_refund` | DOUBLE | - | `0.0` | 减:摊回分保费用 |
| `other_bus_cost` | DOUBLE | - | `0.0` | 其他业务成本 |
| `operate_profit` | DOUBLE | - | `0.0` | 营业利润 |
| `non_oper_income` | DOUBLE | - | `0.0` | 加:营业外收入 |
| `non_oper_exp` | DOUBLE | - | `0.0` | 减:营业外支出 |
| `nca_disploss` | DOUBLE | - | `0.0` | 其中:减:非流动资产处置净损失 |
| `total_profit` | DOUBLE | - | `0.0` | 利润总额 |
| `income_tax` | DOUBLE | - | `0.0` | 所得税费用 |
| `n_income` | DOUBLE | - | `0.0` | 净利润(含少数股东损益) |
| `n_income_attr_p` | DOUBLE | - | `0.0` | 净利润(不含少数股东损益) |
| `minority_gain` | DOUBLE | - | `0.0` | 少数股东损益 |
| `oth_compr_income` | DOUBLE | - | `0.0` | 其他综合收益 |
| `t_compr_income` | DOUBLE | - | `0.0` | 综合收益总额 |
| `compr_inc_attr_p` | DOUBLE | - | `0.0` | 归属于母公司(或股东)的综合收益总额 |
| `compr_inc_attr_m_s` | DOUBLE | - | `0.0` | 归属于少数股东的综合收益总额 |
| `ebit` | DOUBLE | - | `0.0` | 息税前利润 |
| `ebitda` | DOUBLE | - | `0.0` | 息税折旧摊销前利润 |
| `insurance_exp` | DOUBLE | - | `0.0` | 保险业务支出 |
| `undist_profit` | DOUBLE | - | `0.0` | 年初未分配利润 |
| `distable_profit` | DOUBLE | - | `0.0` | 可分配利润 |
| `rd_exp` | DOUBLE | - | `0.0` | 研发费用 |
| `fin_exp_int_exp` | DOUBLE | - | `0.0` | 财务费用:利息费用 |
| `fin_exp_int_inc` | DOUBLE | - | `0.0` | 财务费用:利息收入 |
| `transfer_surplus_rese` | DOUBLE | - | `0.0` | 盈余公积转入 |
| `transfer_housing_imprest` | DOUBLE | - | `0.0` | 住房周转金转入 |
| `transfer_oth` | DOUBLE | - | `0.0` | 其他转入 |
| `adj_lossgain` | DOUBLE | - | `0.0` | 调整以前年度损益 |
| `withdra_legal_surplus` | DOUBLE | - | `0.0` | 提取法定盈余公积 |
| `withdra_legal_pubfund` | DOUBLE | - | `0.0` | 提取法定公益金 |
| `withdra_biz_devfund` | DOUBLE | - | `0.0` | 提取企业发展基金 |
| `withdra_rese_fund` | DOUBLE | - | `0.0` | 提取储备基金 |
| `withdra_oth_ersu` | DOUBLE | - | `0.0` | 提取任意盈余公积金 |
| `workers_welfare` | DOUBLE | - | `0.0` | 职工奖金福利 |
| `distr_profit_shrhder` | DOUBLE | - | `0.0` | 可供股东分配的利润 |
| `prfshare_payable_dvd` | DOUBLE | - | `0.0` | 应付优先股股利 |
| `comshare_payable_dvd` | DOUBLE | - | `0.0` | 应付普通股股利 |
| `capit_comstock_div` | DOUBLE | - | `0.0` | 转作股本的普通股股利 |
| `net_after_nr_lp_correct` | DOUBLE | - | `0.0` | 扣除非经常性损益后的净利润（更正前） |
| `oth_income` | DOUBLE | - | `0.0` | 其他收益 |
| `asset_disp_income` | DOUBLE | - | `0.0` | 资产处置收益 |
| `continued_net_profit` | DOUBLE | - | `0.0` | 持续经营净利润 |
| `end_net_profit` | DOUBLE | - | `0.0` | 终止经营净利润 |
| `credit_impa_loss` | DOUBLE | - | `0.0` | 信用减值损失 |
| `net_expo_hedging_benefits` | DOUBLE | - | `0.0` | 净敞口套期收益 |
| `oth_impair_loss_assets` | DOUBLE | - | `0.0` | 其他资产减值损失 |
| `total_opcost` | DOUBLE | - | `0.0` | 营业总成本2 |
| `amodcost_fin_assets` | DOUBLE | - | `0.0` | 以摊余成本计量的金融资产终止确认收益 |
| `update_flag` | INTEGER | - | `0` | 更新标识 |

---

### balancesheet

**表名**: `balancesheet` | **说明**: 资产负债表 | **主键**: `ts_code`, `ann_date`, `f_ann_date`, `end_date`, `report_type`, `update_flag` | **依赖表**: `stock/basic/stock_basic`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | TS股票代码 |
| `ann_date` | DATE | - | `1970-01-01` | 公告日期 |
| `f_ann_date` | DATE | - | `1970-01-01` | 实际公告日期 |
| `end_date` | DATE | - | `1970-01-01` | 报告期 |
| `report_type` | VARCHAR(16) | 16 | `` | 报表类型 |
| `comp_type` | VARCHAR(255) | 255 | `` | 公司类型(1一般工商业2银行3保险4证券) |
| `end_type` | VARCHAR(255) | 255 | `` | 报告期类型 |
| `total_share` | DOUBLE | - | `0.0` | 期末总股本 |
| `cap_rese` | DOUBLE | - | `0.0` | 资本公积金 |
| `undistr_porfit` | DOUBLE | - | `0.0` | 未分配利润 |
| `surplus_rese` | DOUBLE | - | `0.0` | 盈余公积金 |
| `special_rese` | DOUBLE | - | `0.0` | 专项储备 |
| `money_cap` | DOUBLE | - | `0.0` | 货币资金 |
| `trad_asset` | DOUBLE | - | `0.0` | 交易性金融资产 |
| `notes_receiv` | DOUBLE | - | `0.0` | 应收票据 |
| `accounts_receiv` | DOUBLE | - | `0.0` | 应收账款 |
| `oth_receiv` | DOUBLE | - | `0.0` | 其他应收款 |
| `prepayment` | DOUBLE | - | `0.0` | 预付款项 |
| `div_receiv` | DOUBLE | - | `0.0` | 应收股利 |
| `int_receiv` | DOUBLE | - | `0.0` | 应收利息 |
| `inventories` | DOUBLE | - | `0.0` | 存货 |
| `amor_exp` | DOUBLE | - | `0.0` | 长期待摊费用 |
| `nca_within_1y` | DOUBLE | - | `0.0` | 一年内到期的非流动资产 |
| `sett_rsrv` | DOUBLE | - | `0.0` | 结算备付金 |
| `loanto_oth_bank_fi` | DOUBLE | - | `0.0` | 拆出资金 |
| `premium_receiv` | DOUBLE | - | `0.0` | 应收保费 |
| `reinsur_receiv` | DOUBLE | - | `0.0` | 应收分保账款 |
| `reinsur_res_receiv` | DOUBLE | - | `0.0` | 应收分保合同准备金 |
| `pur_resale_fa` | DOUBLE | - | `0.0` | 买入返售金融资产 |
| `oth_cur_assets` | DOUBLE | - | `0.0` | 其他流动资产 |
| `total_cur_assets` | DOUBLE | - | `0.0` | 流动资产合计 |
| `fa_avail_for_sale` | DOUBLE | - | `0.0` | 可供出售金融资产 |
| `htm_invest` | DOUBLE | - | `0.0` | 持有至到期投资 |
| `lt_eqt_invest` | DOUBLE | - | `0.0` | 长期股权投资 |
| `invest_real_estate` | DOUBLE | - | `0.0` | 投资性房地产 |
| `time_deposits` | DOUBLE | - | `0.0` | 定期存款 |
| `oth_assets` | DOUBLE | - | `0.0` | 其他资产 |
| `lt_rec` | DOUBLE | - | `0.0` | 长期应收款 |
| `fix_assets` | DOUBLE | - | `0.0` | 固定资产 |
| `cip` | DOUBLE | - | `0.0` | 在建工程 |
| `const_materials` | DOUBLE | - | `0.0` | 工程物资 |
| `fixed_assets_disp` | DOUBLE | - | `0.0` | 固定资产清理 |
| `produc_bio_assets` | DOUBLE | - | `0.0` | 生产性生物资产 |
| `oil_and_gas_assets` | DOUBLE | - | `0.0` | 油气资产 |
| `intan_assets` | DOUBLE | - | `0.0` | 无形资产 |
| `r_and_d` | DOUBLE | - | `0.0` | 研发支出 |
| `goodwill` | DOUBLE | - | `0.0` | 商誉 |
| `lt_amor_exp` | DOUBLE | - | `0.0` | 长期待摊费用 |
| `defer_tax_assets` | DOUBLE | - | `0.0` | 递延所得税资产 |
| `decr_in_disbur` | DOUBLE | - | `0.0` | 发放贷款及垫款 |
| `oth_nca` | DOUBLE | - | `0.0` | 其他非流动资产 |
| `total_nca` | DOUBLE | - | `0.0` | 非流动资产合计 |
| `cash_reser_cb` | DOUBLE | - | `0.0` | 现金及存放中央银行款项 |
| `depos_in_oth_bfi` | DOUBLE | - | `0.0` | 存放同业和其它金融机构款项 |
| `prec_metals` | DOUBLE | - | `0.0` | 贵金属 |
| `deriv_assets` | DOUBLE | - | `0.0` | 衍生金融资产 |
| `rr_reins_une_prem` | DOUBLE | - | `0.0` | 应收分保未到期责任准备金 |
| `rr_reins_outstd_cla` | DOUBLE | - | `0.0` | 应收分保未决赔款准备金 |
| `rr_reins_lins_liab` | DOUBLE | - | `0.0` | 应收分保寿险责任准备金 |
| `rr_reins_lthins_liab` | DOUBLE | - | `0.0` | 应收分保长期健康险责任准备金 |
| `refund_depos` | DOUBLE | - | `0.0` | 存出保证金 |
| `ph_pledge_loans` | DOUBLE | - | `0.0` | 保户质押贷款 |
| `refund_cap_depos` | DOUBLE | - | `0.0` | 存出资本保证金 |
| `indep_acct_assets` | DOUBLE | - | `0.0` | 独立账户资产 |
| `client_depos` | DOUBLE | - | `0.0` | 其中：客户资金存款 |
| `client_prov` | DOUBLE | - | `0.0` | 其中：客户备付金 |
| `transac_seat_fee` | DOUBLE | - | `0.0` | 其中:交易席位费 |
| `invest_as_receiv` | DOUBLE | - | `0.0` | 应收款项类投资 |
| `total_assets` | DOUBLE | - | `0.0` | 资产总计 |
| `lt_borr` | DOUBLE | - | `0.0` | 长期借款 |
| `st_borr` | DOUBLE | - | `0.0` | 短期借款 |
| `cb_borr` | DOUBLE | - | `0.0` | 向中央银行借款 |
| `depos_ib_deposits` | DOUBLE | - | `0.0` | 吸收存款及同业存放 |
| `loan_oth_bank` | DOUBLE | - | `0.0` | 拆入资金 |
| `trading_fl` | DOUBLE | - | `0.0` | 交易性金融负债 |
| `notes_payable` | DOUBLE | - | `0.0` | 应付票据 |
| `acct_payable` | DOUBLE | - | `0.0` | 应付账款 |
| `adv_receipts` | DOUBLE | - | `0.0` | 预收款项 |
| `sold_for_repur_fa` | DOUBLE | - | `0.0` | 卖出回购金融资产款 |
| `comm_payable` | DOUBLE | - | `0.0` | 应付手续费及佣金 |
| `payroll_payable` | DOUBLE | - | `0.0` | 应付职工薪酬 |
| `taxes_payable` | DOUBLE | - | `0.0` | 应交税费 |
| `int_payable` | DOUBLE | - | `0.0` | 应付利息 |
| `div_payable` | DOUBLE | - | `0.0` | 应付股利 |
| `oth_payable` | DOUBLE | - | `0.0` | 其他应付款 |
| `acc_exp` | DOUBLE | - | `0.0` | 预提费用 |
| `deferred_inc` | DOUBLE | - | `0.0` | 递延收益 |
| `st_bonds_payable` | DOUBLE | - | `0.0` | 应付短期债券 |
| `payable_to_reinsurer` | DOUBLE | - | `0.0` | 应付分保账款 |
| `rsrv_insur_cont` | DOUBLE | - | `0.0` | 保险合同准备金 |
| `acting_trading_sec` | DOUBLE | - | `0.0` | 代理买卖证券款 |
| `acting_uw_sec` | DOUBLE | - | `0.0` | 代理承销证券款 |
| `non_cur_liab_due_1y` | DOUBLE | - | `0.0` | 一年内到期的非流动负债 |
| `oth_cur_liab` | DOUBLE | - | `0.0` | 其他流动负债 |
| `total_cur_liab` | DOUBLE | - | `0.0` | 流动负债合计 |
| `bond_payable` | DOUBLE | - | `0.0` | 应付债券 |
| `lt_payable` | DOUBLE | - | `0.0` | 长期应付款 |
| `specific_payables` | DOUBLE | - | `0.0` | 专项应付款 |
| `estimated_liab` | DOUBLE | - | `0.0` | 预计负债 |
| `defer_tax_liab` | DOUBLE | - | `0.0` | 递延所得税负债 |
| `defer_inc_non_cur_liab` | DOUBLE | - | `0.0` | 递延收益-非流动负债 |
| `oth_ncl` | DOUBLE | - | `0.0` | 其他非流动负债 |
| `total_ncl` | DOUBLE | - | `0.0` | 非流动负债合计 |
| `depos_oth_bfi` | DOUBLE | - | `0.0` | 同业和其它金融机构存放款项 |
| `deriv_liab` | DOUBLE | - | `0.0` | 衍生金融负债 |
| `depos` | DOUBLE | - | `0.0` | 吸收存款 |
| `agency_bus_liab` | DOUBLE | - | `0.0` | 代理业务负债 |
| `oth_liab` | DOUBLE | - | `0.0` | 其他负债 |
| `prem_receiv_adva` | DOUBLE | - | `0.0` | 预收保费 |
| `depos_received` | DOUBLE | - | `0.0` | 存入保证金 |
| `ph_invest` | DOUBLE | - | `0.0` | 保户储金及投资款 |
| `reser_une_prem` | DOUBLE | - | `0.0` | 未到期责任准备金 |
| `reser_outstd_claims` | DOUBLE | - | `0.0` | 未决赔款准备金 |
| `reser_lins_liab` | DOUBLE | - | `0.0` | 寿险责任准备金 |
| `reser_lthins_liab` | DOUBLE | - | `0.0` | 长期健康险责任准备金 |
| `indept_acc_liab` | DOUBLE | - | `0.0` | 独立账户负债 |
| `pledge_borr` | DOUBLE | - | `0.0` | 其中:质押借款 |
| `indem_payable` | DOUBLE | - | `0.0` | 应付赔付款 |
| `policy_div_payable` | DOUBLE | - | `0.0` | 应付保单红利 |
| `total_liab` | DOUBLE | - | `0.0` | 负债合计 |
| `treasury_share` | DOUBLE | - | `0.0` | 减:库存股 |
| `ordin_risk_reser` | DOUBLE | - | `0.0` | 一般风险准备 |
| `forex_differ` | DOUBLE | - | `0.0` | 外币报表折算差额 |
| `invest_loss_unconf` | DOUBLE | - | `0.0` | 未确认的投资损失 |
| `minority_int` | DOUBLE | - | `0.0` | 少数股东权益 |
| `total_hldr_eqy_exc_min_int` | DOUBLE | - | `0.0` | 股东权益合计(不含少数股东权益) |
| `total_hldr_eqy_inc_min_int` | DOUBLE | - | `0.0` | 股东权益合计(含少数股东权益) |
| `total_liab_hldr_eqy` | DOUBLE | - | `0.0` | 负债及股东权益总计 |
| `lt_payroll_payable` | DOUBLE | - | `0.0` | 长期应付职工薪酬 |
| `oth_comp_income` | DOUBLE | - | `0.0` | 其他综合收益 |
| `oth_eqt_tools` | DOUBLE | - | `0.0` | 其他权益工具 |
| `oth_eqt_tools_p_shr` | DOUBLE | - | `0.0` | 其他权益工具(优先股) |
| `lending_funds` | DOUBLE | - | `0.0` | 融出资金 |
| `acc_receivable` | DOUBLE | - | `0.0` | 应收款项 |
| `st_fin_payable` | DOUBLE | - | `0.0` | 应付短期融资款 |
| `payables` | DOUBLE | - | `0.0` | 应付款项 |
| `hfs_assets` | DOUBLE | - | `0.0` | 持有待售的资产 |
| `hfs_sales` | DOUBLE | - | `0.0` | 持有待售的负债 |
| `cost_fin_assets` | DOUBLE | - | `0.0` | 以摊余成本计量的金融资产 |
| `fair_value_fin_assets` | DOUBLE | - | `0.0` | 以公允价值计量且其变动计入其他综合收益的金融资产 |
| `contract_assets` | DOUBLE | - | `0.0` | 合同资产 |
| `contract_liab` | DOUBLE | - | `0.0` | 合同负债 |
| `accounts_receiv_bill` | DOUBLE | - | `0.0` | 应收票据及应收账款 |
| `accounts_pay` | DOUBLE | - | `0.0` | 应付票据及应付账款 |
| `oth_rcv_total` | DOUBLE | - | `0.0` | 其他应收款(合计)（元） |
| `fix_assets_total` | DOUBLE | - | `0.0` | 固定资产(合计)(元) |
| `cip_total` | DOUBLE | - | `0.0` | 在建工程(合计)(元) |
| `oth_pay_total` | DOUBLE | - | `0.0` | 其他应付款(合计)(元) |
| `long_pay_total` | DOUBLE | - | `0.0` | 长期应付款(合计)(元) |
| `debt_invest` | DOUBLE | - | `0.0` | 债权投资(元) |
| `oth_debt_invest` | DOUBLE | - | `0.0` | 其他债权投资(元) |
| `oth_eq_invest` | DOUBLE | - | `0.0` | 其他权益工具投资(元) |
| `oth_illiq_fin_assets` | DOUBLE | - | `0.0` | 其他非流动金融资产(元) |
| `oth_eq_ppbond` | DOUBLE | - | `0.0` | 其他权益工具:永续债(元) |
| `receiv_financing` | DOUBLE | - | `0.0` | 应收款项融资 |
| `use_right_assets` | DOUBLE | - | `0.0` | 使用权资产 |
| `lease_liab` | DOUBLE | - | `0.0` | 租赁负债 |
| `update_flag` | INTEGER | - | `0` | 更新标识 |

---

### cashflow

**表名**: `cashflow` | **说明**: 现金流量表 | **主键**: `ts_code`, `ann_date`, `f_ann_date`, `end_date`, `report_type`, `update_flag` | **依赖表**: `stock/basic/stock_basic`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | TS股票代码 |
| `ann_date` | DATE | - | `1970-01-01` | 公告日期 |
| `f_ann_date` | DATE | - | `1970-01-01` | 实际公告日期 |
| `end_date` | DATE | - | `1970-01-01` | 报告期 |
| `comp_type` | VARCHAR(255) | 255 | `` | 公司类型(1一般工商业2银行3保险4证券) |
| `report_type` | VARCHAR(16) | 16 | `` | 报表类型 |
| `end_type` | VARCHAR(255) | 255 | `` | 报告期类型 |
| `net_profit` | DOUBLE | - | `0.0` | 净利润 |
| `finan_exp` | DOUBLE | - | `0.0` | 财务费用 |
| `c_fr_sale_sg` | DOUBLE | - | `0.0` | 销售商品、提供劳务收到的现金 |
| `recp_tax_rends` | DOUBLE | - | `0.0` | 收到的税费返还 |
| `n_depos_incr_fi` | DOUBLE | - | `0.0` | 客户存款和同业存放款项净增加额 |
| `n_incr_loans_cb` | DOUBLE | - | `0.0` | 向中央银行借款净增加额 |
| `n_inc_borr_oth_fi` | DOUBLE | - | `0.0` | 向其他金融机构拆入资金净增加额 |
| `prem_fr_orig_contr` | DOUBLE | - | `0.0` | 收到原保险合同保费取得的现金 |
| `n_incr_insured_dep` | DOUBLE | - | `0.0` | 保户储金净增加额 |
| `n_reinsur_prem` | DOUBLE | - | `0.0` | 收到再保业务现金净额 |
| `n_incr_disp_tfa` | DOUBLE | - | `0.0` | 处置交易性金融资产净增加额 |
| `ifc_cash_incr` | DOUBLE | - | `0.0` | 收取利息和手续费净增加额 |
| `n_incr_disp_faas` | DOUBLE | - | `0.0` | 处置可供出售金融资产净增加额 |
| `n_incr_loans_oth_bank` | DOUBLE | - | `0.0` | 拆入资金净增加额 |
| `n_cap_incr_repur` | DOUBLE | - | `0.0` | 回购业务资金净增加额 |
| `c_fr_oth_operate_a` | DOUBLE | - | `0.0` | 收到其他与经营活动有关的现金 |
| `c_inf_fr_operate_a` | DOUBLE | - | `0.0` | 经营活动现金流入小计 |
| `c_paid_goods_s` | DOUBLE | - | `0.0` | 购买商品、接受劳务支付的现金 |
| `c_paid_to_for_empl` | DOUBLE | - | `0.0` | 支付给职工以及为职工支付的现金 |
| `c_paid_for_taxes` | DOUBLE | - | `0.0` | 支付的各项税费 |
| `n_incr_clt_loan_adv` | DOUBLE | - | `0.0` | 客户贷款及垫款净增加额 |
| `n_incr_dep_cbob` | DOUBLE | - | `0.0` | 存放央行和同业款项净增加额 |
| `c_pay_claims_orig_inco` | DOUBLE | - | `0.0` | 支付原保险合同赔付款项的现金 |
| `pay_handling_chrg` | DOUBLE | - | `0.0` | 支付手续费的现金 |
| `pay_comm_insur_plcy` | DOUBLE | - | `0.0` | 支付保单红利的现金 |
| `oth_cash_pay_oper_act` | DOUBLE | - | `0.0` | 支付其他与经营活动有关的现金 |
| `st_cash_out_act` | DOUBLE | - | `0.0` | 经营活动现金流出小计 |
| `n_cashflow_act` | DOUBLE | - | `0.0` | 经营活动产生的现金流量净额 |
| `oth_recp_ral_inv_act` | DOUBLE | - | `0.0` | 收到其他与投资活动有关的现金 |
| `c_disp_withdrwl_invest` | DOUBLE | - | `0.0` | 收回投资收到的现金 |
| `c_recp_return_invest` | DOUBLE | - | `0.0` | 取得投资收益收到的现金 |
| `n_recp_disp_fiolta` | DOUBLE | - | `0.0` | 处置固定资产、无形资产和其他长期资产收回的现金净额 |
| `n_recp_disp_sobu` | DOUBLE | - | `0.0` | 处置子公司及其他营业单位收到的现金净额 |
| `stot_inflows_inv_act` | DOUBLE | - | `0.0` | 投资活动现金流入小计 |
| `c_pay_acq_const_fiolta` | DOUBLE | - | `0.0` | 购建固定资产、无形资产和其他长期资产支付的现金 |
| `c_paid_invest` | DOUBLE | - | `0.0` | 投资支付的现金 |
| `n_disp_subs_oth_biz` | DOUBLE | - | `0.0` | 取得子公司及其他营业单位支付的现金净额 |
| `oth_pay_ral_inv_act` | DOUBLE | - | `0.0` | 支付其他与投资活动有关的现金 |
| `n_incr_pledge_loan` | DOUBLE | - | `0.0` | 质押贷款净增加额 |
| `stot_out_inv_act` | DOUBLE | - | `0.0` | 投资活动现金流出小计 |
| `n_cashflow_inv_act` | DOUBLE | - | `0.0` | 投资活动产生的现金流量净额 |
| `c_recp_borrow` | DOUBLE | - | `0.0` | 取得借款收到的现金 |
| `proc_issue_bonds` | DOUBLE | - | `0.0` | 发行债券收到的现金 |
| `oth_cash_recp_ral_fnc_act` | DOUBLE | - | `0.0` | 收到其他与筹资活动有关的现金 |
| `stot_cash_in_fnc_act` | DOUBLE | - | `0.0` | 筹资活动现金流入小计 |
| `free_cashflow` | DOUBLE | - | `0.0` | 企业自由现金流量 |
| `c_prepay_amt_borr` | DOUBLE | - | `0.0` | 偿还债务支付的现金 |
| `c_pay_dist_dpcp_int_exp` | DOUBLE | - | `0.0` | 分配股利、利润或偿付利息支付的现金 |
| `incl_dvd_profit_paid_sc_ms` | DOUBLE | - | `0.0` | 其中:子公司支付给少数股东的股利、利润 |
| `oth_cashpay_ral_fnc_act` | DOUBLE | - | `0.0` | 支付其他与筹资活动有关的现金 |
| `stot_cashout_fnc_act` | DOUBLE | - | `0.0` | 筹资活动现金流出小计 |
| `n_cash_flows_fnc_act` | DOUBLE | - | `0.0` | 筹资活动产生的现金流量净额 |
| `eff_fx_flu_cash` | DOUBLE | - | `0.0` | 汇率变动对现金的影响 |
| `n_incr_cash_cash_equ` | DOUBLE | - | `0.0` | 现金及现金等价物净增加额 |
| `c_cash_equ_beg_period` | DOUBLE | - | `0.0` | 期初现金及现金等价物余额 |
| `c_cash_equ_end_period` | DOUBLE | - | `0.0` | 期末现金及现金等价物余额 |
| `c_recp_cap_contrib` | DOUBLE | - | `0.0` | 吸收投资收到的现金 |
| `incl_cash_rec_saims` | DOUBLE | - | `0.0` | 其中:子公司吸收少数股东投资收到的现金 |
| `uncon_invest_loss` | DOUBLE | - | `0.0` | 未确认投资损失 |
| `prov_depr_assets` | DOUBLE | - | `0.0` | 加:资产减值准备 |
| `depr_fa_coga_dpba` | DOUBLE | - | `0.0` | 固定资产折旧、油气资产折耗、生产性生物资产折旧 |
| `amort_intang_assets` | DOUBLE | - | `0.0` | 无形资产摊销 |
| `lt_amort_deferred_exp` | DOUBLE | - | `0.0` | 长期待摊费用摊销 |
| `decr_deferred_exp` | DOUBLE | - | `0.0` | 待摊费用减少 |
| `incr_acc_exp` | DOUBLE | - | `0.0` | 预提费用增加 |
| `loss_disp_fiolta` | DOUBLE | - | `0.0` | 处置固定、无形资产和其他长期资产的损失 |
| `loss_scr_fa` | DOUBLE | - | `0.0` | 固定资产报废损失 |
| `loss_fv_chg` | DOUBLE | - | `0.0` | 公允价值变动损失 |
| `invest_loss` | DOUBLE | - | `0.0` | 投资损失 |
| `decr_def_inc_tax_assets` | DOUBLE | - | `0.0` | 递延所得税资产减少 |
| `incr_def_inc_tax_liab` | DOUBLE | - | `0.0` | 递延所得税负债增加 |
| `decr_inventories` | DOUBLE | - | `0.0` | 存货的减少 |
| `decr_oper_payable` | DOUBLE | - | `0.0` | 经营性应收项目的减少 |
| `incr_oper_payable` | DOUBLE | - | `0.0` | 经营性应付项目的增加 |
| `others` | DOUBLE | - | `0.0` | 其他 |
| `im_net_cashflow_oper_act` | DOUBLE | - | `0.0` | 经营活动产生的现金流量净额(间接法) |
| `conv_debt_into_cap` | DOUBLE | - | `0.0` | 债务转为资本 |
| `conv_copbonds_due_within_1y` | DOUBLE | - | `0.0` | 一年内到期的可转换公司债券 |
| `fa_fnc_leases` | DOUBLE | - | `0.0` | 融资租入固定资产 |
| `im_n_incr_cash_equ` | DOUBLE | - | `0.0` | 现金及现金等价物净增加额(间接法) |
| `net_dism_capital_add` | DOUBLE | - | `0.0` | 拆出资金净增加额 |
| `net_cash_rece_sec` | DOUBLE | - | `0.0` | 代理买卖证券收到的现金净额(元) |
| `credit_impa_loss` | DOUBLE | - | `0.0` | 信用减值损失 |
| `use_right_asset_dep` | DOUBLE | - | `0.0` | 使用权资产折旧 |
| `oth_loss_asset` | DOUBLE | - | `0.0` | 其他资产减值损失 |
| `end_bal_cash` | DOUBLE | - | `0.0` | 现金的期末余额 |
| `beg_bal_cash` | DOUBLE | - | `0.0` | 减:现金的期初余额 |
| `end_bal_cash_equ` | DOUBLE | - | `0.0` | 加:现金等价物的期末余额 |
| `beg_bal_cash_equ` | DOUBLE | - | `0.0` | 减:现金等价物的期初余额 |
| `update_flag` | INTEGER | - | `0` | 更新标志 |

---

### forecast

**表名**: `forecast` | **说明**: 业绩预告 | **主键**: `ts_code`, `ann_date`, `end_date` | **依赖表**: `stock/basic/stock_basic`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | TS股票代码 |
| `ann_date` | DATE | - | `1970-01-01` | 公告日期 |
| `end_date` | DATE | - | `1970-01-01` | 报告期 |
| `type` | VARCHAR(255) | 255 | `` | 业绩预告类型 |
| `p_change_min` | DOUBLE | - | `0.0` | 预告净利润变动幅度下限（%） |
| `p_change_max` | DOUBLE | - | `0.0` | 预告净利润变动幅度上限（%） |
| `net_profit_min` | DOUBLE | - | `0.0` | 预告净利润下限（万元） |
| `net_profit_max` | DOUBLE | - | `0.0` | 预告净利润上限（万元） |
| `last_parent_net` | DOUBLE | - | `0.0` | 上年同期归属母公司净利润 |
| `notice_times` | INTEGER | - | `0` | 公布次数 |
| `first_ann_date` | DATE | - | `1970-01-01` | 首次公告日 |
| `summary` | VARCHAR(255) | 255 | `` | 业绩预告摘要 |
| `change_reason` | VARCHAR(255) | 255 | `` | 业绩变动原因 |
| `update_flag` | VARCHAR(255) | 255 | `` | 更新标志 |

---

### express

**表名**: `express` | **说明**: 业绩快报 | **主键**: `ts_code`, `ann_date`, `end_date` | **依赖表**: `stock/basic/stock_basic`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | TS股票代码 |
| `ann_date` | DATE | - | `1970-01-01` | 公告日期 |
| `end_date` | DATE | - | `1970-01-01` | 报告期 |
| `revenue` | DOUBLE | - | `0.0` | 营业收入(元) |
| `operate_profit` | DOUBLE | - | `0.0` | 营业利润(元) |
| `total_profit` | DOUBLE | - | `0.0` | 利润总额(元) |
| `n_income` | DOUBLE | - | `0.0` | 净利润(元) |
| `total_assets` | DOUBLE | - | `0.0` | 总资产(元) |
| `total_hldr_eqy_exc_min_int` | DOUBLE | - | `0.0` | 股东权益合计(不含少数股东权益)(元) |
| `diluted_eps` | DOUBLE | - | `0.0` | 每股收益(摊薄)(元) |
| `diluted_roe` | DOUBLE | - | `0.0` | 净资产收益率(摊薄)(%) |
| `yoy_net_profit` | DOUBLE | - | `0.0` | 去年同期修正后净利润 |
| `bps` | DOUBLE | - | `0.0` | 每股净资产 |
| `yoy_sales` | DOUBLE | - | `0.0` | 同比增长率:营业收入 |
| `yoy_op` | DOUBLE | - | `0.0` | 同比增长率:营业利润 |
| `yoy_tp` | DOUBLE | - | `0.0` | 同比增长率:利润总额 |
| `yoy_dedu_np` | DOUBLE | - | `0.0` | 同比增长率:归属母公司股东的净利润 |
| `yoy_eps` | DOUBLE | - | `0.0` | 同比增长率:基本每股收益 |
| `yoy_roe` | DOUBLE | - | `0.0` | 同比增减:加权平均净资产收益率 |
| `growth_assets` | DOUBLE | - | `0.0` | 比年初增长率:总资产 |
| `yoy_equity` | DOUBLE | - | `0.0` | 比年初增长率:归属母公司的股东权益 |
| `growth_bps` | DOUBLE | - | `0.0` | 比年初增长率:归属于母公司股东的每股净资产 |
| `or_last_year` | DOUBLE | - | `0.0` | 去年同期营业收入 |
| `op_last_year` | DOUBLE | - | `0.0` | 去年同期营业利润 |
| `tp_last_year` | DOUBLE | - | `0.0` | 去年同期利润总额 |
| `np_last_year` | DOUBLE | - | `0.0` | 去年同期净利润 |
| `eps_last_year` | DOUBLE | - | `0.0` | 去年同期每股收益 |
| `open_net_assets` | DOUBLE | - | `0.0` | 期初净资产 |
| `open_bps` | DOUBLE | - | `0.0` | 期初每股净资产 |
| `perf_summary` | VARCHAR(255) | 255 | `` | 业绩简要说明 |
| `is_audit` | INTEGER | - | `0` | 是否审计： 1是 0否 |
| `remark` | VARCHAR(255) | 255 | `` | 备注 |
| `update_flag` | VARCHAR(255) | 255 | `` | 更新标志 |

---

### fina_indicator

**表名**: `fina_indicator` | **说明**: 财务指标数据 | **主键**: `ts_code`, `ann_date`, `end_date`, `update_flag` | **依赖表**: `stock/basic/stock_basic`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | TS代码 |
| `ann_date` | DATE | - | `1970-01-01` | 公告日期 |
| `end_date` | DATE | - | `1970-01-01` | 报告期 |
| `eps` | DOUBLE | - | `0.0` | 基本每股收益 |
| `dt_eps` | DOUBLE | - | `0.0` | 稀释每股收益 |
| `total_revenue_ps` | DOUBLE | - | `0.0` | 每股营业总收入 |
| `revenue_ps` | DOUBLE | - | `0.0` | 每股营业收入 |
| `capital_rese_ps` | DOUBLE | - | `0.0` | 每股资本公积 |
| `surplus_rese_ps` | DOUBLE | - | `0.0` | 每股盈余公积 |
| `undist_profit_ps` | DOUBLE | - | `0.0` | 每股未分配利润 |
| `extra_item` | DOUBLE | - | `0.0` | 非经常性损益 |
| `profit_dedt` | DOUBLE | - | `0.0` | 扣除非经常性损益后的净利润 |
| `gross_margin` | DOUBLE | - | `0.0` | 毛利 |
| `current_ratio` | DOUBLE | - | `0.0` | 流动比率 |
| `quick_ratio` | DOUBLE | - | `0.0` | 速动比率 |
| `cash_ratio` | DOUBLE | - | `0.0` | 保守速动比率 |
| `invturn_days` | DOUBLE | - | `0.0` | 存货周转天数 |
| `arturn_days` | DOUBLE | - | `0.0` | 应收账款周转天数 |
| `inv_turn` | DOUBLE | - | `0.0` | 存货周转率 |
| `ar_turn` | DOUBLE | - | `0.0` | 应收账款周转率 |
| `ca_turn` | DOUBLE | - | `0.0` | 流动资产周转率 |
| `fa_turn` | DOUBLE | - | `0.0` | 固定资产周转率 |
| `assets_turn` | DOUBLE | - | `0.0` | 总资产周转率 |
| `op_income` | DOUBLE | - | `0.0` | 经营活动净收益 |
| `valuechange_income` | DOUBLE | - | `0.0` | 价值变动净收益 |
| `interst_income` | DOUBLE | - | `0.0` | 利息费用 |
| `daa` | DOUBLE | - | `0.0` | 折旧与摊销 |
| `ebit` | DOUBLE | - | `0.0` | 息税前利润 |
| `ebitda` | DOUBLE | - | `0.0` | 息税折旧摊销前利润 |
| `fcff` | DOUBLE | - | `0.0` | 企业自由现金流量 |
| `fcfe` | DOUBLE | - | `0.0` | 股权自由现金流量 |
| `current_exint` | DOUBLE | - | `0.0` | 无息流动负债 |
| `noncurrent_exint` | DOUBLE | - | `0.0` | 无息非流动负债 |
| `interestdebt` | DOUBLE | - | `0.0` | 带息债务 |
| `netdebt` | DOUBLE | - | `0.0` | 净债务 |
| `tangible_asset` | DOUBLE | - | `0.0` | 有形资产 |
| `working_capital` | DOUBLE | - | `0.0` | 营运资金 |
| `networking_capital` | DOUBLE | - | `0.0` | 营运流动资本 |
| `invest_capital` | DOUBLE | - | `0.0` | 全部投入资本 |
| `retained_earnings` | DOUBLE | - | `0.0` | 留存收益 |
| `diluted2_eps` | DOUBLE | - | `0.0` | 期末摊薄每股收益 |
| `bps` | DOUBLE | - | `0.0` | 每股净资产 |
| `ocfps` | DOUBLE | - | `0.0` | 每股经营活动产生的现金流量净额 |
| `retainedps` | DOUBLE | - | `0.0` | 每股留存收益 |
| `cfps` | DOUBLE | - | `0.0` | 每股现金流量净额 |
| `ebit_ps` | DOUBLE | - | `0.0` | 每股息税前利润 |
| `fcff_ps` | DOUBLE | - | `0.0` | 每股企业自由现金流量 |
| `fcfe_ps` | DOUBLE | - | `0.0` | 每股股东自由现金流量 |
| `netprofit_margin` | DOUBLE | - | `0.0` | 销售净利率 |
| `grossprofit_margin` | DOUBLE | - | `0.0` | 销售毛利率 |
| `cogs_of_sales` | DOUBLE | - | `0.0` | 销售成本率 |
| `expense_of_sales` | DOUBLE | - | `0.0` | 销售期间费用率 |
| `profit_to_gr` | DOUBLE | - | `0.0` | 净利润/营业总收入 |
| `saleexp_to_gr` | DOUBLE | - | `0.0` | 销售费用/营业总收入 |
| `adminexp_of_gr` | DOUBLE | - | `0.0` | 管理费用/营业总收入 |
| `finaexp_of_gr` | DOUBLE | - | `0.0` | 财务费用/营业总收入 |
| `impai_ttm` | DOUBLE | - | `0.0` | 资产减值损失/营业总收入 |
| `gc_of_gr` | DOUBLE | - | `0.0` | 营业总成本/营业总收入 |
| `op_of_gr` | DOUBLE | - | `0.0` | 营业利润/营业总收入 |
| `ebit_of_gr` | DOUBLE | - | `0.0` | 息税前利润/营业总收入 |
| `roe` | DOUBLE | - | `0.0` | 净资产收益率 |
| `roe_waa` | DOUBLE | - | `0.0` | 加权平均净资产收益率 |
| `roe_dt` | DOUBLE | - | `0.0` | 净资产收益率(扣除非经常损益) |
| `roa` | DOUBLE | - | `0.0` | 总资产报酬率 |
| `npta` | DOUBLE | - | `0.0` | 总资产净利润 |
| `roic` | DOUBLE | - | `0.0` | 投入资本回报率 |
| `roe_yearly` | DOUBLE | - | `0.0` | 年化净资产收益率 |
| `roa2_yearly` | DOUBLE | - | `0.0` | 年化总资产报酬率 |
| `roe_avg` | DOUBLE | - | `0.0` | 平均净资产收益率(增发条件) |
| `opincome_of_ebt` | DOUBLE | - | `0.0` | 经营活动净收益/利润总额 |
| `investincome_of_ebt` | DOUBLE | - | `0.0` | 价值变动净收益/利润总额 |
| `n_op_profit_of_ebt` | DOUBLE | - | `0.0` | 营业外收支净额/利润总额 |
| `tax_to_ebt` | DOUBLE | - | `0.0` | 所得税/利润总额 |
| `dtprofit_to_profit` | DOUBLE | - | `0.0` | 扣除非经常损益后的净利润/净利润 |
| `salescash_to_or` | DOUBLE | - | `0.0` | 销售商品提供劳务收到的现金/营业收入 |
| `ocf_to_or` | DOUBLE | - | `0.0` | 经营活动产生的现金流量净额/营业收入 |
| `ocf_to_opincome` | DOUBLE | - | `0.0` | 经营活动产生的现金流量净额/经营活动净收益 |
| `capitalized_to_da` | DOUBLE | - | `0.0` | 资本支出/折旧和摊销 |
| `debt_to_assets` | DOUBLE | - | `0.0` | 资产负债率 |
| `assets_to_eqt` | DOUBLE | - | `0.0` | 权益乘数 |
| `dp_assets_to_eqt` | DOUBLE | - | `0.0` | 权益乘数(杜邦分析) |
| `ca_to_assets` | DOUBLE | - | `0.0` | 流动资产/总资产 |
| `nca_to_assets` | DOUBLE | - | `0.0` | 非流动资产/总资产 |
| `tbassets_to_totalassets` | DOUBLE | - | `0.0` | 有形资产/总资产 |
| `int_to_talcap` | DOUBLE | - | `0.0` | 带息债务/全部投入资本 |
| `eqt_to_talcapital` | DOUBLE | - | `0.0` | 归属于母公司的股东权益/全部投入资本 |
| `currentdebt_to_debt` | DOUBLE | - | `0.0` | 流动负债/负债合计 |
| `longdeb_to_debt` | DOUBLE | - | `0.0` | 非流动负债/负债合计 |
| `ocf_to_shortdebt` | DOUBLE | - | `0.0` | 经营活动产生的现金流量净额/流动负债 |
| `debt_to_eqt` | DOUBLE | - | `0.0` | 产权比率 |
| `eqt_to_debt` | DOUBLE | - | `0.0` | 归属于母公司的股东权益/负债合计 |
| `eqt_to_interestdebt` | DOUBLE | - | `0.0` | 归属于母公司的股东权益/带息债务 |
| `tangibleasset_to_debt` | DOUBLE | - | `0.0` | 有形资产/负债合计 |
| `tangasset_to_intdebt` | DOUBLE | - | `0.0` | 有形资产/带息债务 |
| `tangibleasset_to_netdebt` | DOUBLE | - | `0.0` | 有形资产/净债务 |
| `ocf_to_debt` | DOUBLE | - | `0.0` | 经营活动产生的现金流量净额/负债合计 |
| `ocf_to_interestdebt` | DOUBLE | - | `0.0` | 经营活动产生的现金流量净额/带息债务 |
| `ocf_to_netdebt` | DOUBLE | - | `0.0` | 经营活动产生的现金流量净额/净债务 |
| `ebit_to_interest` | DOUBLE | - | `0.0` | 已获利息倍数(EBIT/利息费用) |
| `longdebt_to_workingcapital` | DOUBLE | - | `0.0` | 长期债务与营运资金比率 |
| `ebitda_to_debt` | DOUBLE | - | `0.0` | 息税折旧摊销前利润/负债合计 |
| `turn_days` | DOUBLE | - | `0.0` | 营业周期 |
| `roa_yearly` | DOUBLE | - | `0.0` | 年化总资产净利率 |
| `roa_dp` | DOUBLE | - | `0.0` | 总资产净利率(杜邦分析) |
| `fixed_assets` | DOUBLE | - | `0.0` | 固定资产合计 |
| `profit_prefin_exp` | DOUBLE | - | `0.0` | 扣除财务费用前营业利润 |
| `non_op_profit` | DOUBLE | - | `0.0` | 非营业利润 |
| `op_to_ebt` | DOUBLE | - | `0.0` | 营业利润／利润总额 |
| `nop_to_ebt` | DOUBLE | - | `0.0` | 非营业利润／利润总额 |
| `ocf_to_profit` | DOUBLE | - | `0.0` | 经营活动产生的现金流量净额／营业利润 |
| `cash_to_liqdebt` | DOUBLE | - | `0.0` | 货币资金／流动负债 |
| `cash_to_liqdebt_withinterest` | DOUBLE | - | `0.0` | 货币资金／带息流动负债 |
| `op_to_liqdebt` | DOUBLE | - | `0.0` | 营业利润／流动负债 |
| `op_to_debt` | DOUBLE | - | `0.0` | 营业利润／负债合计 |
| `roic_yearly` | DOUBLE | - | `0.0` | 年化投入资本回报率 |
| `total_fa_trun` | DOUBLE | - | `0.0` | 固定资产合计周转率 |
| `profit_to_op` | DOUBLE | - | `0.0` | 利润总额／营业收入 |
| `q_opincome` | DOUBLE | - | `0.0` | 经营活动单季度净收益 |
| `q_investincome` | DOUBLE | - | `0.0` | 价值变动单季度净收益 |
| `q_dtprofit` | DOUBLE | - | `0.0` | 扣除非经常损益后的单季度净利润 |
| `q_eps` | DOUBLE | - | `0.0` | 每股收益(单季度) |
| `q_netprofit_margin` | DOUBLE | - | `0.0` | 销售净利率(单季度) |
| `q_gsprofit_margin` | DOUBLE | - | `0.0` | 销售毛利率(单季度) |
| `q_exp_to_sales` | DOUBLE | - | `0.0` | 销售期间费用率(单季度) |
| `q_profit_to_gr` | DOUBLE | - | `0.0` | 净利润／营业总收入(单季度) |
| `q_saleexp_to_gr` | DOUBLE | - | `0.0` | 销售费用／营业总收入 (单季度) |
| `q_adminexp_to_gr` | DOUBLE | - | `0.0` | 管理费用／营业总收入 (单季度) |
| `q_finaexp_to_gr` | DOUBLE | - | `0.0` | 财务费用／营业总收入 (单季度) |
| `q_impair_to_gr_ttm` | DOUBLE | - | `0.0` | 资产减值损失／营业总收入(单季度) |
| `q_gc_to_gr` | DOUBLE | - | `0.0` | 营业总成本／营业总收入 (单季度) |
| `q_op_to_gr` | DOUBLE | - | `0.0` | 营业利润／营业总收入(单季度) |
| `q_roe` | DOUBLE | - | `0.0` | 净资产收益率(单季度) |
| `q_dt_roe` | DOUBLE | - | `0.0` | 净资产单季度收益率(扣除非经常损益) |
| `q_npta` | DOUBLE | - | `0.0` | 总资产净利润(单季度) |
| `q_opincome_to_ebt` | DOUBLE | - | `0.0` | 经营活动净收益／利润总额(单季度) |
| `q_investincome_to_ebt` | DOUBLE | - | `0.0` | 价值变动净收益／利润总额(单季度) |
| `q_dtprofit_to_profit` | DOUBLE | - | `0.0` | 扣除非经常损益后的净利润／净利润(单季度) |
| `q_salescash_to_or` | DOUBLE | - | `0.0` | 销售商品提供劳务收到的现金／营业收入(单季度) |
| `q_ocf_to_sales` | DOUBLE | - | `0.0` | 经营活动产生的现金流量净额／营业收入(单季度) |
| `q_ocf_to_or` | DOUBLE | - | `0.0` | 经营活动产生的现金流量净额／经营活动净收益(单季度) |
| `basic_eps_yoy` | DOUBLE | - | `0.0` | 基本每股收益同比增长率(%) |
| `dt_eps_yoy` | DOUBLE | - | `0.0` | 稀释每股收益同比增长率(%) |
| `cfps_yoy` | DOUBLE | - | `0.0` | 每股经营活动产生的现金流量净额同比增长率(%) |
| `op_yoy` | DOUBLE | - | `0.0` | 营业利润同比增长率(%) |
| `ebt_yoy` | DOUBLE | - | `0.0` | 利润总额同比增长率(%) |
| `netprofit_yoy` | DOUBLE | - | `0.0` | 归属母公司股东的净利润同比增长率(%) |
| `dt_netprofit_yoy` | DOUBLE | - | `0.0` | 归属母公司股东的净利润-扣除非经常损益同比增长率(%) |
| `ocf_yoy` | DOUBLE | - | `0.0` | 经营活动产生的现金流量净额同比增长率(%) |
| `roe_yoy` | DOUBLE | - | `0.0` | 净资产收益率(摊薄)同比增长率(%) |
| `bps_yoy` | DOUBLE | - | `0.0` | 每股净资产相对年初增长率(%) |
| `assets_yoy` | DOUBLE | - | `0.0` | 资产总计相对年初增长率(%) |
| `eqt_yoy` | DOUBLE | - | `0.0` | 归属母公司的股东权益相对年初增长率(%) |
| `tr_yoy` | DOUBLE | - | `0.0` | 营业总收入同比增长率(%) |
| `or_yoy` | DOUBLE | - | `0.0` | 营业收入同比增长率(%) |
| `q_gr_yoy` | DOUBLE | - | `0.0` | 营业总收入同比增长率(%)(单季度) |
| `q_gr_qoq` | DOUBLE | - | `0.0` | 营业总收入环比增长率(%)(单季度) |
| `q_sales_yoy` | DOUBLE | - | `0.0` | 营业收入同比增长率(%)(单季度) |
| `q_sales_qoq` | DOUBLE | - | `0.0` | 营业收入环比增长率(%)(单季度) |
| `q_op_yoy` | DOUBLE | - | `0.0` | 营业利润同比增长率(%)(单季度) |
| `q_op_qoq` | DOUBLE | - | `0.0` | 营业利润环比增长率(%)(单季度) |
| `q_profit_yoy` | DOUBLE | - | `0.0` | 净利润同比增长率(%)(单季度) |
| `q_profit_qoq` | DOUBLE | - | `0.0` | 净利润环比增长率(%)(单季度) |
| `q_netprofit_yoy` | DOUBLE | - | `0.0` | 归属母公司股东的净利润同比增长率(%)(单季度) |
| `q_netprofit_qoq` | DOUBLE | - | `0.0` | 归属母公司股东的净利润环比增长率(%)(单季度) |
| `equity_yoy` | DOUBLE | - | `0.0` | 净资产同比增长率 |
| `rd_exp` | DOUBLE | - | `0.0` | 研发费用 |
| `update_flag` | VARCHAR(255) | 255 | `` | 更新标识 |

---

### fina_audit

**表名**: `fina_audit` | **说明**: 财务审计意见 | **主键**: `ts_code`, `end_date`, `ann_date` | **依赖表**: `stock/basic/stock_basic`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | TS股票代码 |
| `ann_date` | DATE | - | `1970-01-01` | 公告日期 |
| `end_date` | DATE | - | `1970-01-01` | 报告期 |
| `audit_result` | VARCHAR(255) | 255 | `` | 审计结果 |
| `audit_fees` | DOUBLE | - | `0.0` | 审计总费用（元） |
| `audit_agency` | VARCHAR(255) | 255 | `` | 会计事务所 |
| `audit_sign` | VARCHAR(255) | 255 | `` | 签字会计师 |

---

### fina_mainbz

**表名**: `fina_mainbz` | **说明**: 主营业务构成 | **主键**: `ts_code`, `end_date`, `update_flag` | **依赖表**: `stock/basic/stock_basic`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | TS代码 |
| `end_date` | DATE | - | `1970-01-01` | 报告期 |
| `bz_item` | VARCHAR(255) | 255 | `` | 主营业务项目 |
| `bz_code` | VARCHAR(255) | 255 | `` | 项目代码 |
| `bz_sales` | DOUBLE | - | `0.0` | 主营业务收入(元) |
| `bz_profit` | DOUBLE | - | `0.0` | 主营业务利润(元) |
| `bz_cost` | DOUBLE | - | `0.0` | 主营业务成本(元) |
| `curr_type` | VARCHAR(255) | 255 | `` | 货币代码 |
| `update_flag` | VARCHAR(255) | 255 | `` | 是否更新 |

---

### dividend

**表名**: `dividend` | **说明**: 分红送股 | **主键**: `ts_code`, `end_date`, `ann_date`, `div_proc`, `update_flag` | **依赖表**: `stock/basic/stock_basic`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | TS代码 |
| `end_date` | DATE | - | `1970-01-01` | 分送年度 |
| `ann_date` | DATE | - | `1970-01-01` | 预案公告日（董事会） |
| `div_proc` | VARCHAR(255) | 255 | `` | 实施进度 |
| `stk_div` | DOUBLE | - | `0.0` | 每股送转 |
| `stk_bo_rate` | DOUBLE | - | `0.0` | 每股送股比例 |
| `stk_co_rate` | DOUBLE | - | `0.0` | 每股转增比例 |
| `cash_div` | DOUBLE | - | `0.0` | 每股分红（税后） |
| `cash_div_tax` | DOUBLE | - | `0.0` | 每股分红（税前） |
| `record_date` | DATE | - | `1970-01-01` | 股权登记日 |
| `ex_date` | DATE | - | `1970-01-01` | 除权除息日 |
| `pay_date` | DATE | - | `1970-01-01` | 派息日 |
| `div_listdate` | DATE | - | `1970-01-01` | 红股上市日 |
| `imp_ann_date` | DATE | - | `1970-01-01` | 实施公告日 |
| `base_date` | DATE | - | `1970-01-01` | 基准日 |
| `base_share` | DOUBLE | - | `0.0` | 实施基准股本（万） |
| `update_flag` | VARCHAR(255) | 255 | `` | 是否变更过（1表示变更） |

---

### disclosure_date

**表名**: `disclosure_date` | **说明**: 财报披露计划 | **主键**: `ts_code`, `end_date` | **依赖表**: `stock/basic/stock_basic`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | TS代码 |
| `ann_date` | DATE | - | `1970-01-01` | 最新披露公告日 |
| `end_date` | DATE | - | `1970-01-01` | 报告期 |
| `pre_date` | DATE | - | `1970-01-01` | 预计披露日期 |
| `actual_date` | DATE | - | `1970-01-01` | 实际披露日期 |
| `modify_date` | DATE | - | `1970-01-01` | 披露日期修正记录 |

---

## 股票-行情数据 {#股票-行情数据}

本分类共包含 **13** 个数据表。

### 表列表

- [stk_mins](#stk-mins) - 分钟线行情
- [adj_factor](#adj-factor) - 复权因子
- [daily](#daily) - 日线行情
- [daily_basic](#daily-basic) - 每日指标
- [hsgt_top10](#hsgt-top10) - 沪深股通十大成交股
- [ggt_top10](#ggt-top10) - 港股通十大成交股
- [weekly](#weekly) - 周线行情
- [monthly](#monthly) - 月线行情
- [stk_limit](#stk-limit) - 每日涨跌停价格
- [ggt_daily](#ggt-daily) - 港股通每日成交统计
- [suspend_d](#suspend-d) - 每日停复牌信息
- [bak_daily](#bak-daily) - 备用行情
- [stk_weekly_monthly](#stk-weekly-monthly) - 股票周/月线行情(每日更新)

### stk_mins

**表名**: `stk_mins` | **说明**: 分钟线行情 | **主键**: `ts_code`, `trade_time` | **依赖表**: `stock/basic/stock_basic`, `stock/basic/trade_cal`, `stock/quotes/daily`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | 股票代码 |
| `trade_time` | DATETIME | - | `1970-01-01 00:00:00` | 交易时间 |
| `open` | DOUBLE | - | `0.0` | 开盘价 |
| `high` | DOUBLE | - | `0.0` | 最高价 |
| `low` | DOUBLE | - | `0.0` | 最低价 |
| `close` | DOUBLE | - | `0.0` | 收盘价 |
| `vol` | DOUBLE | - | `0.0` | 成交量 |
| `amount` | DOUBLE | - | `0.0` | 成交额 |

---

### adj_factor

**表名**: `adj_factor` | **说明**: 复权因子 | **主键**: `ts_code`, `trade_date` | **依赖表**: `stock/basic/trade_cal`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | 股票代码 |
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `adj_factor` | NUMBER | - | `0.0` | 复权因子 |

---

### daily

**表名**: `daily` | **说明**: 日线行情 | **主键**: `ts_code`, `trade_date` | **依赖表**: `stock/basic/stock_basic`, `stock/basic/trade_cal`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | 股票代码 |
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `open` | DOUBLE | - | `0.0` | 开盘价 |
| `high` | DOUBLE | - | `0.0` | 最高价 |
| `low` | DOUBLE | - | `0.0` | 最低价 |
| `close` | DOUBLE | - | `0.0` | 收盘价 |
| `pre_close` | DOUBLE | - | `0.0` | 昨收价 |
| `change` | DOUBLE | - | `0.0` | 涨跌额 |
| `pct_chg` | DOUBLE | - | `0.0` | 涨跌幅 |
| `vol` | DOUBLE | - | `0.0` | 成交量 |
| `amount` | DOUBLE | - | `0.0` | 成交额 |

---

### daily_basic

**表名**: `daily_basic` | **说明**: 每日指标 | **主键**: `ts_code`, `trade_date` | **依赖表**: `stock/basic/stock_basic`, `stock/quotes/daily`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | TS股票代码 |
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `close` | NUMBER | - | `0.0` | 当日收盘价 |
| `turnover_rate` | NUMBER | - | `0.0` | 换手率 |
| `turnover_rate_f` | NUMBER | - | `0.0` | 换手率(自由流通股) |
| `volume_ratio` | NUMBER | - | `0.0` | 量比 |
| `pe` | NUMBER | - | `0.0` | 市盈率（总市值/净利润） |
| `pe_ttm` | NUMBER | - | `0.0` | 市盈率（TTM） |
| `pb` | NUMBER | - | `0.0` | 市净率（总市值/净资产） |
| `ps` | NUMBER | - | `0.0` | 市销率 |
| `ps_ttm` | NUMBER | - | `0.0` | 市销率（TTM） |
| `dv_ratio` | NUMBER | - | `0.0` | 股息率（%） |
| `dv_ttm` | NUMBER | - | `0.0` | 股息率（TTM） （%） |
| `total_share` | NUMBER | - | `0.0` | 总股本 |
| `float_share` | NUMBER | - | `0.0` | 流通股本 |
| `free_share` | NUMBER | - | `0.0` | 自由流通股本 |
| `total_mv` | NUMBER | - | `0.0` | 总市值 |
| `circ_mv` | NUMBER | - | `0.0` | 流通市值 |
| `limit_status` | INTEGER | - | `0` | 涨跌停状态 |

---

### hsgt_top10

**表名**: `hsgt_top10` | **说明**: 沪深股通十大成交股 | **主键**: `ts_code`, `trade_date` | **依赖表**: `stock/basic/trade_cal`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `ts_code` | VARCHAR(16) | 16 | `` | 股票代码 |
| `name` | VARCHAR(255) | 255 | `` | 股票名称 |
| `close` | DOUBLE | - | `0.0` | 收盘价 |
| `change` | DOUBLE | - | `0.0` | 涨跌幅 |
| `rank` | INTEGER | - | `0` | 资金排名 |
| `market_type` | VARCHAR(255) | 255 | `` | 市场类型（1：沪市 3：深市） |
| `amount` | DOUBLE | - | `0.0` | 成交金额 |
| `net_amount` | DOUBLE | - | `0.0` | 净成交金额 |
| `buy` | DOUBLE | - | `0.0` | 买入金额 |
| `sell` | DOUBLE | - | `0.0` | 卖出金额 |

---

### ggt_top10

**表名**: `ggt_top10` | **说明**: 港股通十大成交股 | **主键**: `ts_code`, `trade_date` | **依赖表**: `stock/basic/trade_cal`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `ts_code` | VARCHAR(16) | 16 | `` | 股票代码 |
| `name` | VARCHAR(255) | 255 | `` | 股票名称 |
| `close` | DOUBLE | - | `0.0` | 收盘价 |
| `p_change` | DOUBLE | - | `0.0` | 涨跌幅 |
| `rank` | VARCHAR(255) | 255 | `` | 资金排名 |
| `market_type` | VARCHAR(255) | 255 | `` | 市场类型 2：港股通（沪） 4：港股通（深） |
| `amount` | DOUBLE | - | `0.0` | 累计成交金额 |
| `net_amount` | DOUBLE | - | `0.0` | 净买入金额 |
| `sh_amount` | DOUBLE | - | `0.0` | 沪市成交金额 |
| `sh_net_amount` | DOUBLE | - | `0.0` | 沪市净买入金额 |
| `sh_buy` | DOUBLE | - | `0.0` | 沪市买入金额 |
| `sh_sell` | DOUBLE | - | `0.0` | 沪市卖出金额 |
| `sz_amount` | DOUBLE | - | `0.0` | 深市成交金额 |
| `sz_net_amount` | DOUBLE | - | `0.0` | 深市净买入金额 |
| `sz_buy` | DOUBLE | - | `0.0` | 深市买入金额 |
| `sz_sell` | DOUBLE | - | `0.0` | 深市卖出金额 |

---

### weekly

**表名**: `weekly` | **说明**: 周线行情 | **主键**: `ts_code`, `trade_date` | **依赖表**: `stock/basic/stock_basic`, `stock/basic/trade_cal`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | 无说明 |
| `trade_date` | DATE | - | `1970-01-01` | 无说明 |
| `close` | DOUBLE | - | `0.0` | 无说明 |
| `open` | DOUBLE | - | `0.0` | 无说明 |
| `high` | DOUBLE | - | `0.0` | 无说明 |
| `low` | DOUBLE | - | `0.0` | 无说明 |
| `pre_close` | DOUBLE | - | `0.0` | 无说明 |
| `change` | DOUBLE | - | `0.0` | 无说明 |
| `pct_chg` | DOUBLE | - | `0.0` | 无说明 |
| `vol` | DOUBLE | - | `0.0` | 无说明 |
| `amount` | DOUBLE | - | `0.0` | 无说明 |

---

### monthly

**表名**: `monthly` | **说明**: 月线行情 | **主键**: `ts_code`, `trade_date` | **依赖表**: `stock/basic/stock_basic`, `stock/basic/trade_cal`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | 无说明 |
| `trade_date` | DATE | - | `1970-01-01` | 无说明 |
| `close` | DOUBLE | - | `0.0` | 无说明 |
| `open` | DOUBLE | - | `0.0` | 无说明 |
| `high` | DOUBLE | - | `0.0` | 无说明 |
| `low` | DOUBLE | - | `0.0` | 无说明 |
| `pre_close` | DOUBLE | - | `0.0` | 无说明 |
| `change` | DOUBLE | - | `0.0` | 无说明 |
| `pct_chg` | DOUBLE | - | `0.0` | 无说明 |
| `vol` | DOUBLE | - | `0.0` | 无说明 |
| `amount` | DOUBLE | - | `0.0` | 无说明 |

---

### stk_limit

**表名**: `stk_limit` | **说明**: 每日涨跌停价格 | **主键**: `ts_code`, `trade_date` | **依赖表**: `stock/basic/stock_basic`, `stock/basic/trade_cal`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `ts_code` | VARCHAR(16) | 16 | `` | TS股票代码 |
| `pre_close` | DOUBLE | - | `0.0` | 昨日收盘价 |
| `up_limit` | DOUBLE | - | `0.0` | 涨停价 |
| `down_limit` | DOUBLE | - | `0.0` | 跌停价 |

---

### ggt_daily

**表名**: `ggt_daily` | **说明**: 港股通每日成交统计 | **主键**: `trade_date` | **依赖表**: `stock/quotes/daily`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `buy_amount` | DOUBLE | - | `0.0` | 买入成交金额（亿元） |
| `buy_volume` | DOUBLE | - | `0.0` | 买入成交笔数（万笔） |
| `sell_amount` | DOUBLE | - | `0.0` | 卖出成交金额（亿元） |
| `sell_volume` | DOUBLE | - | `0.0` | 卖出成交笔数（万笔） |

---

### suspend_d

**表名**: `suspend_d` | **说明**: 每日停复牌信息 | **主键**: `ts_code`, `trade_date` | **依赖表**: `stock/basic/stock_basic`, `stock/quotes/daily`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | TS代码 |
| `trade_date` | DATE | - | `1970-01-01` | 停复牌日期 |
| `suspend_timing` | VARCHAR(255) | 255 | `` | 日内停牌时间段 |
| `suspend_type` | VARCHAR(255) | 255 | `` | 停复牌类型：S-停牌，R-复牌 |

---

### bak_daily

**表名**: `bak_daily` | **说明**: 备用行情 | **主键**: `ts_code`, `trade_date` | **依赖表**: `stock/basic/stock_basic`, `stock/basic/trade_cal`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | 股票代码 |
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `name` | VARCHAR(255) | 255 | `` | 股票名称 |
| `pct_change` | DOUBLE | - | `0.0` | 涨跌幅 |
| `close` | DOUBLE | - | `0.0` | 收盘价 |
| `change` | DOUBLE | - | `0.0` | 涨跌额 |
| `open` | DOUBLE | - | `0.0` | 开盘价 |
| `high` | DOUBLE | - | `0.0` | 最高价 |
| `low` | DOUBLE | - | `0.0` | 最低价 |
| `pre_close` | DOUBLE | - | `0.0` | 昨收价 |
| `vol_ratio` | DOUBLE | - | `0.0` | 量比 |
| `turn_over` | DOUBLE | - | `0.0` | 换手率 |
| `swing` | DOUBLE | - | `0.0` | 振幅 |
| `vol` | DOUBLE | - | `0.0` | 成交量 |
| `amount` | DOUBLE | - | `0.0` | 成交额 |
| `selling` | DOUBLE | - | `0.0` | 外盘 |
| `buying` | DOUBLE | - | `0.0` | 内盘 |
| `total_share` | DOUBLE | - | `0.0` | 总股本(万) |
| `float_share` | DOUBLE | - | `0.0` | 流通股本(万) |
| `pe` | DOUBLE | - | `0.0` | 市盈(动) |
| `industry` | VARCHAR(255) | 255 | `` | 所属行业 |
| `area` | VARCHAR(255) | 255 | `` | 所属地域 |
| `float_mv` | DOUBLE | - | `0.0` | 流通市值 |
| `total_mv` | DOUBLE | - | `0.0` | 总市值 |
| `avg_price` | DOUBLE | - | `0.0` | 平均价 |
| `strength` | DOUBLE | - | `0.0` | 强弱度(%) |
| `activity` | DOUBLE | - | `0.0` | 活跃度(%) |
| `avg_turnover` | DOUBLE | - | `0.0` | 笔换手 |
| `attack` | DOUBLE | - | `0.0` | 攻击波(%) |
| `interval_3` | DOUBLE | - | `0.0` | 近3月涨幅 |
| `interval_6` | DOUBLE | - | `0.0` | 近6月涨幅 |

---

### stk_weekly_monthly

**表名**: `stk_weekly_monthly` | **说明**: 股票周/月线行情(每日更新) | **主键**: `ts_code`, `trade_date`, `freq` | **依赖表**: `stock/basic/stock_basic`, `stock/basic/trade_cal`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | 股票代码 |
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `freq` | VARCHAR(255) | 255 | `` | 频率(周week,月month) |
| `open` | DOUBLE | - | `0.0` | (周/月)开盘价 |
| `high` | DOUBLE | - | `0.0` | (周/月)最高价 |
| `low` | DOUBLE | - | `0.0` | (周/月)最低价 |
| `close` | DOUBLE | - | `0.0` | (周/月)收盘价 |
| `pre_close` | DOUBLE | - | `0.0` | 上一(周/月)收盘价 |
| `vol` | DOUBLE | - | `0.0` | (周/月)成交量 |
| `amount` | DOUBLE | - | `0.0` | (周/月)成交额 |
| `change` | DOUBLE | - | `0.0` | (周/月)涨跌额 |
| `pct_chg` | DOUBLE | - | `0.0` | (周/月)涨跌幅(未复权,如果是复权请用 通用行情接口) |

---

## 股票-市场数据 {#股票-市场数据}

本分类共包含 **17** 个数据表。

### 表列表

- [margin](#margin) - 融资融券交易汇总
- [margin_detail](#margin-detail) - 融资融券交易明细
- [top10_holders](#top10-holders) - 前十大股东
- [top10_floatholders](#top10-floatholders) - 前十大流通股东
- [top_list](#top-list) - 龙虎榜每日明细
- [top_inst](#top-inst) - 龙虎榜机构明细
- [pledge_stat](#pledge-stat) - 股权质押统计数据
- [pledge_detail](#pledge-detail) - 股权质押明细
- [repurchase](#repurchase) - 股票回购
- [concept](#concept) - 概念股分类
- [concept_detail](#concept-detail) - 概念股列表
- [share_float](#share-float) - 限售股解禁
- [block_trade](#block-trade) - 大宗交易
- [stk_holdernumber](#stk-holdernumber) - 股东户数
- [stk_holdertrade](#stk-holdertrade) - 股东增减持
- [margin_target](#margin-target) - 融资融券标的
- [margin_secs](#margin-secs) - 融资融券标的（新）

### margin

**表名**: `margin` | **说明**: 融资融券交易汇总 | **依赖表**: `stock/basic/trade_cal` | **索引**: `{'name': 'idx_default', 'columns': ['trade_date']}`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `exchange_id` | VARCHAR(255) | 255 | `` | 交易所代码（SSE上交所SZSE深交所） |
| `rzye` | DOUBLE | - | `0.0` | 融资余额(元) |
| `rzmre` | DOUBLE | - | `0.0` | 融资买入额(元) |
| `rzche` | DOUBLE | - | `0.0` | 融资偿还额(元) |
| `rqye` | DOUBLE | - | `0.0` | 融券余额(元) |
| `rqmcl` | DOUBLE | - | `0.0` | 融券卖出量(股,份,手) |
| `rzrqye` | DOUBLE | - | `0.0` | 融资融券余额(元) |
| `rqyl` | DOUBLE | - | `0.0` | 融券余量 |

---

### margin_detail

**表名**: `margin_detail` | **说明**: 融资融券交易明细 | **依赖表**: `stock/basic/trade_cal` | **索引**: `{'name': 'idx_default', 'columns': ['ts_code', 'trade_date']}`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `ts_code` | VARCHAR(16) | 16 | `` | TS股票代码 |
| `name` | VARCHAR(255) | 255 | `` | 股票名称 |
| `rzye` | DOUBLE | - | `0.0` | 融资余额(元) |
| `rqye` | DOUBLE | - | `0.0` | 融券余额(元) |
| `rzmre` | DOUBLE | - | `0.0` | 融资买入额(元) |
| `rqyl` | DOUBLE | - | `0.0` | 融券余量（手） |
| `rzche` | DOUBLE | - | `0.0` | 融资偿还额(元) |
| `rqchl` | DOUBLE | - | `0.0` | 融券偿还量(手) |
| `rqmcl` | DOUBLE | - | `0.0` | 融券卖出量(股,份,手) |
| `rzrqye` | DOUBLE | - | `0.0` | 融资融券余额(元) |

---

### top10_holders

**表名**: `top10_holders` | **说明**: 前十大股东 | **主键**: `ts_code`, `ann_date` | **依赖表**: `stock/basic/stock_basic`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | TS股票代码 |
| `ann_date` | DATE | - | `1970-01-01` | 公告日期 |
| `end_date` | DATE | - | `1970-01-01` | 报告期 |
| `holder_name` | VARCHAR(255) | 255 | `` | 股东名称 |
| `hold_amount` | DOUBLE | - | `0.0` | 持有数量 |
| `hold_ratio` | DOUBLE | - | `0.0` | 占总股本比例(%) |
| `hold_float_ratio` | DOUBLE | - | `0.0` | 占流通股本比例(%) |
| `hold_change` | DOUBLE | - | `0.0` | 持股变动 |
| `holder_type` | VARCHAR(255) | 255 | `` | 股东性质 |

---

### top10_floatholders

**表名**: `top10_floatholders` | **说明**: 前十大流通股东 | **主键**: `ts_code`, `ann_date` | **依赖表**: `stock/basic/stock_basic`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | TS股票代码 |
| `ann_date` | DATE | - | `1970-01-01` | 公告日期 |
| `end_date` | DATE | - | `1970-01-01` | 报告期 |
| `holder_name` | VARCHAR(255) | 255 | `` | 股东名称 |
| `hold_amount` | DOUBLE | - | `0.0` | 持有数量 |
| `hold_ratio` | DOUBLE | - | `0.0` | 占总股本比例(%) |
| `hold_float_ratio` | DOUBLE | - | `0.0` | 占流通股本比例(%) |
| `hold_change` | DOUBLE | - | `0.0` | 持股变动 |
| `holder_type` | VARCHAR(255) | 255 | `` | 股东性质 |

---

### top_list

**表名**: `top_list` | **说明**: 龙虎榜每日明细 | **主键**: `ts_code`, `trade_date` | **依赖表**: `stock/basic/stock_basic`, `stock/basic/trade_cal`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `ts_code` | VARCHAR(16) | 16 | `` | TS代码 |
| `name` | VARCHAR(255) | 255 | `` | 名称 |
| `close` | DOUBLE | - | `0.0` | 收盘价 |
| `pct_change` | DOUBLE | - | `0.0` | 涨跌幅 |
| `turnover_rate` | DOUBLE | - | `0.0` | 换手率 |
| `amount` | DOUBLE | - | `0.0` | 总成交额 |
| `l_sell` | DOUBLE | - | `0.0` | 龙虎榜卖出额 |
| `l_buy` | DOUBLE | - | `0.0` | 龙虎榜买入额 |
| `l_amount` | DOUBLE | - | `0.0` | 龙虎榜成交额 |
| `net_amount` | DOUBLE | - | `0.0` | 龙虎榜净买入额 |
| `net_rate` | DOUBLE | - | `0.0` | 龙虎榜净买额占比 |
| `amount_rate` | DOUBLE | - | `0.0` | 龙虎榜成交额占比 |
| `float_values` | DOUBLE | - | `0.0` | 当日流通市值 |
| `reason` | VARCHAR(255) | 255 | `` | 上榜理由 |

---

### top_inst

**表名**: `top_inst` | **说明**: 龙虎榜机构明细 | **主键**: `ts_code`, `trade_date` | **依赖表**: `stock/basic/stock_basic`, `stock/basic/trade_cal`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `ts_code` | VARCHAR(16) | 16 | `` | TS代码 |
| `exalter` | VARCHAR(255) | 255 | `` | 营业部名称 |
| `buy` | DOUBLE | - | `0.0` | 买入额（万） |
| `buy_rate` | DOUBLE | - | `0.0` | 买入占总成交比例 |
| `sell` | DOUBLE | - | `0.0` | 卖出额（万） |
| `sell_rate` | DOUBLE | - | `0.0` | 卖出占总成交比例 |
| `net_buy` | DOUBLE | - | `0.0` | 净成交额（万） |
| `side` | VARCHAR(255) | 255 | `` | 买卖类型0买入1卖出 |
| `reason` | VARCHAR(255) | 255 | `` | 上榜理由 |

---

### pledge_stat

**表名**: `pledge_stat` | **说明**: 股权质押统计数据 | **主键**: `ts_code`, `end_date`, `update_flag` | **依赖表**: `stock/basic/stock_basic`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | TS代码 |
| `end_date` | DATE | - | `1970-01-01` | 截至日期 |
| `pledge_count` | INTEGER | - | `0` | 质押次数 |
| `unrest_pledge` | DOUBLE | - | `0.0` | 无限售股质押数量（万） |
| `rest_pledge` | DOUBLE | - | `0.0` | 限售股份质押数量（万） |
| `total_share` | DOUBLE | - | `0.0` | 总股本 |
| `pledge_ratio` | DOUBLE | - | `0.0` | 质押比例 |
| `update_flag` | VARCHAR(255) | 255 | `` | 更新标识 |

---

### pledge_detail

**表名**: `pledge_detail` | **说明**: 股权质押明细 | **主键**: `ts_code`, `ann_date` | **依赖表**: `stock/basic/stock_basic`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | TS股票代码 |
| `ann_date` | DATE | - | `1970-01-01` | 公告日期 |
| `holder_name` | VARCHAR(255) | 255 | `` | 股东名称 |
| `holder_type` | VARCHAR(255) | 255 | `` | 股东类型 |
| `pledge_amount` | DOUBLE | - | `0.0` | 质押数量 |
| `start_date` | DATE | - | `1970-01-01` | 质押开始日期 |
| `end_date` | DATE | - | `1970-01-01` | 质押结束日期 |
| `is_release` | VARCHAR(255) | 255 | `` | 是否已解押 |
| `release_date` | DATE | - | `1970-01-01` | 解押日期 |
| `pledgor` | VARCHAR(255) | 255 | `` | 质押方 |
| `holding_amount` | DOUBLE | - | `0.0` | 持股总数 |
| `pledged_amount` | DOUBLE | - | `0.0` | 质押总数 |
| `p_total_ratio` | DOUBLE | - | `0.0` | 本次质押占总股本比例 |
| `h_total_ratio` | DOUBLE | - | `0.0` | 持股总数占总股本比例 |
| `is_buyback` | VARCHAR(255) | 255 | `` | 是否回购 |
| `desc` | VARCHAR(255) | 255 | `` | 备注 |

---

### repurchase

**表名**: `repurchase` | **说明**: 股票回购 | **主键**: `ts_code`, `ann_date`, `update_flag` | **依赖表**: `stock/basic/stock_basic`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | TS代码 |
| `ann_date` | DATE | - | `1970-01-01` | 公告日期 |
| `end_date` | DATE | - | `1970-01-01` | 截止日期 |
| `proc` | VARCHAR(255) | 255 | `` | 进度 |
| `exp_date` | DATE | - | `1970-01-01` | 过期日期 |
| `vol` | DOUBLE | - | `0.0` | 回购数量 |
| `amount` | DOUBLE | - | `0.0` | 回购金额 |
| `high_limit` | DOUBLE | - | `0.0` | 回购最高价 |
| `low_limit` | DOUBLE | - | `0.0` | 回购最低价 |
| `repo_goal` | VARCHAR(255) | 255 | `` | 回购目的 |
| `update_flag` | VARCHAR(255) | 255 | `` | 更新标识 |

---

### concept

**表名**: `concept` | **说明**: 概念股分类 | **主键**: `code`, `src`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `code` | VARCHAR(255) | 255 | `` | 概念分类ID |
| `name` | VARCHAR(255) | 255 | `` | 概念分类名称 |
| `src` | VARCHAR(255) | 255 | `` | 来源 |

---

### concept_detail

**表名**: `concept_detail` | **说明**: 概念股列表 | **主键**: `ts_code`, `id` | **依赖表**: `stock/market/concept`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `id` | VARCHAR(255) | 255 | `` | 概念代码 |
| `concept_name` | VARCHAR(255) | 255 | `` | 概念名称 |
| `ts_code` | VARCHAR(16) | 16 | `` | 股票代码 |
| `name` | VARCHAR(255) | 255 | `` | 股票名称 |
| `in_date` | DATE | - | `1970-01-01` | 纳入日期 |
| `out_date` | DATE | - | `1970-01-01` | 剔除日期 |

---

### share_float

**表名**: `share_float` | **说明**: 限售股解禁 | **主键**: `ts_code`, `ann_date`, `float_date` | **依赖表**: `stock/basic/stock_basic`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | TS代码 |
| `ann_date` | DATE | - | `1970-01-01` | 公告日期 |
| `float_date` | DATE | - | `1970-01-01` | 解禁日期 |
| `float_share` | DOUBLE | - | `0.0` | 流通股份 |
| `float_ratio` | DOUBLE | - | `0.0` | 流通股份占总股本比率 |
| `holder_name` | VARCHAR(255) | 255 | `` | 股东名称 |
| `share_type` | VARCHAR(255) | 255 | `` | 股份类型 |

---

### block_trade

**表名**: `block_trade` | **说明**: 大宗交易 | **主键**: `ts_code`, `trade_date` | **依赖表**: `stock/basic/stock_basic`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | TS代码 |
| `trade_date` | DATE | - | `1970-01-01` | 交易日历 |
| `price` | DOUBLE | - | `0.0` | 成交价 |
| `vol` | DOUBLE | - | `0.0` | 成交量（万股） |
| `amount` | DOUBLE | - | `0.0` | 成交金额 |
| `buyer` | VARCHAR(255) | 255 | `` | 买方营业部 |
| `seller` | VARCHAR(255) | 255 | `` | 卖房营业部 |

---

### stk_holdernumber

**表名**: `stk_holdernumber` | **说明**: 股东户数 | **主键**: `ts_code`, `ann_date` | **依赖表**: `stock/basic/stock_basic`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | TS股票代码 |
| `ann_date` | DATE | - | `1970-01-01` | 公告日期 |
| `end_date` | DATE | - | `1970-01-01` | 截止日期 |
| `holder_nums` | INTEGER | - | `0` | 股东户数 |
| `holder_num` | INTEGER | - | `0` | 股东总户数（A+B） |

---

### stk_holdertrade

**表名**: `stk_holdertrade` | **说明**: 股东增减持 | **主键**: `ts_code`, `ann_date` | **依赖表**: `stock/basic/stock_basic`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | TS代码 |
| `ann_date` | DATE | - | `1970-01-01` | 公告日期 |
| `holder_name` | VARCHAR(255) | 255 | `` | 股东名称 |
| `holder_type` | VARCHAR(255) | 255 | `` | 股东类型G高管P个人C公司 |
| `in_de` | VARCHAR(255) | 255 | `` | 类型IN增持DE减持 |
| `change_vol` | DOUBLE | - | `0.0` | 变动数量 |
| `change_ratio` | DOUBLE | - | `0.0` | 占流通比例（%） |
| `after_share` | DOUBLE | - | `0.0` | 变动后持股 |
| `after_ratio` | DOUBLE | - | `0.0` | 变动后占流通比例（%） |
| `avg_price` | DOUBLE | - | `0.0` | 平均价格 |
| `total_share` | DOUBLE | - | `0.0` | 持股总数 |
| `begin_date` | DATE | - | `1970-01-01` | 增减持开始日期 |
| `close_date` | DATE | - | `1970-01-01` | 增减持结束日期 |

---

### margin_target

**表名**: `margin_target` | **说明**: 融资融券标的 | **主键**: `ts_code` | **依赖表**: `stock/basic/stock_basic`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | 标的代码 |
| `mg_type` | VARCHAR(255) | 255 | `` | 标的类型：B买入标的 S卖出标的 |
| `is_new` | VARCHAR(255) | 255 | `` | 最新标记：Y是 N否 |
| `in_date` | DATE | - | `1970-01-01` | 纳入日期 |
| `out_date` | DATE | - | `1970-01-01` | 剔除日期 |
| `ann_date` | DATE | - | `1970-01-01` | 公布日期 |

---

### margin_secs

**表名**: `margin_secs` | **说明**: 融资融券标的（新） | **主键**: `ts_code`, `trade_date`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `ts_code` | VARCHAR(16) | 16 | `` | 股票代码 |
| `name` | VARCHAR(255) | 255 | `` | 股票名称 |
| `exchange` | VARCHAR(255) | 255 | `` | 交易所 |

---

## 股票-资金流向 {#股票-资金流向}

本分类共包含 **7** 个数据表。

### 表列表

- [moneyflow_hsgt](#moneyflow-hsgt) - 沪深港通资金流向
- [moneyflow](#moneyflow) - 个股资金流向
- [moneyflow_ind_ths](#moneyflow-ind-ths) - 行业资金流向（THS）
- [moneyflow_ind_dc](#moneyflow-ind-dc) - 板块资金流向（DC）
- [moneyflow_mkt_dc](#moneyflow-mkt-dc) - 大盘资金流向（DC）
- [moneyflow_ths](#moneyflow-ths) - 个股资金流向（THS）
- [moneyflow_dc](#moneyflow-dc) - 个股资金流向（DC）

### moneyflow_hsgt

**表名**: `moneyflow_hsgt` | **说明**: 沪深港通资金流向 | **主键**: `trade_date` | **依赖表**: `stock/basic/stock_basic`, `stock/basic/trade_cal`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `ggt_ss` | DOUBLE | - | `0.0` | 港股通（上海） |
| `ggt_sz` | DOUBLE | - | `0.0` | 港股通（深圳） |
| `hgt` | DOUBLE | - | `0.0` | 沪股通 |
| `sgt` | DOUBLE | - | `0.0` | 深股通 |
| `north_money` | DOUBLE | - | `0.0` | 北向资金 |
| `south_money` | DOUBLE | - | `0.0` | 南向资金 |

---

### moneyflow

**表名**: `moneyflow` | **说明**: 个股资金流向 | **主键**: `ts_code`, `trade_date` | **依赖表**: `stock/basic/stock_basic`, `stock/basic/trade_cal`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | TS代码 |
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `buy_sm_vol` | INTEGER | - | `0` | 小单买入量（手） |
| `buy_sm_amount` | DOUBLE | - | `0.0` | 小单买入金额（万元） |
| `sell_sm_vol` | INTEGER | - | `0` | 小单卖出量（手） |
| `sell_sm_amount` | DOUBLE | - | `0.0` | 小单卖出金额（万元） |
| `buy_md_vol` | INTEGER | - | `0` | 中单买入量（手） |
| `buy_md_amount` | DOUBLE | - | `0.0` | 中单买入金额（万元） |
| `sell_md_vol` | INTEGER | - | `0` | 中单卖出量（手） |
| `sell_md_amount` | DOUBLE | - | `0.0` | 中单卖出金额（万元） |
| `buy_lg_vol` | INTEGER | - | `0` | 大单买入量（手） |
| `buy_lg_amount` | DOUBLE | - | `0.0` | 大单买入金额（万元） |
| `sell_lg_vol` | INTEGER | - | `0` | 大单卖出量（手） |
| `sell_lg_amount` | DOUBLE | - | `0.0` | 大单卖出金额（万元） |
| `buy_elg_vol` | INTEGER | - | `0` | 特大单买入量（手） |
| `buy_elg_amount` | DOUBLE | - | `0.0` | 特大单买入金额（万元） |
| `sell_elg_vol` | INTEGER | - | `0` | 特大单卖出量（手） |
| `sell_elg_amount` | DOUBLE | - | `0.0` | 特大单卖出金额（万元） |
| `net_mf_vol` | INTEGER | - | `0` | 净流入量（手） |
| `net_mf_amount` | DOUBLE | - | `0.0` | 净流入额（万元） |
| `trade_count` | INTEGER | - | `0` | 交易笔数 |

---

### moneyflow_ind_ths

**表名**: `moneyflow_ind_ths` | **说明**: 行业资金流向（THS） | **主键**: `ts_code`, `trade_date` | **依赖表**: `stock_basic`, `trade_cal`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `ts_code` | VARCHAR(16) | 16 | `` | 板块代码 |
| `industry` | VARCHAR(255) | 255 | `` | 板块名称 |
| `lead_stock` | VARCHAR(255) | 255 | `` | 领涨股票名称 |
| `close` | DOUBLE | - | `0.0` | 收盘指数 |
| `pct_change` | DOUBLE | - | `0.0` | 指数涨跌幅 |
| `company_num` | INTEGER | - | `0` | 公司数量 |
| `pct_change_stock` | DOUBLE | - | `0.0` | 领涨股涨跌幅 |
| `close_price` | DOUBLE | - | `0.0` | 领涨股最新价 |
| `net_buy_amount` | DOUBLE | - | `0.0` | 流入资金(元) |
| `net_sell_amount` | DOUBLE | - | `0.0` | 流出资金(元) |
| `net_amount` | DOUBLE | - | `0.0` | 净额(元) |

---

### moneyflow_ind_dc

**表名**: `moneyflow_ind_dc` | **说明**: 板块资金流向（DC） | **主键**: `ts_code`, `trade_date` | **依赖表**: `stock_basic`, `trade_cal`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `ts_code` | VARCHAR(16) | 16 | `` | 股票代码 |
| `name` | VARCHAR(255) | 255 | `` | 股票名称 |
| `pct_change` | DOUBLE | - | `0.0` | 涨跌幅（%） |
| `close` | DOUBLE | - | `0.0` | 最新价（元） |
| `net_amount` | DOUBLE | - | `0.0` | 今日主力净流入 净额（元） |
| `net_amount_rate` | DOUBLE | - | `0.0` | 今日主力净流入净占比% |
| `buy_elg_amount` | DOUBLE | - | `0.0` | 今日超大单净流入 净额（元） |
| `buy_elg_amount_rate` | DOUBLE | - | `0.0` | 今日超大单净流入 净占比% |
| `buy_lg_amount` | DOUBLE | - | `0.0` | 今日大单净流入 净额（元） |
| `buy_lg_amount_rate` | DOUBLE | - | `0.0` | 今日大单净流入 净占比% |
| `buy_md_amount` | DOUBLE | - | `0.0` | 今日中单净流入 净额（元） |
| `buy_md_amount_rate` | DOUBLE | - | `0.0` | 今日中单净流入 净占比% |
| `buy_sm_amount` | DOUBLE | - | `0.0` | 今日小单净流入 净额（元） |
| `buy_sm_amount_rate` | DOUBLE | - | `0.0` | 今日小单净流入 净占比% |
| `buy_sm_amount_stock` | VARCHAR(255) | 255 | `` | 今日主力净流入最大股 |
| `rank` | INTEGER | - | `0` | 序号 |

---

### moneyflow_mkt_dc

**表名**: `moneyflow_mkt_dc` | **说明**: 大盘资金流向（DC） | **主键**: `trade_date` | **依赖表**: `stock_basic`, `trade_cal`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `close_sh` | DOUBLE | - | `0.0` | 上证收盘价（元） |
| `pct_change_sh` | DOUBLE | - | `0.0` | 上证涨跌幅(%) |
| `close_sz` | DOUBLE | - | `0.0` | 深证收盘价（元） |
| `pct_change_sz` | DOUBLE | - | `0.0` | 深证涨跌幅(%) |
| `net_amount` | DOUBLE | - | `0.0` | 今日主力净流入 净额（元） |
| `net_amount_rate` | DOUBLE | - | `0.0` | 今日主力净流入净占比% |
| `buy_elg_amount` | DOUBLE | - | `0.0` | 今日超大单净流入 净额（元） |
| `buy_elg_amount_rate` | DOUBLE | - | `0.0` | 今日超大单净流入 净占比% |
| `buy_lg_amount` | DOUBLE | - | `0.0` | 今日大单净流入 净额（元） |
| `buy_lg_amount_rate` | DOUBLE | - | `0.0` | 今日大单净流入 净占比% |
| `buy_md_amount` | DOUBLE | - | `0.0` | 今日中单净流入 净额（元） |
| `buy_md_amount_rate` | DOUBLE | - | `0.0` | 今日中单净流入 净占比% |
| `buy_sm_amount` | DOUBLE | - | `0.0` | 今日小单净流入 净额（元） |
| `buy_sm_amount_rate` | DOUBLE | - | `0.0` | 今日小单净流入 净占比% |

---

### moneyflow_ths

**表名**: `moneyflow_ths` | **说明**: 个股资金流向（THS） | **主键**: `ts_code`, `trade_date` | **依赖表**: `stock_basic`, `trade_cal`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `ts_code` | VARCHAR(16) | 16 | `` | 股票代码 |
| `name` | VARCHAR(255) | 255 | `` | 股票名称 |
| `pct_change` | DOUBLE | - | `0.0` | 涨跌幅 |
| `latest` | DOUBLE | - | `0.0` | 最新价 |
| `net_amount` | DOUBLE | - | `0.0` | 资金净流入(万元) |
| `net_d5_amount` | DOUBLE | - | `0.0` | 5日主力净额(万元) |
| `buy_lg_amount` | DOUBLE | - | `0.0` | 今日大单净流入额(万元) |
| `buy_lg_amount_rate` | DOUBLE | - | `0.0` | 今日大单净流入占比(%) |
| `buy_md_amount` | DOUBLE | - | `0.0` | 今日中单净流入额(万元) |
| `buy_md_amount_rate` | DOUBLE | - | `0.0` | 今日中单净流入占比(%) |
| `buy_sm_amount` | DOUBLE | - | `0.0` | 今日小单净流入额(万元) |
| `buy_sm_amount_rate` | DOUBLE | - | `0.0` | 今日小单净流入占比(%) |

---

### moneyflow_dc

**表名**: `moneyflow_dc` | **说明**: 个股资金流向（DC） | **主键**: `ts_code`, `trade_date` | **依赖表**: `stock_basic`, `trade_cal`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `ts_code` | VARCHAR(16) | 16 | `` | 股票代码 |
| `name` | VARCHAR(255) | 255 | `` | 股票名称 |
| `pct_change` | DOUBLE | - | `0.0` | 涨跌幅 |
| `close` | DOUBLE | - | `0.0` | 最新价 |
| `net_amount` | DOUBLE | - | `0.0` | 今日主力净流入额（万元） |
| `net_amount_rate` | DOUBLE | - | `0.0` | 今日主力净流入净占比（%） |
| `buy_elg_amount` | DOUBLE | - | `0.0` | 今日超大单净流入额（万元） |
| `buy_elg_amount_rate` | DOUBLE | - | `0.0` | 今日超大单净流入占比（%） |
| `buy_lg_amount` | DOUBLE | - | `0.0` | 今日大单净流入额（万元） |
| `buy_lg_amount_rate` | DOUBLE | - | `0.0` | 今日大单净流入占比（%） |
| `buy_md_amount` | DOUBLE | - | `0.0` | 今日中单净流入额（万元） |
| `buy_md_amount_rate` | DOUBLE | - | `0.0` | 今日中单净流入占比（%） |
| `buy_sm_amount` | DOUBLE | - | `0.0` | 今日小单净流入额（万元） |
| `buy_sm_amount_rate` | DOUBLE | - | `0.0` | 今日小单净流入占比（%） |

---

## 股票-融资融券 {#股票-融资融券}

本分类共包含 **6** 个数据表。

### 表列表

- [margin](#margin) - 融资融券交易汇总
- [margin_detail](#margin-detail) - 融资融券交易明细
- [slb_len](#slb-len) - 转融资交易汇总
- [slb_sec](#slb-sec) - 转融券交易汇总
- [slb_sec_detail](#slb-sec-detail) - 转融券交易明细
- [slb_len_mm](#slb-len-mm) - 做市借券交易汇总

### margin

**表名**: `margin` | **说明**: 融资融券交易汇总 | **主键**: `trade_date` | **依赖表**: `stock/basic/trade_cal`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `exchange_id` | VARCHAR(255) | 255 | `` | 交易所代码（SSE上交所SZSE深交所） |
| `rzye` | DOUBLE | - | `0.0` | 融资余额(元) |
| `rzmre` | DOUBLE | - | `0.0` | 融资买入额(元) |
| `rzche` | DOUBLE | - | `0.0` | 融资偿还额(元) |
| `rqye` | DOUBLE | - | `0.0` | 融券余额(元) |
| `rqmcl` | DOUBLE | - | `0.0` | 融券卖出量(股,份,手) |
| `rzrqye` | DOUBLE | - | `0.0` | 融资融券余额(元) |
| `rqyl` | DOUBLE | - | `0.0` | 融券余量 |

---

### margin_detail

**表名**: `margin_detail` | **说明**: 融资融券交易明细 | **主键**: `ts_code`, `trade_date` | **依赖表**: `stock/basic/trade_cal`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `ts_code` | VARCHAR(16) | 16 | `` | TS股票代码 |
| `name` | VARCHAR(255) | 255 | `` | 股票名称 |
| `rzye` | DOUBLE | - | `0.0` | 融资余额(元) |
| `rqye` | DOUBLE | - | `0.0` | 融券余额(元) |
| `rzmre` | DOUBLE | - | `0.0` | 融资买入额(元) |
| `rqyl` | DOUBLE | - | `0.0` | 融券余量（手） |
| `rzche` | DOUBLE | - | `0.0` | 融资偿还额(元) |
| `rqchl` | DOUBLE | - | `0.0` | 融券偿还量(手) |
| `rqmcl` | DOUBLE | - | `0.0` | 融券卖出量(股,份,手) |
| `rzrqye` | DOUBLE | - | `0.0` | 融资融券余额(元) |

---

### slb_len

**表名**: `slb_len` | **说明**: 转融资交易汇总 | **主键**: `trade_date` | **依赖表**: `stock/basic/trade_cal`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `trade_date` | DATE | - | `1970-01-01` | 交易日期（YYYYMMDD） |
| `ob` | DOUBLE | - | `0.0` | 期初余额(亿元) |
| `auc_amount` | DOUBLE | - | `0.0` | 竞价成交金额(亿元) |
| `repo_amount` | DOUBLE | - | `0.0` | 再借成交金额(亿元) |
| `repay_amount` | DOUBLE | - | `0.0` | 偿还金额(亿元) |
| `cb` | DOUBLE | - | `0.0` | 期末余额(亿元) |

---

### slb_sec

**表名**: `slb_sec` | **说明**: 转融券交易汇总 | **主键**: `ts_code`, `trade_date` | **依赖表**: `stock/basic/trade_cal`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `trade_date` | DATE | - | `1970-01-01` | 交易日期（YYYYMMDD） |
| `ts_code` | VARCHAR(16) | 16 | `` | 股票代码 |
| `name` | VARCHAR(255) | 255 | `` | 股票名称 |
| `ope_inv` | DOUBLE | - | `0.0` | 期初余量(万股) |
| `lent_qnt` | DOUBLE | - | `0.0` | 转融券融出数量(万股) |
| `cls_inv` | DOUBLE | - | `0.0` | 期末余量(万股) |
| `end_bal` | DOUBLE | - | `0.0` | 期末余额(万元) |

---

### slb_sec_detail

**表名**: `slb_sec_detail` | **说明**: 转融券交易明细 | **主键**: `ts_code`, `trade_date` | **依赖表**: `stock/basic/trade_cal`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `trade_date` | DATE | - | `1970-01-01` | 交易日期（YYYYMMDD） |
| `ts_code` | VARCHAR(16) | 16 | `` | 股票代码 |
| `name` | VARCHAR(255) | 255 | `` | 股票名称 |
| `tenor` | VARCHAR(255) | 255 | `` | 期 限(天) |
| `fee_rate` | DOUBLE | - | `0.0` | 融出费率(%) |
| `lent_qnt` | DOUBLE | - | `0.0` | 转融券融出数量(万股) |

---

### slb_len_mm

**表名**: `slb_len_mm` | **说明**: 做市借券交易汇总 | **主键**: `ts_code`, `trade_date` | **依赖表**: `stock/basic/trade_cal`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `trade_date` | DATE | - | `1970-01-01` | 交易日期（YYYYMMDD） |
| `ts_code` | VARCHAR(16) | 16 | `` | 股票代码 |
| `name` | VARCHAR(255) | 255 | `` | 股票名称 |
| `ope_inv` | DOUBLE | - | `0.0` | 期初余量(万股) |
| `lent_qnt` | DOUBLE | - | `0.0` | 融出数量(万股) |
| `cls_inv` | DOUBLE | - | `0.0` | 期末余量(万股) |
| `end_bal` | DOUBLE | - | `0.0` | 期末余额(万元) |

---

## 股票-涨跌停 {#股票-涨跌停}

本分类共包含 **11** 个数据表。

### 表列表

- [limit_list_d](#limit-list-d) - 涨跌停列表（新）
- [hm_list](#hm-list) - 游资名录
- [hm_detail](#hm-detail) - 游资每日明细
- [ths_hot](#ths-hot) - 同花顺热板
- [dc_hot](#dc-hot) - 东方财富热板
- [kpl_list](#kpl-list) - 榜单数据（开盘啦）
- [kpl_concept](#kpl-concept) - 题材数据（开盘啦）
- [kpl_concept_cons](#kpl-concept-cons) - 题材成分（开盘啦）
- [limit_list_ths](#limit-list-ths) - 涨跌停列表（同花顺）
- [limit_step](#limit-step) - 涨停股票连板天梯
- [limit_cpt_list](#limit-cpt-list) - 涨停最强板块统计

### limit_list_d

**表名**: `limit_list_d` | **说明**: 涨跌停列表（新） | **主键**: `ts_code`, `trade_date`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `ts_code` | VARCHAR(16) | 16 | `` | 股票代码 |
| `industry` | VARCHAR(255) | 255 | `` | 所属行业 |
| `name` | VARCHAR(255) | 255 | `` | 股票名称 |
| `close` | DOUBLE | - | `0.0` | 收盘价 |
| `pct_chg` | DOUBLE | - | `0.0` | 涨跌幅 |
| `swing` | DOUBLE | - | `0.0` | 振幅 |
| `amount` | DOUBLE | - | `0.0` | 成交额 |
| `limit_amount` | DOUBLE | - | `0.0` | 板上成交金额 |
| `float_mv` | DOUBLE | - | `0.0` | 流通市值 |
| `total_mv` | DOUBLE | - | `0.0` | 总市值 |
| `turnover_ratio` | DOUBLE | - | `0.0` | 换手率 |
| `fd_amount` | DOUBLE | - | `0.0` | 封单金额 |
| `first_time` | VARCHAR(255) | 255 | `` | 首次封板时间 |
| `last_time` | VARCHAR(255) | 255 | `` | 最后封板时间 |
| `open_times` | INTEGER | - | `0` | 炸板次数 |
| `up_stat` | VARCHAR(255) | 255 | `` | 涨停统计 |
| `limit_times` | INTEGER | - | `0` | 连板数 |
| `limit` | VARCHAR(255) | 255 | `` | D跌停U涨停Z炸板 |

---

### hm_list

**表名**: `hm_list` | **说明**: 游资名录 | **主键**: `name`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `name` | VARCHAR(255) | 255 | `` | 无说明 |
| `desc` | VARCHAR(255) | 255 | `` | 描述 |
| `orgs` | VARCHAR(255) | 255 | `` | 关联机构 |

---

### hm_detail

**表名**: `hm_detail` | **说明**: 游资每日明细 | **主键**: `ts_code`, `trade_date`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `ts_code` | VARCHAR(16) | 16 | `` | 无说明 |
| `ts_name` | VARCHAR(255) | 255 | `` | 无说明 |
| `buy_amount` | DOUBLE | - | `0.0` | 买入数量（万） |
| `sell_amount` | DOUBLE | - | `0.0` | 卖出数量（万） |
| `net_amount` | DOUBLE | - | `0.0` | 净买入（买卖和（万）） |
| `tag` | VARCHAR(255) | 255 | `` | 标签 |
| `hm_name` | VARCHAR(255) | 255 | `` | 游资名称 |
| `hm_orgs` | VARCHAR(255) | 255 | `` | 关联机构 |

---

### ths_hot

**表名**: `ths_hot` | **说明**: 同花顺热板 | **主键**: `ts_code`, `trade_date`, `data_type`, `rank_time` | **依赖表**: `stock/basic/trade_cal`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `data_type` | VARCHAR(255) | 255 | `` | 数据类型 |
| `ts_code` | VARCHAR(16) | 16 | `` | 股票代码 |
| `ts_name` | VARCHAR(255) | 255 | `` | 股票名称 |
| `rank` | INTEGER | - | `0` | 排行或者热度 |
| `pct_change` | DOUBLE | - | `0.0` | 涨跌幅% |
| `current_price` | DOUBLE | - | `0.0` | 当前价格 |
| `hot` | DOUBLE | - | `0.0` | 热度 |
| `concept` | VARCHAR(255) | 255 | `` | 标签 |
| `rank_time` | VARCHAR(255) | 255 | `` | 排行榜获取时间 |
| `rank_reason` | VARCHAR(255) | 255 | `` | 上榜解读 |

---

### dc_hot

**表名**: `dc_hot` | **说明**: 东方财富热板 | **主键**: `trade_date`, `data_type`, `ts_code`, `rank_time` | **依赖表**: `stock/basic/stock_basic`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `data_type` | VARCHAR(255) | 255 | `` | 数据类型 |
| `ts_code` | VARCHAR(16) | 16 | `` | 股票代码 |
| `ts_name` | VARCHAR(255) | 255 | `` | 股票名称 |
| `rank` | INTEGER | - | `0` | 排行或者热度 |
| `pct_change` | DOUBLE | - | `0.0` | 涨跌幅% |
| `current_price` | DOUBLE | - | `0.0` | 当前价格 |
| `hot` | DOUBLE | - | `0.0` | 热度 |
| `concept` | VARCHAR(255) | 255 | `` | 标签 |
| `rank_time` | VARCHAR(255) | 255 | `` | 排行榜获取时间 |

---

### kpl_list

**表名**: `kpl_list` | **说明**: 榜单数据（开盘啦） | **主键**: `ts_code`, `trade_date`, `tag`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | 代码 |
| `name` | VARCHAR(255) | 255 | `` | 名称 |
| `trade_date` | DATE | - | `1970-01-01` | 交易时间 |
| `lu_time` | VARCHAR(255) | 255 | `` | 涨停时间 |
| `ld_time` | VARCHAR(255) | 255 | `` | 跌停时间 |
| `open_time` | VARCHAR(255) | 255 | `` | 开板时间 |
| `last_time` | VARCHAR(255) | 255 | `` | 最后涨停时间 |
| `lu_desc` | VARCHAR(255) | 255 | `` | 涨停原因 |
| `tag` | VARCHAR(255) | 255 | `` | 标签\|类别 |
| `theme` | VARCHAR(255) | 255 | `` | 板块 |
| `net_change` | DOUBLE | - | `0.0` | 主力净额(元) |
| `bid_amount` | DOUBLE | - | `0.0` | 主力净额(元) |
| `status` | VARCHAR(255) | 255 | `` | 状态 |
| `bid_change` | DOUBLE | - | `0.0` | 竞价成交额(元\|个) |
| `bid_turnover` | DOUBLE | - | `0.0` | 竞价换手)% |
| `lu_bid_vol` | DOUBLE | - | `0.0` | 涨停委买额(元\|个) |
| `pct_chg` | DOUBLE | - | `0.0` | 涨跌幅% |
| `bid_pct_chg` | DOUBLE | - | `0.0` | 竞价涨幅% |
| `rt_pct_chg` | DOUBLE | - | `0.0` | 实时涨幅% |
| `limit_order` | DOUBLE | - | `0.0` | 封单(元\|个) |
| `amount` | DOUBLE | - | `0.0` | 成交额(元\|个) |
| `turnover_rate` | DOUBLE | - | `0.0` | 换手率% |
| `free_float` | DOUBLE | - | `0.0` | 实际流通(元\|个) |
| `lu_limit_order` | DOUBLE | - | `0.0` | 最大封单(元\|个) |

---

### kpl_concept

**表名**: `kpl_concept` | **说明**: 题材数据（开盘啦） | **主键**: `ts_code`, `trade_date`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `ts_code` | VARCHAR(16) | 16 | `` | 题材代码 |
| `name` | VARCHAR(255) | 255 | `` | 题材名称 |
| `z_t_num` | INTEGER | - | `0` | 涨停数量 |
| `up_num` | VARCHAR(255) | 255 | `` | 排名上升位数 |

---

### kpl_concept_cons

**表名**: `kpl_concept_cons` | **说明**: 题材成分（开盘啦） | **主键**: `ts_code`, `cons_code`, `trade_date`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | 题材ID |
| `name` | VARCHAR(255) | 255 | `` | 题材名称 |
| `cons_name` | VARCHAR(255) | 255 | `` | 股票名称 |
| `cons_code` | VARCHAR(255) | 255 | `` | 股票代码 |
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `desc` | VARCHAR(255) | 255 | `` | 描述 |
| `hot_num` | INTEGER | - | `0` | 人气值 |

---

### limit_list_ths

**表名**: `limit_list_ths` | **说明**: 涨跌停列表（同花顺） | **主键**: `ts_code`, `trade_date`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `ts_code` | VARCHAR(16) | 16 | `` | 股票代码 |
| `name` | VARCHAR(255) | 255 | `` | 股票名称 |
| `price` | DOUBLE | - | `0.0` | 最近价格(元) |
| `pct_chg` | DOUBLE | - | `0.0` | 涨跌幅% |
| `open_num` | INTEGER | - | `0` | 打开次数 |
| `lu_desc` | VARCHAR(255) | 255 | `` | 涨停原因 |
| `limit_type` | VARCHAR(255) | 255 | `` | 板单类别 |
| `tag` | VARCHAR(255) | 255 | `` | 涨停标签 |
| `status` | VARCHAR(255) | 255 | `` | 涨停状态（N连板、一字板） |
| `first_lu_time` | VARCHAR(255) | 255 | `` | 首次涨停时间 |
| `last_lu_time` | VARCHAR(255) | 255 | `` | 最后涨停时间 |
| `first_ld_time` | VARCHAR(255) | 255 | `` | 首次跌停时间 |
| `last_ld_time` | VARCHAR(255) | 255 | `` | 最后涨停时间 |
| `limit_order` | DOUBLE | - | `0.0` | 封单量(元\|个) |
| `limit_amount` | DOUBLE | - | `0.0` | 封单额(元\|个) |
| `turnover_rate` | DOUBLE | - | `0.0` | 换手率% |
| `free_float` | DOUBLE | - | `0.0` | 实际流通(元\|个) |
| `lu_limit_order` | DOUBLE | - | `0.0` | 最大封单(元\|个) |
| `limit_up_suc_rate` | DOUBLE | - | `0.0` | 近一年涨停封板率 |
| `turnover` | DOUBLE | - | `0.0` | 成交额 |
| `rise_rate` | DOUBLE | - | `0.0` | 涨速 |
| `sum_float` | DOUBLE | - | `0.0` |  总市值 亿元 |
| `market_type` | VARCHAR(255) | 255 | `` | 股票类型：HS沪深主板、GEM创业板、STAR科创板 |

---

### limit_step

**表名**: `limit_step` | **说明**: 涨停股票连板天梯 | **主键**: `ts_code`, `trade_date`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | 代码 |
| `name` | VARCHAR(255) | 255 | `` | 名称 |
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `nums` | VARCHAR(255) | 255 | `` | 连板次数 |

---

### limit_cpt_list

**表名**: `limit_cpt_list` | **说明**: 涨停最强板块统计 | **主键**: `ts_code`, `trade_date`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | 板块代码 |
| `name` | VARCHAR(255) | 255 | `` | 板块名称 |
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `days` | VARCHAR(255) | 255 | `` | 上榜天数 |
| `up_stat` | VARCHAR(255) | 255 | `` | 连板高度 |
| `cons_nums` | VARCHAR(255) | 255 | `` | 连板家数 |
| `up_nums` | VARCHAR(255) | 255 | `` | 涨停家数 |
| `pct_chg` | DOUBLE | - | `0.0` | 涨跌幅% |
| `rank` | VARCHAR(255) | 255 | `` | 板块热点排名 |

---

## 股票-特殊数据 {#股票-特殊数据}

本分类共包含 **15** 个数据表。

### 表列表

- [hk_hold](#hk-hold) - 沪深股通持股明细
- [broker_recommend](#broker-recommend) - 券商每月荐股
- [stk_surv](#stk-surv) - 机构调研表
- [ccass_hold](#ccass-hold) - 中央结算系统持股汇总
- [ccass_hold_detail](#ccass-hold-detail) - 中央结算系统持股明细
- [report_rc](#report-rc) - 卖方盈利预测数据
- [cyq_perf](#cyq-perf) - 每日筹码及胜率
- [cyq_chips](#cyq-chips) - 每日筹码分布
- [stk_factor](#stk-factor) - 股票技术因子
- [limit_list_d](#limit-list-d) - 涨跌停列表（新）
- [hm_list](#hm-list) - 游资名录
- [hm_detail](#hm-detail) - 游资每日明细
- [ths_hot](#ths-hot) - 同花顺热板
- [dc_hot](#dc-hot) - 东方财富热板
- [stk_factor_pro](#stk-factor-pro) - 股票技术因子(专业版)

### hk_hold

**表名**: `hk_hold` | **说明**: 沪深股通持股明细 | **主键**: `ts_code`, `trade_date`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `code` | VARCHAR(255) | 255 | `` | 原始代码 |
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `ts_code` | VARCHAR(16) | 16 | `` | TS代码 |
| `name` | VARCHAR(255) | 255 | `` | 股票名称 |
| `vol` | INTEGER | - | `0` | 持股数量 |
| `ratio` | DOUBLE | - | `0.0` | 持股占比 |
| `exchange` | VARCHAR(255) | 255 | `` | 类型:SH沪股通SZ深港通 |

---

### broker_recommend

**表名**: `broker_recommend` | **说明**: 券商每月荐股 | **主键**: `month`, `broker`, `ts_code`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `month` | VARCHAR(255) | 255 | `` | 月度 |
| `broker` | VARCHAR(255) | 255 | `` | 券商 |
| `ts_code` | VARCHAR(16) | 16 | `` | 股票代码 |
| `name` | VARCHAR(255) | 255 | `` | 股票简称 |

---

### stk_surv

**表名**: `stk_surv` | **说明**: 机构调研表 | **主键**: `ts_code`, `surv_date` | **依赖表**: `stock/basic/stock_basic`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | 股票代码 |
| `name` | VARCHAR(255) | 255 | `` | 股票名称 |
| `surv_date` | DATE | - | `1970-01-01` | 调研日期 |
| `fund_visitors` | VARCHAR(255) | 255 | `` | 机构参与人员 |
| `rece_place` | VARCHAR(255) | 255 | `` | 接待地点 |
| `rece_mode` | VARCHAR(255) | 255 | `` | 接待方式 |
| `rece_org` | VARCHAR(255) | 255 | `` | 接待的公司 |
| `org_type` | VARCHAR(255) | 255 | `` | 接待公司类型 |
| `comp_rece` | VARCHAR(255) | 255 | `` | 上市公司接待人员 |
| `content` | VARCHAR(255) | 255 | `` | 调研内容 |

---

### ccass_hold

**表名**: `ccass_hold` | **说明**: 中央结算系统持股汇总 | **主键**: `ts_code`, `trade_date` | **依赖表**: `stock/basic/trade_cal`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `ts_code` | VARCHAR(16) | 16 | `` | 股票代号 |
| `name` | VARCHAR(255) | 255 | `` | 股票名称 |
| `shareholding` | VARCHAR(255) | 255 | `` | 于中央结算系统的持股量(股) |
| `hold_nums` | VARCHAR(255) | 255 | `` | 参与者数目（个） |
| `hold_ratio` | VARCHAR(255) | 255 | `` | 占于上交所/深交所上市及交易的A股总数的百分比（%） |

---

### ccass_hold_detail

**表名**: `ccass_hold_detail` | **说明**: 中央结算系统持股明细 | **主键**: `ts_code`, `trade_date` | **依赖表**: `stock/basic/trade_cal`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `ts_code` | VARCHAR(16) | 16 | `` | 股票代号 |
| `name` | VARCHAR(255) | 255 | `` | 股票名称 |
| `col_participant_id` | VARCHAR(255) | 255 | `` | 参与者编号 |
| `col_participant_name` | VARCHAR(255) | 255 | `` | 机构名称 |
| `col_shareholding` | VARCHAR(255) | 255 | `` | 持股量(股) |
| `col_shareholding_percent` | VARCHAR(255) | 255 | `` | 占已发行股份/权证/单位百分比(%) |

---

### report_rc

**表名**: `report_rc` | **说明**: 卖方盈利预测数据 | **主键**: `ts_code`, `report_date` | **依赖表**: `stock/basic/stock_basic`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | 股票代码 |
| `name` | VARCHAR(255) | 255 | `` | 股票名称 |
| `report_date` | DATE | - | `1970-01-01` | 研报日期 |
| `report_title` | VARCHAR(255) | 255 | `` | 报告标题 |
| `report_type` | VARCHAR(255) | 255 | `` | 报告类型 |
| `classify` | VARCHAR(255) | 255 | `` | 报告分类 |
| `org_name` | VARCHAR(255) | 255 | `` | 机构名称 |
| `author_name` | VARCHAR(255) | 255 | `` | 作者 |
| `quarter` | VARCHAR(255) | 255 | `` | 预测报告期 |
| `op_rt` | DOUBLE | - | `0.0` | 预测营业收入（万元） |
| `op_pr` | DOUBLE | - | `0.0` | 预测营业利润（万元） |
| `tp` | DOUBLE | - | `0.0` | 预测利润总额（万元） |
| `np` | DOUBLE | - | `0.0` | 预测净利润（万元） |
| `eps` | DOUBLE | - | `0.0` | 预测每股收益（元） |
| `pe` | DOUBLE | - | `0.0` | 预测市盈率（元） |
| `rd` | DOUBLE | - | `0.0` | 预测股息率（元） |
| `roe` | DOUBLE | - | `0.0` | 预测净资产收益率（元） |
| `ev_ebitda` | DOUBLE | - | `0.0` | 预测EV/EBITDA |
| `rating` | VARCHAR(255) | 255 | `` | 卖方评级 |
| `max_price` | DOUBLE | - | `0.0` | 预测最高目标价 |
| `min_price` | DOUBLE | - | `0.0` | 预测最低目标价 |
| `imp_dg` | VARCHAR(255) | 255 | `` | 机构关注度 |
| `create_time` | DATETIME | - | `1970-01-01 00:00:00` | TS数据更新时间 |

---

### cyq_perf

**表名**: `cyq_perf` | **说明**: 每日筹码及胜率 | **主键**: `ts_code`, `trade_date` | **依赖表**: `stock/basic/trade_cal`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | 股票代码 |
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `his_low` | DOUBLE | - | `0.0` | 历史最低价 |
| `his_high` | DOUBLE | - | `0.0` | 历史最高价 |
| `cost_5pct` | DOUBLE | - | `0.0` | 5分位成本 |
| `cost_15pct` | DOUBLE | - | `0.0` | 15分位成本 |
| `cost_50pct` | DOUBLE | - | `0.0` | 50分位成本 |
| `cost_85pct` | DOUBLE | - | `0.0` | 85分位成本 |
| `cost_95pct` | DOUBLE | - | `0.0` | 95分位成本 |
| `weight_avg` | DOUBLE | - | `0.0` | 加权平均成本 |
| `winner_rate` | DOUBLE | - | `0.0` | 胜率 |

---

### cyq_chips

**表名**: `cyq_chips` | **说明**: 每日筹码分布 | **主键**: `ts_code`, `trade_date` | **依赖表**: `stock/basic/stock_basic`, `stock/quotes/daily`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | 股票代码 |
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `price` | DOUBLE | - | `0.0` | 成本价格 |
| `percent` | DOUBLE | - | `0.0` | 价格占比（%） |

---

### stk_factor

**表名**: `stk_factor` | **说明**: 股票技术因子 | **主键**: `ts_code`, `trade_date` | **依赖表**: `stock/basic/trade_cal`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | 股票代码 |
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `close` | DOUBLE | - | `0.0` | 收盘价 |
| `open` | DOUBLE | - | `0.0` | 开盘价 |
| `high` | DOUBLE | - | `0.0` | 最高价 |
| `low` | DOUBLE | - | `0.0` | 最低价 |
| `pre_close` | DOUBLE | - | `0.0` | 昨收价 |
| `change` | DOUBLE | - | `0.0` | 涨跌额 |
| `pct_change` | DOUBLE | - | `0.0` | 涨跌幅 |
| `vol` | DOUBLE | - | `0.0` | 成交量 （手） |
| `amount` | DOUBLE | - | `0.0` | 成交额 （千元） |
| `adj_factor` | DOUBLE | - | `0.0` | 复权因子 |
| `open_hfq` | DOUBLE | - | `0.0` | 开盘价后复权 |
| `open_qfq` | DOUBLE | - | `0.0` | 开盘价前复权 |
| `close_hfq` | DOUBLE | - | `0.0` | 收盘价后复权 |
| `close_qfq` | DOUBLE | - | `0.0` | 收盘价前复权 |
| `high_hfq` | DOUBLE | - | `0.0` | 最高价后复权 |
| `high_qfq` | DOUBLE | - | `0.0` | 最高价前复权 |
| `low_hfq` | DOUBLE | - | `0.0` | 最低价后复权 |
| `low_qfq` | DOUBLE | - | `0.0` | 最低价前复权 |
| `pre_close_hfq` | DOUBLE | - | `0.0` | 昨收价后复权 |
| `pre_close_qfq` | DOUBLE | - | `0.0` | 昨收价前复权 |
| `macd_dif` | DOUBLE | - | `0.0` | macd_diff |
| `macd_dea` | DOUBLE | - | `0.0` | macd_dea |
| `macd` | DOUBLE | - | `0.0` | macd |
| `kdj_k` | DOUBLE | - | `0.0` | KDJ_K |
| `kdj_d` | DOUBLE | - | `0.0` | KDJ_D |
| `kdj_j` | DOUBLE | - | `0.0` | KDJ_J |
| `rsi_6` | DOUBLE | - | `0.0` | RSI_6 |
| `rsi_12` | DOUBLE | - | `0.0` | RSI_12 |
| `rsi_24` | DOUBLE | - | `0.0` | RSI_24 |
| `boll_upper` | DOUBLE | - | `0.0` | BOLL_UPPER |
| `boll_mid` | DOUBLE | - | `0.0` | BOLL_MID |
| `boll_lower` | DOUBLE | - | `0.0` | BOLL_LOWER |
| `cci` | DOUBLE | - | `0.0` | CCI |

---

### limit_list_d

**表名**: `limit_list_d` | **说明**: 涨跌停列表（新） | **主键**: `ts_code`, `trade_date` | **依赖表**: `stock/basic/trade_cal`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `ts_code` | VARCHAR(16) | 16 | `` | 股票代码 |
| `industry` | VARCHAR(255) | 255 | `` | 所属行业 |
| `name` | VARCHAR(255) | 255 | `` | 股票名称 |
| `close` | DOUBLE | - | `0.0` | 收盘价 |
| `pct_chg` | DOUBLE | - | `0.0` | 涨跌幅 |
| `swing` | DOUBLE | - | `0.0` | 振幅 |
| `amount` | DOUBLE | - | `0.0` | 成交额 |
| `limit_amount` | DOUBLE | - | `0.0` | 板上成交金额 |
| `float_mv` | DOUBLE | - | `0.0` | 流通市值 |
| `total_mv` | DOUBLE | - | `0.0` | 总市值 |
| `turnover_ratio` | DOUBLE | - | `0.0` | 换手率 |
| `fd_amount` | DOUBLE | - | `0.0` | 封单金额 |
| `first_time` | VARCHAR(255) | 255 | `` | 首次封板时间 |
| `last_time` | VARCHAR(255) | 255 | `` | 最后封板时间 |
| `open_times` | INTEGER | - | `0` | 炸板次数 |
| `up_stat` | VARCHAR(255) | 255 | `` | 涨停统计 |
| `limit_times` | INTEGER | - | `0` | 连板数 |
| `limit` | VARCHAR(255) | 255 | `` | D跌停U涨停Z炸板 |

---

### hm_list

**表名**: `hm_list` | **说明**: 游资名录 | **主键**: `name`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `name` | VARCHAR(255) | 255 | `` | 无说明 |
| `desc` | VARCHAR(255) | 255 | `` | 描述 |
| `orgs` | VARCHAR(255) | 255 | `` | 关联机构 |

---

### hm_detail

**表名**: `hm_detail` | **说明**: 游资每日明细 | **主键**: `ts_code`, `trade_date`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `ts_code` | VARCHAR(16) | 16 | `` | 无说明 |
| `ts_name` | VARCHAR(255) | 255 | `` | 无说明 |
| `buy_amount` | DOUBLE | - | `0.0` | 买入数量（万） |
| `sell_amount` | DOUBLE | - | `0.0` | 卖出数量（万） |
| `net_amount` | DOUBLE | - | `0.0` | 净买入（买卖和（万）） |
| `tag` | VARCHAR(255) | 255 | `` | 标签 |
| `hm_name` | VARCHAR(255) | 255 | `` | 游资名称 |
| `hm_orgs` | VARCHAR(255) | 255 | `` | 关联机构 |

---

### ths_hot

**表名**: `ths_hot` | **说明**: 同花顺热板 | **主键**: `trade_date`, `data_type`, `ts_code`, `rank_time` | **依赖表**: `stock/basic/trade_cal`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `data_type` | VARCHAR(255) | 255 | `` | 数据类型 |
| `ts_code` | VARCHAR(16) | 16 | `` | 股票代码 |
| `ts_name` | VARCHAR(255) | 255 | `` | 股票名称 |
| `rank` | INTEGER | - | `0` | 排行或者热度 |
| `pct_change` | DOUBLE | - | `0.0` | 涨跌幅% |
| `current_price` | DOUBLE | - | `0.0` | 当前价格 |
| `hot` | DOUBLE | - | `0.0` | 热度 |
| `concept` | VARCHAR(255) | 255 | `` | 标签 |
| `rank_time` | VARCHAR(255) | 255 | `` | 排行榜获取时间 |
| `rank_reason` | VARCHAR(255) | 255 | `` | 上榜解读 |

---

### dc_hot

**表名**: `dc_hot` | **说明**: 东方财富热板 | **主键**: `trade_date`, `data_type`, `ts_code`, `rank_time` | **依赖表**: `stock/basic/trade_cal`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `data_type` | VARCHAR(255) | 255 | `` | 数据类型 |
| `ts_code` | VARCHAR(16) | 16 | `` | 股票代码 |
| `ts_name` | VARCHAR(255) | 255 | `` | 股票名称 |
| `rank` | INTEGER | - | `0` | 排行或者热度 |
| `pct_change` | DOUBLE | - | `0.0` | 涨跌幅% |
| `current_price` | DOUBLE | - | `0.0` | 当前价格 |
| `hot` | DOUBLE | - | `0.0` | 热度 |
| `concept` | VARCHAR(255) | 255 | `` | 标签 |
| `rank_time` | VARCHAR(255) | 255 | `` | 排行榜获取时间 |

---

### stk_factor_pro

**表名**: `stk_factor_pro` | **说明**: 股票技术因子(专业版) | **主键**: `ts_code`, `trade_date` | **依赖表**: `stock/basic/trade_cal`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | 股票代码 |
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `open` | DOUBLE | - | `0.0` | 开盘价 |
| `open_hfq` | DOUBLE | - | `0.0` | 开盘价 |
| `open_qfq` | DOUBLE | - | `0.0` | 开盘价 |
| `high` | DOUBLE | - | `0.0` | 最高价 |
| `high_hfq` | DOUBLE | - | `0.0` | 最高价 |
| `high_qfq` | DOUBLE | - | `0.0` | 最高价 |
| `low` | DOUBLE | - | `0.0` | 最低价 |
| `low_hfq` | DOUBLE | - | `0.0` | 最低价 |
| `low_qfq` | DOUBLE | - | `0.0` | 最低价 |
| `close` | DOUBLE | - | `0.0` | 收盘价 |
| `close_hfq` | DOUBLE | - | `0.0` | 收盘价 |
| `close_qfq` | DOUBLE | - | `0.0` | 收盘价 |
| `pre_close` | DOUBLE | - | `0.0` | 昨收价(前复权) |
| `change` | DOUBLE | - | `0.0` | 涨跌额 |
| `pct_chg` | DOUBLE | - | `0.0` | 涨跌幅 （未复权，如果是复权请用 通用行情接口 ） |
| `vol` | DOUBLE | - | `0.0` | 成交量 （手） |
| `amount` | DOUBLE | - | `0.0` | 成交额 （千元） |
| `turnover_rate` | DOUBLE | - | `0.0` | 换手率（%） |
| `turnover_rate_f` | DOUBLE | - | `0.0` | 换手率（自由流通股） |
| `volume_ratio` | DOUBLE | - | `0.0` | 量比 |
| `pe` | DOUBLE | - | `0.0` | 市盈率（总市值/净利润， 亏损的PE为空） |
| `pe_ttm` | DOUBLE | - | `0.0` | 市盈率（TTM，亏损的PE为空） |
| `pb` | DOUBLE | - | `0.0` | 市净率（总市值/净资产） |
| `ps` | DOUBLE | - | `0.0` | 市销率 |
| `ps_ttm` | DOUBLE | - | `0.0` | 市销率（TTM） |
| `dv_ratio` | DOUBLE | - | `0.0` | 股息率 （%） |
| `dv_ttm` | DOUBLE | - | `0.0` | 股息率（TTM）（%） |
| `total_share` | DOUBLE | - | `0.0` | 总股本 （万股） |
| `float_share` | DOUBLE | - | `0.0` | 流通股本 （万股） |
| `free_share` | DOUBLE | - | `0.0` | 自由流通股本 （万） |
| `total_mv` | DOUBLE | - | `0.0` | 总市值 （万元） |
| `circ_mv` | DOUBLE | - | `0.0` | 流通市值（万元） |
| `adj_factor` | DOUBLE | - | `0.0` | 复权因子 |
| `asi_bfq` | DOUBLE | - | `0.0` | 振动升降指标-OPEN, CLOSE, HIGH, LOW, M1=26, M2=10 |
| `asi_hfq` | DOUBLE | - | `0.0` | 振动升降指标-OPEN, CLOSE, HIGH, LOW, M1=26, M2=10 |
| `asi_qfq` | DOUBLE | - | `0.0` | 振动升降指标-OPEN, CLOSE, HIGH, LOW, M1=26, M2=10 |
| `asit_bfq` | DOUBLE | - | `0.0` | 振动升降指标-OPEN, CLOSE, HIGH, LOW, M1=26, M2=10 |
| `asit_hfq` | DOUBLE | - | `0.0` | 振动升降指标-OPEN, CLOSE, HIGH, LOW, M1=26, M2=10 |
| `asit_qfq` | DOUBLE | - | `0.0` | 振动升降指标-OPEN, CLOSE, HIGH, LOW, M1=26, M2=10 |
| `atr_bfq` | DOUBLE | - | `0.0` | 真实波动N日平均值-CLOSE, HIGH, LOW, N=20 |
| `atr_hfq` | DOUBLE | - | `0.0` | 真实波动N日平均值-CLOSE, HIGH, LOW, N=20 |
| `atr_qfq` | DOUBLE | - | `0.0` | 真实波动N日平均值-CLOSE, HIGH, LOW, N=20 |
| `bbi_bfq` | DOUBLE | - | `0.0` | BBI多空指标-CLOSE, M1=3, M2=6, M3=12, M4=20 |
| `bbi_hfq` | DOUBLE | - | `0.0` | BBI多空指标-CLOSE, M1=3, M2=6, M3=12, M4=21 |
| `bbi_qfq` | DOUBLE | - | `0.0` | BBI多空指标-CLOSE, M1=3, M2=6, M3=12, M4=22 |
| `bias1_bfq` | DOUBLE | - | `0.0` | BIAS乖离率-CLOSE, L1=6, L2=12, L3=24 |
| `bias1_hfq` | DOUBLE | - | `0.0` | BIAS乖离率-CLOSE, L1=6, L2=12, L3=24 |
| `bias1_qfq` | DOUBLE | - | `0.0` | BIAS乖离率-CLOSE, L1=6, L2=12, L3=24 |
| `bias2_bfq` | DOUBLE | - | `0.0` | BIAS乖离率-CLOSE, L1=6, L2=12, L3=24 |
| `bias2_hfq` | DOUBLE | - | `0.0` | BIAS乖离率-CLOSE, L1=6, L2=12, L3=24 |
| `bias2_qfq` | DOUBLE | - | `0.0` | BIAS乖离率-CLOSE, L1=6, L2=12, L3=24 |
| `bias3_bfq` | DOUBLE | - | `0.0` | BIAS乖离率-CLOSE, L1=6, L2=12, L3=24 |
| `bias3_hfq` | DOUBLE | - | `0.0` | BIAS乖离率-CLOSE, L1=6, L2=12, L3=24 |
| `bias3_qfq` | DOUBLE | - | `0.0` | BIAS乖离率-CLOSE, L1=6, L2=12, L3=24 |
| `boll_lower_bfq` | DOUBLE | - | `0.0` | BOLL指标，布林带-CLOSE, N=20, P=2 |
| `boll_lower_hfq` | DOUBLE | - | `0.0` | BOLL指标，布林带-CLOSE, N=20, P=2 |
| `boll_lower_qfq` | DOUBLE | - | `0.0` | BOLL指标，布林带-CLOSE, N=20, P=2 |
| `boll_mid_bfq` | DOUBLE | - | `0.0` | BOLL指标，布林带-CLOSE, N=20, P=2 |
| `boll_mid_hfq` | DOUBLE | - | `0.0` | BOLL指标，布林带-CLOSE, N=20, P=2 |
| `boll_mid_qfq` | DOUBLE | - | `0.0` | BOLL指标，布林带-CLOSE, N=20, P=2 |
| `boll_upper_bfq` | DOUBLE | - | `0.0` | BOLL指标，布林带-CLOSE, N=20, P=2 |
| `boll_upper_hfq` | DOUBLE | - | `0.0` | BOLL指标，布林带-CLOSE, N=20, P=2 |
| `boll_upper_qfq` | DOUBLE | - | `0.0` | BOLL指标，布林带-CLOSE, N=20, P=2 |
| `brar_ar_bfq` | DOUBLE | - | `0.0` |  BRAR情绪指标-OPEN, CLOSE, HIGH, LOW, M1=26 |
| `brar_ar_hfq` | DOUBLE | - | `0.0` |  BRAR情绪指标-OPEN, CLOSE, HIGH, LOW, M1=26 |
| `brar_ar_qfq` | DOUBLE | - | `0.0` |  BRAR情绪指标-OPEN, CLOSE, HIGH, LOW, M1=26 |
| `brar_br_bfq` | DOUBLE | - | `0.0` |  BRAR情绪指标-OPEN, CLOSE, HIGH, LOW, M1=26 |
| `brar_br_hfq` | DOUBLE | - | `0.0` |  BRAR情绪指标-OPEN, CLOSE, HIGH, LOW, M1=26 |
| `brar_br_qfq` | DOUBLE | - | `0.0` |  BRAR情绪指标-OPEN, CLOSE, HIGH, LOW, M1=26 |
| `cci_bfq` | DOUBLE | - | `0.0` | 顺势指标又叫CCI指标-CLOSE, HIGH, LOW, N=14 |
| `cci_hfq` | DOUBLE | - | `0.0` | 顺势指标又叫CCI指标-CLOSE, HIGH, LOW, N=14 |
| `cci_qfq` | DOUBLE | - | `0.0` | 顺势指标又叫CCI指标-CLOSE, HIGH, LOW, N=14 |
| `cr_bfq` | DOUBLE | - | `0.0` | CR价格动量指标-CLOSE, HIGH, LOW, N=20 |
| `cr_hfq` | DOUBLE | - | `0.0` | CR价格动量指标-CLOSE, HIGH, LOW, N=20 |
| `cr_qfq` | DOUBLE | - | `0.0` | CR价格动量指标-CLOSE, HIGH, LOW, N=20 |
| `dfma_dif_bfq` | DOUBLE | - | `0.0` | 平行线差指标-CLOSE, N1=10, N2=50, M=10 |
| `dfma_dif_hfq` | DOUBLE | - | `0.0` | 平行线差指标-CLOSE, N1=10, N2=50, M=10 |
| `dfma_dif_qfq` | DOUBLE | - | `0.0` | 平行线差指标-CLOSE, N1=10, N2=50, M=10 |
| `dfma_difma_bfq` | DOUBLE | - | `0.0` | 平行线差指标-CLOSE, N1=10, N2=50, M=10 |
| `dfma_difma_hfq` | DOUBLE | - | `0.0` | 平行线差指标-CLOSE, N1=10, N2=50, M=10 |
| `dfma_difma_qfq` | DOUBLE | - | `0.0` | 平行线差指标-CLOSE, N1=10, N2=50, M=10 |
| `dmi_adx_bfq` | DOUBLE | - | `0.0` |  动向指标-CLOSE, HIGH, LOW, M1=14, M2=6 |
| `dmi_adx_hfq` | DOUBLE | - | `0.0` |  动向指标-CLOSE, HIGH, LOW, M1=14, M2=6 |
| `dmi_adx_qfq` | DOUBLE | - | `0.0` |  动向指标-CLOSE, HIGH, LOW, M1=14, M2=6 |
| `dmi_adxr_bfq` | DOUBLE | - | `0.0` |  动向指标-CLOSE, HIGH, LOW, M1=14, M2=6 |
| `dmi_adxr_hfq` | DOUBLE | - | `0.0` |  动向指标-CLOSE, HIGH, LOW, M1=14, M2=6 |
| `dmi_adxr_qfq` | DOUBLE | - | `0.0` |  动向指标-CLOSE, HIGH, LOW, M1=14, M2=6 |
| `dmi_mdi_bfq` | DOUBLE | - | `0.0` |  动向指标-CLOSE, HIGH, LOW, M1=14, M2=6 |
| `dmi_mdi_hfq` | DOUBLE | - | `0.0` |  动向指标-CLOSE, HIGH, LOW, M1=14, M2=6 |
| `dmi_mdi_qfq` | DOUBLE | - | `0.0` |  动向指标-CLOSE, HIGH, LOW, M1=14, M2=6 |
| `dmi_pdi_bfq` | DOUBLE | - | `0.0` |  动向指标-CLOSE, HIGH, LOW, M1=14, M2=6 |
| `dmi_pdi_hfq` | DOUBLE | - | `0.0` |  动向指标-CLOSE, HIGH, LOW, M1=14, M2=6 |
| `dmi_pdi_qfq` | DOUBLE | - | `0.0` |  动向指标-CLOSE, HIGH, LOW, M1=14, M2=6 |
| `downdays` | DOUBLE | - | `0.0` | 连跌天数 |
| `updays` | DOUBLE | - | `0.0` | 连涨天数 |
| `dpo_bfq` | DOUBLE | - | `0.0` | 区间震荡线-CLOSE, M1=20, M2=10, M3=6 |
| `dpo_hfq` | DOUBLE | - | `0.0` | 区间震荡线-CLOSE, M1=20, M2=10, M3=6 |
| `dpo_qfq` | DOUBLE | - | `0.0` | 区间震荡线-CLOSE, M1=20, M2=10, M3=6 |
| `madpo_bfq` | DOUBLE | - | `0.0` | 区间震荡线-CLOSE, M1=20, M2=10, M3=6 |
| `madpo_hfq` | DOUBLE | - | `0.0` | 区间震荡线-CLOSE, M1=20, M2=10, M3=6 |
| `madpo_qfq` | DOUBLE | - | `0.0` | 区间震荡线-CLOSE, M1=20, M2=10, M3=6 |
| `ema_bfq_10` | DOUBLE | - | `0.0` | 指数移动平均-N=10 |
| `ema_bfq_20` | DOUBLE | - | `0.0` | 指数移动平均-N=20 |
| `ema_bfq_250` | DOUBLE | - | `0.0` | 指数移动平均-N=250 |
| `ema_bfq_30` | DOUBLE | - | `0.0` | 指数移动平均-N=30 |
| `ema_bfq_5` | DOUBLE | - | `0.0` | 指数移动平均-N=5 |
| `ema_bfq_60` | DOUBLE | - | `0.0` | 指数移动平均-N=60 |
| `ema_bfq_90` | DOUBLE | - | `0.0` | 指数移动平均-N=90 |
| `ema_hfq_10` | DOUBLE | - | `0.0` | 指数移动平均-N=10 |
| `ema_hfq_20` | DOUBLE | - | `0.0` | 指数移动平均-N=20 |
| `ema_hfq_250` | DOUBLE | - | `0.0` | 指数移动平均-N=250 |
| `ema_hfq_30` | DOUBLE | - | `0.0` | 指数移动平均-N=30 |
| `ema_hfq_5` | DOUBLE | - | `0.0` | 指数移动平均-N=5 |
| `ema_hfq_60` | DOUBLE | - | `0.0` | 指数移动平均-N=60 |
| `ema_hfq_90` | DOUBLE | - | `0.0` | 指数移动平均-N=90 |
| `ema_qfq_10` | DOUBLE | - | `0.0` | 指数移动平均-N=10 |
| `ema_qfq_20` | DOUBLE | - | `0.0` | 指数移动平均-N=20 |
| `ema_qfq_250` | DOUBLE | - | `0.0` | 指数移动平均-N=250 |
| `ema_qfq_30` | DOUBLE | - | `0.0` | 指数移动平均-N=30 |
| `ema_qfq_5` | DOUBLE | - | `0.0` | 指数移动平均-N=5 |
| `ema_qfq_60` | DOUBLE | - | `0.0` | 指数移动平均-N=60 |
| `ema_qfq_90` | DOUBLE | - | `0.0` | 指数移动平均-N=90 |
| `emv_bfq` | DOUBLE | - | `0.0` | 简易波动指标-HIGH, LOW, VOL, N=14, M=9 |
| `emv_hfq` | DOUBLE | - | `0.0` | 简易波动指标-HIGH, LOW, VOL, N=14, M=9 |
| `emv_qfq` | DOUBLE | - | `0.0` | 简易波动指标-HIGH, LOW, VOL, N=14, M=9 |
| `maemv_bfq` | DOUBLE | - | `0.0` | 简易波动指标-HIGH, LOW, VOL, N=14, M=9 |
| `maemv_hfq` | DOUBLE | - | `0.0` | 简易波动指标-HIGH, LOW, VOL, N=14, M=9 |
| `maemv_qfq` | DOUBLE | - | `0.0` | 简易波动指标-HIGH, LOW, VOL, N=14, M=9 |
| `expma_12_bfq` | DOUBLE | - | `0.0` | EMA指数平均数指标-CLOSE, N1=12, N2=50 |
| `expma_12_hfq` | DOUBLE | - | `0.0` | EMA指数平均数指标-CLOSE, N1=12, N2=50 |
| `expma_12_qfq` | DOUBLE | - | `0.0` | EMA指数平均数指标-CLOSE, N1=12, N2=50 |
| `expma_50_bfq` | DOUBLE | - | `0.0` | EMA指数平均数指标-CLOSE, N1=12, N2=50 |
| `expma_50_hfq` | DOUBLE | - | `0.0` | EMA指数平均数指标-CLOSE, N1=12, N2=50 |
| `expma_50_qfq` | DOUBLE | - | `0.0` | EMA指数平均数指标-CLOSE, N1=12, N2=50 |
| `kdj_bfq` | DOUBLE | - | `0.0` | KDJ指标-CLOSE, HIGH, LOW, N=9, M1=3, M2=3 |
| `kdj_hfq` | DOUBLE | - | `0.0` | KDJ指标-CLOSE, HIGH, LOW, N=9, M1=3, M2=3 |
| `kdj_qfq` | DOUBLE | - | `0.0` | KDJ指标-CLOSE, HIGH, LOW, N=9, M1=3, M2=3 |
| `kdj_d_bfq` | DOUBLE | - | `0.0` | KDJ指标-CLOSE, HIGH, LOW, N=9, M1=3, M2=3 |
| `kdj_d_hfq` | DOUBLE | - | `0.0` | KDJ指标-CLOSE, HIGH, LOW, N=9, M1=3, M2=3 |
| `kdj_d_qfq` | DOUBLE | - | `0.0` | KDJ指标-CLOSE, HIGH, LOW, N=9, M1=3, M2=3 |
| `kdj_k_bfq` | DOUBLE | - | `0.0` | KDJ指标-CLOSE, HIGH, LOW, N=9, M1=3, M2=3 |
| `kdj_k_hfq` | DOUBLE | - | `0.0` | KDJ指标-CLOSE, HIGH, LOW, N=9, M1=3, M2=3 |
| `kdj_k_qfq` | DOUBLE | - | `0.0` | KDJ指标-CLOSE, HIGH, LOW, N=9, M1=3, M2=3 |
| `ktn_down_bfq` | DOUBLE | - | `0.0` | 肯特纳交易通道, N选20日，ATR选10日-CLOSE, HIGH, LOW, N=20, M=10 |
| `ktn_down_hfq` | DOUBLE | - | `0.0` | 肯特纳交易通道, N选20日，ATR选10日-CLOSE, HIGH, LOW, N=20, M=10 |
| `ktn_down_qfq` | DOUBLE | - | `0.0` | 肯特纳交易通道, N选20日，ATR选10日-CLOSE, HIGH, LOW, N=20, M=10 |
| `ktn_mid_bfq` | DOUBLE | - | `0.0` | 肯特纳交易通道, N选20日，ATR选10日-CLOSE, HIGH, LOW, N=20, M=10 |
| `ktn_mid_hfq` | DOUBLE | - | `0.0` | 肯特纳交易通道, N选20日，ATR选10日-CLOSE, HIGH, LOW, N=20, M=10 |
| `ktn_mid_qfq` | DOUBLE | - | `0.0` | 肯特纳交易通道, N选20日，ATR选10日-CLOSE, HIGH, LOW, N=20, M=10 |
| `ktn_upper_bfq` | DOUBLE | - | `0.0` | 肯特纳交易通道, N选20日，ATR选10日-CLOSE, HIGH, LOW, N=20, M=10 |
| `ktn_upper_hfq` | DOUBLE | - | `0.0` | 肯特纳交易通道, N选20日，ATR选10日-CLOSE, HIGH, LOW, N=20, M=10 |
| `ktn_upper_qfq` | DOUBLE | - | `0.0` | 肯特纳交易通道, N选20日，ATR选10日-CLOSE, HIGH, LOW, N=20, M=10 |
| `lowdays` | DOUBLE | - | `0.0` | LOWRANGE(LOW)表示当前最低价是近多少周期内最低价的最小值 |
| `topdays` | DOUBLE | - | `0.0` | TOPRANGE(HIGH)表示当前最高价是近多少周期内最高价的最大值 |
| `ma_bfq_10` | DOUBLE | - | `0.0` | 简单移动平均-N=10 |
| `ma_bfq_20` | DOUBLE | - | `0.0` | 简单移动平均-N=20 |
| `ma_bfq_250` | DOUBLE | - | `0.0` | 简单移动平均-N=250 |
| `ma_bfq_30` | DOUBLE | - | `0.0` | 简单移动平均-N=30 |
| `ma_bfq_5` | DOUBLE | - | `0.0` | 简单移动平均-N=5 |
| `ma_bfq_60` | DOUBLE | - | `0.0` | 简单移动平均-N=60 |
| `ma_bfq_90` | DOUBLE | - | `0.0` | 简单移动平均-N=90 |
| `ma_hfq_10` | DOUBLE | - | `0.0` | 简单移动平均-N=10 |
| `ma_hfq_20` | DOUBLE | - | `0.0` | 简单移动平均-N=20 |
| `ma_hfq_250` | DOUBLE | - | `0.0` | 简单移动平均-N=250 |
| `ma_hfq_30` | DOUBLE | - | `0.0` | 简单移动平均-N=30 |
| `ma_hfq_5` | DOUBLE | - | `0.0` | 简单移动平均-N=5 |
| `ma_hfq_60` | DOUBLE | - | `0.0` | 简单移动平均-N=60 |
| `ma_hfq_90` | DOUBLE | - | `0.0` | 简单移动平均-N=90 |
| `ma_qfq_10` | DOUBLE | - | `0.0` | 简单移动平均-N=10 |
| `ma_qfq_20` | DOUBLE | - | `0.0` | 简单移动平均-N=20 |
| `ma_qfq_250` | DOUBLE | - | `0.0` | 简单移动平均-N=250 |
| `ma_qfq_30` | DOUBLE | - | `0.0` | 简单移动平均-N=30 |
| `ma_qfq_5` | DOUBLE | - | `0.0` | 简单移动平均-N=5 |
| `ma_qfq_60` | DOUBLE | - | `0.0` | 简单移动平均-N=60 |
| `ma_qfq_90` | DOUBLE | - | `0.0` | 简单移动平均-N=90 |
| `macd_bfq` | DOUBLE | - | `0.0` | MACD指标-CLOSE, SHORT=12, LONG=26, M=9 |
| `macd_hfq` | DOUBLE | - | `0.0` | MACD指标-CLOSE, SHORT=12, LONG=26, M=9 |
| `macd_qfq` | DOUBLE | - | `0.0` | MACD指标-CLOSE, SHORT=12, LONG=26, M=9 |
| `macd_dea_bfq` | DOUBLE | - | `0.0` | MACD指标-CLOSE, SHORT=12, LONG=26, M=9 |
| `macd_dea_hfq` | DOUBLE | - | `0.0` | MACD指标-CLOSE, SHORT=12, LONG=26, M=9 |
| `macd_dea_qfq` | DOUBLE | - | `0.0` | MACD指标-CLOSE, SHORT=12, LONG=26, M=9 |
| `macd_dif_bfq` | DOUBLE | - | `0.0` | MACD指标-CLOSE, SHORT=12, LONG=26, M=9 |
| `macd_dif_hfq` | DOUBLE | - | `0.0` | MACD指标-CLOSE, SHORT=12, LONG=26, M=9 |
| `macd_dif_qfq` | DOUBLE | - | `0.0` | MACD指标-CLOSE, SHORT=12, LONG=26, M=9 |
| `mass_bfq` | DOUBLE | - | `0.0` | 梅斯线-HIGH, LOW, N1=9, N2=25, M=6 |
| `mass_hfq` | DOUBLE | - | `0.0` | 梅斯线-HIGH, LOW, N1=9, N2=25, M=6 |
| `mass_qfq` | DOUBLE | - | `0.0` | 梅斯线-HIGH, LOW, N1=9, N2=25, M=6 |
| `ma_mass_bfq` | DOUBLE | - | `0.0` | 梅斯线-HIGH, LOW, N1=9, N2=25, M=6 |
| `ma_mass_hfq` | DOUBLE | - | `0.0` | 梅斯线-HIGH, LOW, N1=9, N2=25, M=6 |
| `ma_mass_qfq` | DOUBLE | - | `0.0` | 梅斯线-HIGH, LOW, N1=9, N2=25, M=6 |
| `mfi_bfq` | DOUBLE | - | `0.0` | MFI指标是成交量的RSI指标-CLOSE, HIGH, LOW, VOL, N=14 |
| `mfi_hfq` | DOUBLE | - | `0.0` | MFI指标是成交量的RSI指标-CLOSE, HIGH, LOW, VOL, N=14 |
| `mfi_qfq` | DOUBLE | - | `0.0` | MFI指标是成交量的RSI指标-CLOSE, HIGH, LOW, VOL, N=14 |
| `mtm_bfq` | DOUBLE | - | `0.0` | 动量指标-CLOSE, N=12, M=6 |
| `mtm_hfq` | DOUBLE | - | `0.0` | 动量指标-CLOSE, N=12, M=6 |
| `mtm_qfq` | DOUBLE | - | `0.0` | 动量指标-CLOSE, N=12, M=6 |
| `mtmma_bfq` | DOUBLE | - | `0.0` | 动量指标-CLOSE, N=12, M=6 |
| `mtmma_hfq` | DOUBLE | - | `0.0` | 动量指标-CLOSE, N=12, M=6 |
| `mtmma_qfq` | DOUBLE | - | `0.0` | 动量指标-CLOSE, N=12, M=6 |
| `obv_bfq` | DOUBLE | - | `0.0` | 能量潮指标-CLOSE, VOL |
| `obv_hfq` | DOUBLE | - | `0.0` | 能量潮指标-CLOSE, VOL |
| `obv_qfq` | DOUBLE | - | `0.0` | 能量潮指标-CLOSE, VOL |
| `psy_bfq` | DOUBLE | - | `0.0` | 投资者对股市涨跌产生心理波动的情绪指标-CLOSE, N=12, M=6 |
| `psy_hfq` | DOUBLE | - | `0.0` | 投资者对股市涨跌产生心理波动的情绪指标-CLOSE, N=12, M=6 |
| `psy_qfq` | DOUBLE | - | `0.0` | 投资者对股市涨跌产生心理波动的情绪指标-CLOSE, N=12, M=6 |
| `psyma_bfq` | DOUBLE | - | `0.0` | 投资者对股市涨跌产生心理波动的情绪指标-CLOSE, N=12, M=6 |
| `psyma_hfq` | DOUBLE | - | `0.0` | 投资者对股市涨跌产生心理波动的情绪指标-CLOSE, N=12, M=6 |
| `psyma_qfq` | DOUBLE | - | `0.0` | 投资者对股市涨跌产生心理波动的情绪指标-CLOSE, N=12, M=6 |
| `roc_bfq` | DOUBLE | - | `0.0` | 变动率指标-CLOSE, N=12, M=6 |
| `roc_hfq` | DOUBLE | - | `0.0` | 变动率指标-CLOSE, N=12, M=6 |
| `roc_qfq` | DOUBLE | - | `0.0` | 变动率指标-CLOSE, N=12, M=6 |
| `maroc_bfq` | DOUBLE | - | `0.0` | 变动率指标-CLOSE, N=12, M=6 |
| `maroc_hfq` | DOUBLE | - | `0.0` | 变动率指标-CLOSE, N=12, M=6 |
| `maroc_qfq` | DOUBLE | - | `0.0` | 变动率指标-CLOSE, N=12, M=6 |
| `rsi_bfq_12` | DOUBLE | - | `0.0` | RSI指标-CLOSE, N=12 |
| `rsi_bfq_24` | DOUBLE | - | `0.0` | RSI指标-CLOSE, N=24 |
| `rsi_bfq_6` | DOUBLE | - | `0.0` | RSI指标-CLOSE, N=6 |
| `rsi_hfq_12` | DOUBLE | - | `0.0` | RSI指标-CLOSE, N=12 |
| `rsi_hfq_24` | DOUBLE | - | `0.0` | RSI指标-CLOSE, N=24 |
| `rsi_hfq_6` | DOUBLE | - | `0.0` | RSI指标-CLOSE, N=6 |
| `rsi_qfq_12` | DOUBLE | - | `0.0` | RSI指标-CLOSE, N=12 |
| `rsi_qfq_24` | DOUBLE | - | `0.0` | RSI指标-CLOSE, N=24 |
| `rsi_qfq_6` | DOUBLE | - | `0.0` | RSI指标-CLOSE, N=6 |
| `taq_down_bfq` | DOUBLE | - | `0.0` | 唐安奇通道(海龟)交易指标-HIGH, LOW, 20 |
| `taq_down_hfq` | DOUBLE | - | `0.0` | 唐安奇通道(海龟)交易指标-HIGH, LOW, 20 |
| `taq_down_qfq` | DOUBLE | - | `0.0` | 唐安奇通道(海龟)交易指标-HIGH, LOW, 20 |
| `taq_mid_bfq` | DOUBLE | - | `0.0` | 唐安奇通道(海龟)交易指标-HIGH, LOW, 20 |
| `taq_mid_hfq` | DOUBLE | - | `0.0` | 唐安奇通道(海龟)交易指标-HIGH, LOW, 20 |
| `taq_mid_qfq` | DOUBLE | - | `0.0` | 唐安奇通道(海龟)交易指标-HIGH, LOW, 20 |
| `taq_up_bfq` | DOUBLE | - | `0.0` | 唐安奇通道(海龟)交易指标-HIGH, LOW, 20 |
| `taq_up_hfq` | DOUBLE | - | `0.0` | 唐安奇通道(海龟)交易指标-HIGH, LOW, 20 |
| `taq_up_qfq` | DOUBLE | - | `0.0` | 唐安奇通道(海龟)交易指标-HIGH, LOW, 20 |
| `trix_bfq` | DOUBLE | - | `0.0` | 三重指数平滑平均线-CLOSE, M1=12, M2=20 |
| `trix_hfq` | DOUBLE | - | `0.0` | 三重指数平滑平均线-CLOSE, M1=12, M2=20 |
| `trix_qfq` | DOUBLE | - | `0.0` | 三重指数平滑平均线-CLOSE, M1=12, M2=20 |
| `trma_bfq` | DOUBLE | - | `0.0` | 三重指数平滑平均线-CLOSE, M1=12, M2=20 |
| `trma_hfq` | DOUBLE | - | `0.0` | 三重指数平滑平均线-CLOSE, M1=12, M2=20 |
| `trma_qfq` | DOUBLE | - | `0.0` | 三重指数平滑平均线-CLOSE, M1=12, M2=20 |
| `vr_bfq` | DOUBLE | - | `0.0` | VR容量比率-CLOSE, VOL, M1=26 |
| `vr_hfq` | DOUBLE | - | `0.0` | VR容量比率-CLOSE, VOL, M1=26 |
| `vr_qfq` | DOUBLE | - | `0.0` | VR容量比率-CLOSE, VOL, M1=26 |
| `wr_bfq` | DOUBLE | - | `0.0` | W&R 威廉指标-CLOSE, HIGH, LOW, N=10, N1=6 |
| `wr_hfq` | DOUBLE | - | `0.0` | W&R 威廉指标-CLOSE, HIGH, LOW, N=10, N1=6 |
| `wr_qfq` | DOUBLE | - | `0.0` | W&R 威廉指标-CLOSE, HIGH, LOW, N=10, N1=6 |
| `wr1_bfq` | DOUBLE | - | `0.0` | W&R 威廉指标-CLOSE, HIGH, LOW, N=10, N1=6 |
| `wr1_hfq` | DOUBLE | - | `0.0` | W&R 威廉指标-CLOSE, HIGH, LOW, N=10, N1=6 |
| `wr1_qfq` | DOUBLE | - | `0.0` | W&R 威廉指标-CLOSE, HIGH, LOW, N=10, N1=6 |
| `xsii_td1_bfq` | DOUBLE | - | `0.0` | 薛斯通道II-CLOSE, HIGH, LOW, N=102, M=7 |
| `xsii_td1_hfq` | DOUBLE | - | `0.0` | 薛斯通道II-CLOSE, HIGH, LOW, N=102, M=7 |
| `xsii_td1_qfq` | DOUBLE | - | `0.0` | 薛斯通道II-CLOSE, HIGH, LOW, N=102, M=7 |
| `xsii_td2_bfq` | DOUBLE | - | `0.0` | 薛斯通道II-CLOSE, HIGH, LOW, N=102, M=7 |
| `xsii_td2_hfq` | DOUBLE | - | `0.0` | 薛斯通道II-CLOSE, HIGH, LOW, N=102, M=7 |
| `xsii_td2_qfq` | DOUBLE | - | `0.0` | 薛斯通道II-CLOSE, HIGH, LOW, N=102, M=7 |
| `xsii_td3_bfq` | DOUBLE | - | `0.0` | 薛斯通道II-CLOSE, HIGH, LOW, N=102, M=7 |
| `xsii_td3_hfq` | DOUBLE | - | `0.0` | 薛斯通道II-CLOSE, HIGH, LOW, N=102, M=7 |
| `xsii_td3_qfq` | DOUBLE | - | `0.0` | 薛斯通道II-CLOSE, HIGH, LOW, N=102, M=7 |
| `xsii_td4_bfq` | DOUBLE | - | `0.0` | 薛斯通道II-CLOSE, HIGH, LOW, N=102, M=7 |
| `xsii_td4_hfq` | DOUBLE | - | `0.0` | 薛斯通道II-CLOSE, HIGH, LOW, N=102, M=7 |
| `xsii_td4_qfq` | DOUBLE | - | `0.0` | 薛斯通道II-CLOSE, HIGH, LOW, N=102, M=7 |

---

## 指数-基础信息 {#指数-基础信息}

本分类共包含 **1** 个数据表。

### 表列表

- [index_basic](#index-basic) - 指数基本信息

### index_basic

**表名**: `index_basic` | **说明**: 指数基本信息 | **主键**: `ts_code`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | TS代码 |
| `name` | VARCHAR(255) | 255 | `` | 简称 |
| `fullname` | VARCHAR(255) | 255 | `` | 指数全称 |
| `market` | VARCHAR(255) | 255 | `` | 市场 |
| `publisher` | VARCHAR(255) | 255 | `` | 发布方 |
| `index_type` | VARCHAR(255) | 255 | `` | 指数风格 |
| `category` | VARCHAR(255) | 255 | `` | 指数类别 |
| `base_date` | DATE | - | `1970-01-01` | 基期 |
| `base_point` | DOUBLE | - | `0.0` | 基点 |
| `list_date` | DATE | - | `1970-01-01` | 发布日期 |
| `weight_rule` | VARCHAR(255) | 255 | `` | 加权方式 |
| `desc` | VARCHAR(255) | 255 | `` | 描述 |
| `exp_date` | DATE | - | `1970-01-01` | 终止日期 |

---

## 指数-行情数据 {#指数-行情数据}

本分类共包含 **8** 个数据表。

### 表列表

- [index_daily](#index-daily) - 指数日线行情
- [index_weight](#index-weight) - 指数成分和权重
- [index_dailybasic](#index-dailybasic) - 大盘指数每日指标
- [index_weekly](#index-weekly) - 指数周线行情
- [index_monthly](#index-monthly) - 指数月线行情
- [index_global](#index-global) - 国际指数
- [daily_info](#daily-info) - 市场交易统计
- [sz_daily_info](#sz-daily-info) - 深圳市场每日交易概况

### index_daily

**表名**: `index_daily` | **说明**: 指数日线行情 | **主键**: `ts_code`, `trade_date` | **依赖表**: `index/basic/index_basic`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | 无说明 |
| `trade_date` | DATE | - | `1970-01-01` | 无说明 |
| `close` | DOUBLE | - | `0.0` | 无说明 |
| `open` | DOUBLE | - | `0.0` | 无说明 |
| `high` | DOUBLE | - | `0.0` | 无说明 |
| `low` | DOUBLE | - | `0.0` | 无说明 |
| `pre_close` | DOUBLE | - | `0.0` | 无说明 |
| `change` | DOUBLE | - | `0.0` | 无说明 |
| `pct_chg` | DOUBLE | - | `0.0` | 无说明 |
| `vol` | DOUBLE | - | `0.0` | 无说明 |
| `amount` | DOUBLE | - | `0.0` | 无说明 |

---

### index_weight

**表名**: `index_weight` | **说明**: 指数成分和权重 | **主键**: `index_code`, `con_code`, `trade_date`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `index_code` | VARCHAR(255) | 255 | `` | 指数代码 |
| `con_code` | VARCHAR(255) | 255 | `` | 成分代码 |
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `weight` | DOUBLE | - | `0.0` | 权重 |

---

### index_dailybasic

**表名**: `index_dailybasic` | **说明**: 大盘指数每日指标 | **主键**: `ts_code`, `trade_date`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | TS代码 |
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `total_mv` | DOUBLE | - | `0.0` | 当日总市值 |
| `float_mv` | DOUBLE | - | `0.0` | 当日流通市值 |
| `total_share` | DOUBLE | - | `0.0` | 当日总股本 |
| `float_share` | DOUBLE | - | `0.0` | 当日流通股本 |
| `free_share` | DOUBLE | - | `0.0` | 当日自由流通股本 |
| `turnover_rate` | DOUBLE | - | `0.0` | 换手率 |
| `turnover_rate_f` | DOUBLE | - | `0.0` | 换手率(自由流通股本) |
| `pe` | DOUBLE | - | `0.0` | 市盈率 |
| `pe_ttm` | DOUBLE | - | `0.0` | 市盈率TTM |
| `pb` | DOUBLE | - | `0.0` | 市净率 |

---

### index_weekly

**表名**: `index_weekly` | **说明**: 指数周线行情 | **主键**: `ts_code`, `trade_date`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | TS指数代码 |
| `trade_date` | DATE | - | `1970-01-01` | 交易日 |
| `close` | DOUBLE | - | `0.0` | 收盘点位 |
| `open` | DOUBLE | - | `0.0` | 开盘点位 |
| `high` | DOUBLE | - | `0.0` | 最高点位 |
| `low` | DOUBLE | - | `0.0` | 最低点位 |
| `pre_close` | DOUBLE | - | `0.0` | 昨日收盘点 |
| `change` | DOUBLE | - | `0.0` | 涨跌点位 |
| `pct_chg` | DOUBLE | - | `0.0` | 涨跌幅 |
| `vol` | DOUBLE | - | `0.0` | 成交量 |
| `amount` | DOUBLE | - | `0.0` | 成交额 |

---

### index_monthly

**表名**: `index_monthly` | **说明**: 指数月线行情 | **主键**: `ts_code`, `trade_date`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | TS指数代码 |
| `trade_date` | DATE | - | `1970-01-01` | 交易日 |
| `close` | DOUBLE | - | `0.0` | 收盘点位 |
| `open` | DOUBLE | - | `0.0` | 开盘点位 |
| `high` | DOUBLE | - | `0.0` | 最高点位 |
| `low` | DOUBLE | - | `0.0` | 最低点位 |
| `pre_close` | DOUBLE | - | `0.0` | 昨日收盘点 |
| `change` | DOUBLE | - | `0.0` | 涨跌点位 |
| `pct_chg` | DOUBLE | - | `0.0` | 涨跌幅 |
| `vol` | DOUBLE | - | `0.0` | 成交量 |
| `amount` | DOUBLE | - | `0.0` | 成交额 |

---

### index_global

**表名**: `index_global` | **说明**: 国际指数 | **主键**: `ts_code`, `trade_date`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | TS指数代码 |
| `trade_date` | DATE | - | `1970-01-01` | 交易日 |
| `open` | DOUBLE | - | `0.0` | 开盘点位 |
| `close` | DOUBLE | - | `0.0` | 收盘点位 |
| `high` | DOUBLE | - | `0.0` | 最高点位 |
| `low` | DOUBLE | - | `0.0` | 最低点位 |
| `pre_close` | DOUBLE | - | `0.0` | 昨日收盘点 |
| `change` | DOUBLE | - | `0.0` | 涨跌点位 |
| `pct_chg` | DOUBLE | - | `0.0` | 涨跌幅 |
| `swing` | DOUBLE | - | `0.0` | 振幅 |
| `vol` | DOUBLE | - | `0.0` | 成交量 |
| `amount` | DOUBLE | - | `0.0` | 成交额 |

---

### daily_info

**表名**: `daily_info` | **说明**: 市场交易统计 | **主键**: `ts_code`, `trade_date`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `ts_code` | VARCHAR(16) | 16 | `` | 市场代码 |
| `ts_name` | VARCHAR(255) | 255 | `` | 市场名称 |
| `com_count` | INTEGER | - | `0` | 挂牌数 |
| `total_share` | DOUBLE | - | `0.0` | 总股本（亿股） |
| `float_share` | DOUBLE | - | `0.0` | 流通股本（亿股） |
| `total_mv` | DOUBLE | - | `0.0` | 总市值（亿元） |
| `float_mv` | DOUBLE | - | `0.0` | 流通市值（亿元） |
| `amount` | DOUBLE | - | `0.0` | 交易金额（亿元） |
| `vol` | DOUBLE | - | `0.0` | 成交量（亿股） |
| `trans_count` | INTEGER | - | `0` | 成交笔数（万笔） |
| `pe` | DOUBLE | - | `0.0` | 平均市盈率 |
| `tr` | DOUBLE | - | `0.0` | 换手率（％） |
| `exchange` | VARCHAR(255) | 255 | `` | 交易所 |

---

### sz_daily_info

**表名**: `sz_daily_info` | **说明**: 深圳市场每日交易概况 | **主键**: `ts_code`, `trade_date`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `trade_date` | DATE | - | `1970-01-01` | 无说明 |
| `ts_code` | VARCHAR(16) | 16 | `` | 市场类型 |
| `count` | INTEGER | - | `0` | 股票个数 |
| `amount` | DOUBLE | - | `0.0` | 成交金额 |
| `vol` | DOUBLE | - | `0.0` | 成交量 |
| `total_share` | DOUBLE | - | `0.0` | 总股本 |
| `total_mv` | DOUBLE | - | `0.0` | 总市值 |
| `float_share` | DOUBLE | - | `0.0` | 流通股票 |
| `float_mv` | DOUBLE | - | `0.0` | 流通市值 |

---

## 指数-SW分类 {#指数-sw分类}

本分类共包含 **4** 个数据表。

### 表列表

- [sw_daily](#sw-daily) - 申万行业日线行情
- [index_classify](#index-classify) - 申万行业分类
- [index_member](#index-member) - 申万行业成分构成
- [index_member_all](#index-member-all) - 申万行业成分构成

### sw_daily

**表名**: `sw_daily` | **说明**: 申万行业日线行情 | **主键**: `ts_code`, `trade_date`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | 指数代码 |
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `name` | VARCHAR(255) | 255 | `` | 指数名称 |
| `open` | DOUBLE | - | `0.0` | 开盘点位 |
| `low` | DOUBLE | - | `0.0` | 最低点位 |
| `high` | DOUBLE | - | `0.0` | 最高点位 |
| `close` | DOUBLE | - | `0.0` | 收盘点位 |
| `change` | DOUBLE | - | `0.0` | 涨跌点位 |
| `pct_change` | DOUBLE | - | `0.0` | 涨跌幅 |
| `vol` | DOUBLE | - | `0.0` | 成交量（万股） |
| `amount` | DOUBLE | - | `0.0` | 成交额（万元） |
| `pe` | DOUBLE | - | `0.0` | 市盈率 |
| `pb` | DOUBLE | - | `0.0` | 市净率 |
| `float_mv` | DOUBLE | - | `0.0` | 流通市值（万元） |
| `total_mv` | DOUBLE | - | `0.0` | 总市值（万元） |
| `weight` | DOUBLE | - | `0.0` | 权重 |

---

### index_classify

**表名**: `index_classify` | **说明**: 申万行业分类 | **主键**: `index_code`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `index_code` | VARCHAR(255) | 255 | `` | 指数代码 |
| `industry_name` | VARCHAR(255) | 255 | `` | 行业名称 |
| `level` | VARCHAR(255) | 255 | `` | 行业名称 |
| `industry_code` | VARCHAR(255) | 255 | `` | 行业代码 |
| `is_pub` | VARCHAR(255) | 255 | `` | 是否发布指数 |
| `parent_code` | VARCHAR(255) | 255 | `` | 父级代码 |
| `src` | VARCHAR(255) | 255 | `` | 行业分类（SW申万） |

---

### index_member

**表名**: `index_member` | **说明**: 申万行业成分构成 | **主键**: `index_code`, `is_new`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `index_code` | VARCHAR(255) | 255 | `` | 指数代码 |
| `index_name` | VARCHAR(255) | 255 | `` | 指数名称 |
| `con_code` | VARCHAR(255) | 255 | `` | 成分股票代码 |
| `con_name` | VARCHAR(255) | 255 | `` | 成分股票名称 |
| `in_date` | DATE | - | `1970-01-01` | 纳入日期 |
| `out_date` | DATE | - | `1970-01-01` | 剔除日期 |
| `is_new` | VARCHAR(255) | 255 | `` | 是否最新Y是N否 |

---

### index_member_all

**表名**: `index_member_all` | **说明**: 申万行业成分构成 | **主键**: `l1_code`, `l2_code`, `l3_code`, `ts_code`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `l1_code` | VARCHAR(255) | 255 | `` | L1代码 |
| `l1_name` | VARCHAR(255) | 255 | `` | L1名称 |
| `l2_code` | VARCHAR(255) | 255 | `` | L2代码 |
| `l2_name` | VARCHAR(255) | 255 | `` | L2名称 |
| `l3_code` | VARCHAR(255) | 255 | `` | L3代码 |
| `l3_name` | VARCHAR(255) | 255 | `` | L3名称 |
| `ts_code` | VARCHAR(16) | 16 | `` | 成分股票代码 |
| `name` | VARCHAR(255) | 255 | `` | 成分股票名称 |
| `in_date` | DATE | - | `1970-01-01` | 纳入日期 |
| `out_date` | DATE | - | `1970-01-01` | 剔除日期 |
| `is_new` | VARCHAR(255) | 255 | `` | 是否最新Y是N否 |

---

## 指数-同花顺 {#指数-同花顺}

本分类共包含 **3** 个数据表。

### 表列表

- [ths_index](#ths-index) - 同花顺板块指数
- [ths_daily](#ths-daily) - 同花顺板块指数行情
- [ths_member](#ths-member) - 同花顺概念板块成分

### ths_index

**表名**: `ths_index` | **说明**: 同花顺板块指数 | **主键**: `ts_code`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | 代码 |
| `name` | VARCHAR(255) | 255 | `` | 名称 |
| `count` | INTEGER | - | `0` | 成分个数 |
| `exchange` | VARCHAR(255) | 255 | `` | 交易所 |
| `list_date` | DATE | - | `1970-01-01` | 上市日期 |
| `type` | VARCHAR(255) | 255 | `` | N概念指数S特色指数 |

---

### ths_daily

**表名**: `ths_daily` | **说明**: 同花顺板块指数行情 | **主键**: `ts_code`, `trade_date`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | TS指数代码 |
| `trade_date` | DATE | - | `1970-01-01` | 交易日 |
| `close` | DOUBLE | - | `0.0` | 收盘点位 |
| `open` | DOUBLE | - | `0.0` | 开盘点位 |
| `high` | DOUBLE | - | `0.0` | 最高点位 |
| `low` | DOUBLE | - | `0.0` | 最低点位 |
| `pre_close` | DOUBLE | - | `0.0` | 昨日收盘点 |
| `avg_price` | DOUBLE | - | `0.0` | 平均点位 |
| `change` | DOUBLE | - | `0.0` | 涨跌点位 |
| `pct_change` | DOUBLE | - | `0.0` | 涨跌幅 |
| `vol` | DOUBLE | - | `0.0` | 成交量 |
| `turnover_rate` | DOUBLE | - | `0.0` | 换手率 |
| `total_mv` | DOUBLE | - | `0.0` | 总市值 |
| `float_mv` | DOUBLE | - | `0.0` | 流通市值 |
| `pe_ttm` | DOUBLE | - | `0.0` | PE TTM |
| `pb_mrq` | DOUBLE | - | `0.0` | PB MRQ |

---

### ths_member

**表名**: `ths_member` | **说明**: 同花顺概念板块成分 | **主键**: `ts_code`, `code`, `is_new`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | 指数代码 |
| `code` | VARCHAR(255) | 255 | `` | 股票代码 |
| `name` | VARCHAR(255) | 255 | `` | 股票名称 |
| `weight` | DOUBLE | - | `0.0` | 权重 |
| `in_date` | DATE | - | `1970-01-01` | 纳入日期 |
| `out_date` | DATE | - | `1970-01-01` | 剔除日期 |
| `is_new` | VARCHAR(255) | 255 | `` | 是否最新Y是N否 |

---

## 指数-中信 {#指数-中信}

本分类共包含 **1** 个数据表。

### 表列表

- [ci_daily](#ci-daily) - 中信行业指数行情

### ci_daily

**表名**: `ci_daily` | **说明**: 中信行业指数行情 | **主键**: `ts_code`, `trade_date`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | 指数代码 |
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `open` | DOUBLE | - | `0.0` | 开盘点位 |
| `low` | DOUBLE | - | `0.0` | 最低点位 |
| `high` | DOUBLE | - | `0.0` | 最高点位 |
| `close` | DOUBLE | - | `0.0` | 收盘点位 |
| `pre_close` | DOUBLE | - | `0.0` | 昨日收盘点位 |
| `change` | DOUBLE | - | `0.0` | 涨跌点位 |
| `pct_change` | DOUBLE | - | `0.0` | 涨跌幅 |
| `vol` | DOUBLE | - | `0.0` | 成交量（万股） |
| `amount` | DOUBLE | - | `0.0` | 成交额（万元） |

---

## 期货-基础信息 {#期货-基础信息}

本分类共包含 **1** 个数据表。

### 表列表

- [fut_basic](#fut-basic) - 期货合约信息表

### fut_basic

**表名**: `fut_basic` | **说明**: 期货合约信息表 | **主键**: `ts_code`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | 无说明 |
| `symbol` | VARCHAR(255) | 255 | `` | 交易代码 |
| `exchange` | VARCHAR(255) | 255 | `` | 交易市场 |
| `name` | VARCHAR(255) | 255 | `` | 中文简称 |
| `fut_code` | VARCHAR(255) | 255 | `` | 合约产品代码 |
| `multiplier` | DOUBLE | - | `0.0` | 合约乘数 |
| `trade_unit` | VARCHAR(255) | 255 | `` | 交易计量单位 |
| `per_unit` | DOUBLE | - | `0.0` | 交易单位(每手) |
| `quote_unit` | VARCHAR(255) | 255 | `` | 报价单位 |
| `quote_unit_desc` | VARCHAR(255) | 255 | `` | 最小报价单位说明 |
| `d_mode_desc` | VARCHAR(255) | 255 | `` | 交割方式说明 |
| `list_date` | DATE | - | `1970-01-01` | 上市日期 |
| `delist_date` | DATE | - | `1970-01-01` | 最后交易日期 |
| `d_month` | VARCHAR(255) | 255 | `` | 交割月份 |
| `last_ddate` | DATE | - | `1970-01-01` | 最后交割日 |
| `trade_time_desc` | VARCHAR(255) | 255 | `` | 交易时间说明 |

---

## 期货-行情数据 {#期货-行情数据}

本分类共包含 **6** 个数据表。

### 表列表

- [fut_daily](#fut-daily) - 期货日线行情
- [fut_holding](#fut-holding) - 每日成交持仓排名
- [fut_wsr](#fut-wsr) - 仓单日报
- [fut_settle](#fut-settle) - 结算参数
- [fut_mapping](#fut-mapping) - 期货主力与连续合约
- [fut_weekly_detail](#fut-weekly-detail) - 期货主要品种交易周报

### fut_daily

**表名**: `fut_daily` | **说明**: 期货日线行情 | **主键**: `ts_code`, `trade_date`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | TS代码 |
| `trade_date` | DATE | - | `1970-01-01` | 交易代码 |
| `pre_close` | DOUBLE | - | `0.0` | 昨收盘价 |
| `pre_settle` | DOUBLE | - | `0.0` | 昨结算价 |
| `open` | DOUBLE | - | `0.0` | 开盘价 |
| `high` | DOUBLE | - | `0.0` | 最高价 |
| `low` | DOUBLE | - | `0.0` | 最低价 |
| `close` | DOUBLE | - | `0.0` | 收盘价 |
| `settle` | DOUBLE | - | `0.0` | 结算价 |
| `change1` | DOUBLE | - | `0.0` | 涨跌1,收盘价-昨结算价 |
| `change2` | DOUBLE | - | `0.0` | 涨跌2,结算价-昨结算价 |
| `vol` | DOUBLE | - | `0.0` | 成交量(手) |
| `amount` | DOUBLE | - | `0.0` | 成交金额(万元) |
| `oi` | DOUBLE | - | `0.0` | 持仓量(手) |
| `oi_chg` | DOUBLE | - | `0.0` | 持仓量变化 |
| `delv_settle` | DOUBLE | - | `0.0` | 交割结算价 |

---

### fut_holding

**表名**: `fut_holding` | **说明**: 每日成交持仓排名 | **主键**: `symbol`, `trade_date`, `broker`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `symbol` | VARCHAR(255) | 255 | `` | 合约代码或类型 |
| `broker` | VARCHAR(255) | 255 | `` | 期货公司会员简称 |
| `vol` | INTEGER | - | `0` | 成交量 |
| `vol_chg` | INTEGER | - | `0` | 成交量变化 |
| `long_hld` | INTEGER | - | `0` | 持买仓量 |
| `long_chg` | INTEGER | - | `0` | 持买仓量变化 |
| `short_hld` | INTEGER | - | `0` | 持卖仓量 |
| `short_chg` | INTEGER | - | `0` | 持卖仓量变化 |
| `exchange` | VARCHAR(255) | 255 | `` | 交易所 |

---

### fut_wsr

**表名**: `fut_wsr` | **说明**: 仓单日报 | **主键**: `symbol`, `trade_date`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `symbol` | VARCHAR(255) | 255 | `` | 产品代码 |
| `fut_name` | VARCHAR(255) | 255 | `` | 产品名称 |
| `warehouse` | VARCHAR(255) | 255 | `` | 仓库名称 |
| `wh_id` | VARCHAR(255) | 255 | `` | 仓库编号 |
| `pre_vol` | INTEGER | - | `0` | 昨日仓单量 |
| `vol` | INTEGER | - | `0` | 今日仓单量 |
| `vol_chg` | INTEGER | - | `0` | 增减量 |
| `area` | VARCHAR(255) | 255 | `` | 地区 |
| `year` | VARCHAR(255) | 255 | `` | 年度 |
| `grade` | VARCHAR(255) | 255 | `` | 等级 |
| `brand` | VARCHAR(255) | 255 | `` | 品牌 |
| `place` | VARCHAR(255) | 255 | `` | 产地 |
| `pd` | INTEGER | - | `0` | 升贴水 |
| `is_ct` | VARCHAR(255) | 255 | `` | 是否折算仓单 |
| `unit` | VARCHAR(255) | 255 | `` | 单位 |
| `exchange` | VARCHAR(255) | 255 | `` | 交易所 |

---

### fut_settle

**表名**: `fut_settle` | **说明**: 结算参数 | **主键**: `ts_code`, `trade_date`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | 合约代码 |
| `trade_date` | DATE | - | `1970-01-01` | 交易日期 |
| `settle` | DOUBLE | - | `0.0` | 结算价 |
| `trading_fee_rate` | DOUBLE | - | `0.0` | 交易手续费率 |
| `trading_fee` | DOUBLE | - | `0.0` | 交易手续费 |
| `delivery_fee` | DOUBLE | - | `0.0` | 交割手续费 |
| `b_hedging_margin_rate` | DOUBLE | - | `0.0` | 买套保交易保证金率 |
| `s_hedging_margin_rate` | DOUBLE | - | `0.0` | 卖套保交易保证金率 |
| `long_margin_rate` | DOUBLE | - | `0.0` | 买投机交易保证金率 |
| `short_margin_rate` | DOUBLE | - | `0.0` | 卖投机交易保证金率 |
| `offset_today_fee` | DOUBLE | - | `0.0` | 平今仓手续率 |
| `exchange` | VARCHAR(255) | 255 | `` | 交易所 |

---

### fut_mapping

**表名**: `fut_mapping` | **说明**: 期货主力与连续合约 | **主键**: `ts_code`, `trade_date`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `ts_code` | VARCHAR(16) | 16 | `` | 连续合约代码 |
| `trade_date` | DATE | - | `1970-01-01` | 起始日期 |
| `mapping_ts_code` | VARCHAR(255) | 255 | `` | 期货合约代码 |

---

### fut_weekly_detail

**表名**: `fut_weekly_detail` | **说明**: 期货主要品种交易周报 | **主键**: `week`, `prd`

**字段列表**:

| 字段名 | 数据类型 | 长度 | 默认值 | 说明 |
|--------|----------|------|--------|------|
| `exchange` | VARCHAR(255) | 255 | `` | 交易所代码 |
| `prd` | VARCHAR(255) | 255 | `` | 期货品种代码 |
| `name` | VARCHAR(255) | 255 | `` | 品种名称 |
| `vol` | INTEGER | - | `0` | 成交量（手） |
| `vol_yoy` | DOUBLE | - | `0.0` | 同比增减（%） |
| `amount` | DOUBLE | - | `0.0` | 成交金额（亿元） |
| `amout_yoy` | DOUBLE | - | `0.0` | 同比增减（%） |
| `cumvol` | INTEGER | - | `0` | 年累计成交总量（手） |
| `cumvol_yoy` | DOUBLE | - | `0.0` | 同比增减（%） |
| `cumamt` | DOUBLE | - | `0.0` | 年累计成交金额（亿元） |
| `cumamt_yoy` | DOUBLE | - | `0.0` | 同比增减（%） |
| `open_interest` | INTEGER | - | `0` | 持仓量（手） |
| `interest_wow` | DOUBLE | - | `0.0` | 环比增减（%） |
| `mc_close` | DOUBLE | - | `0.0` | 本周主力合约收盘价 |
| `close_wow` | DOUBLE | - | `0.0` | 环比涨跌（%） |
| `week` | VARCHAR(255) | 255 | `` | 周期 |
| `week_date` | DATE | - | `1970-01-01` | 周日期 |

---

## 统计信息

- **总表数**: 113
- **生成时间**: 2025-11-05 22:44:49
