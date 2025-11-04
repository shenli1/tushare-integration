#!/usr/bin/env python3
"""
测试飞书Webhook Reporter功能
"""
import sys
import os
import logging

# 尝试加载.env文件（如果存在）
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # 如果没有python-dotenv，尝试手动读取.env文件
    if os.path.exists('.env'):
        with open('.env', 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key.strip()] = value.strip()

# 设置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def test_feishu_reporter():
    """测试飞书Webhook Reporter"""
    from tushare_integration.reporters import FeishuWebHookReporter
    
    # 从环境变量或直接输入获取webhook URL
    webhook = os.environ.get('FEISHU_WEBHOOK', '')
    
    if not webhook:
        webhook = input("请输入飞书Webhook URL（或在.env文件中设置FEISHU_WEBHOOK）: ").strip()
        if not webhook:
            logger.error("未提供飞书Webhook URL，无法测试")
            logger.info("提示：可以在项目根目录创建.env文件，添加：FEISHU_WEBHOOK=your_webhook_url")
            return False
    
    logger.info(f"使用Webhook URL: {webhook[:50]}...")
    
    # 创建reporter实例
    reporter = FeishuWebHookReporter(webhook=webhook)
    
    # 测试发送报告
    test_subject = "测试报告 - Tushare Integration"
    test_content = """这是一个测试报告
测试内容：
- 测试项目1：成功
- 测试项目2：成功
- 测试项目3：成功

测试时间：2025-11-04
"""
    
    try:
        logger.info("开始发送测试报告...")
        reporter.send_report(subject=test_subject, content=test_content)
        logger.info("测试报告发送成功！")
        return True
    except Exception as e:
        logger.error(f"发送测试报告失败: {e}")
        logger.exception("详细错误信息:")
        return False

if __name__ == '__main__':
    success = test_feishu_reporter()
    sys.exit(0 if success else 1)

