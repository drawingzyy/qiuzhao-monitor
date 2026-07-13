"""PushPlus 微信推送通知器。

API 文档: https://www.pushplus.plus/doc/guide/api.html
"""

from loguru import logger

import httpx

from qiuzhao.notifiers.base import BaseNotifier
from qiuzhao.config import PUSHPLUS_TOKEN


class PushPlusNotifier(BaseNotifier):
    """通过 PushPlus 推送到个人微信。"""

    API_URL = "http://www.pushplus.plus/send"

    def __init__(self, token: str | None = None):
        self.token = token or PUSHPLUS_TOKEN

    async def send(self, title: str, content: str) -> bool:
        if not self.token:
            logger.error("PushPlus token 未配置，请在 .env 中设置 PUSHPLUS_TOKEN")
            return False

        payload = {
            "token": self.token,
            "title": title,
            "content": content,
            "template": "markdown",
        }

        try:
            async with httpx.AsyncClient(timeout=15.0) as client:
                resp = await client.post(self.API_URL, json=payload)
                data = resp.json()
                if data.get("code") == 200:
                    logger.info(f"PushPlus 推送成功: {title}")
                    return True
                else:
                    logger.error(f"PushPlus 推送失败: {data}")
                    return False
        except Exception as e:
            logger.error(f"PushPlus 推送异常: {e}")
            return False
