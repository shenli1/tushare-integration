import importlib
import logging
import os

import requests


class Reporter(object):
    def send_report(self, subject: str, content: str, *args, **kwargs):
        raise NotImplementedError


class FeishuWebHookReporter(Reporter):
    def __init__(self, webhook: str, *args, **kwargs):
        self.webhook = webhook
        super(FeishuWebHookReporter, self).__init__(*args, **kwargs)

    def send_report(self, subject: str, content: str, *args, **kwargs):
        if not self.webhook:
            logging.info('No feishu webhook, skip send report')
            return

        # 将content按照\n分割，构建消息内容
        content_lines = []
        for line in content.split('\n'):
            if line.strip():  # 跳过空行
                content_lines.append([{"text": line, "tag": "text"}])
        
        body = {
            "msg_type": "post",
            "content": {
                "post": {
                    "zh_cn": {
                        "title": subject,
                        "content": content_lines,
                    }
                }
            },
        }

        try:
            resp = requests.post(self.webhook, json=body, timeout=10)
            resp.raise_for_status()
            logging.info(f'发送报告到飞书Webhook成功，状态码: {resp.status_code}')
            return True
        except requests.exceptions.RequestException as e:
            logging.error(f'发送报告到飞书Webhook失败: {e}')
            if hasattr(e, 'response') and e.response is not None:
                logging.error(f'响应内容: {e.response.text}')
            return False

    @classmethod
    def from_settings(cls, settings):
        # 优先从环境变量读取FEISHU_WEBHOOK，支持从.env文件读取
        webhook = os.environ.get('FEISHU_WEBHOOK', '') or settings.get('FEISHU_WEBHOOK', '')
        return cls(webhook=webhook)


class ReporterLoader(object):
    def __init__(self, settings: dict):
        self.settings = settings
        self.reporters = settings.get('REPORTERS', [])
        logging.info(f'Load reporters: {self.reporters}')

    def get_reporters(self):
        reporters = []
        for reporter in self.reporters:
            package, class_name = reporter.rsplit('.', 1)
            module = importlib.import_module(package)
            cls = getattr(module, class_name)
            reporters.append(cls.from_settings(self.settings))

        return reporters
