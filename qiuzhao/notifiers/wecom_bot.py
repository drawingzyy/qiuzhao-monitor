"""企业微信 Bot 推送通知器。

通过 Webhook 发送 Markdown 消息到企业微信群。
"""

from loguru import logger

import httpx

from qiuzhao.notifiers.base import BaseNotifier
from qiuzhao.config import WECOM_WEBHOOK_URL


class WecomBotNotifier(BaseNotifier):
    """企业微信群机器人推送。"""

    # 企业微信 Markdown 消息上限 4096 字节
    MAX_BYTES = 4000

    def __init__(self, webhook_url: str | None = None):
        self.webhook_url = webhook_url or WECOM_WEBHOOK_URL

    async def send(self, title: str, content: str) -> bool:
        if not self.webhook_url:
            logger.error("企业微信 Webhook URL 未配置")
            return False

        # 企业微信格式：标题 + 内容
        full_content = f"# {title}\n\n{content}"

        # 超长截断
        content_bytes = full_content.encode("utf-8")
        if len(content_bytes) > self.MAX_BYTES:
            full_content = content_bytes[: self.MAX_BYTES].decode("utf-8", errors="ignore")
            full_content += "\n\n...\n> ⚠️ 内容过长已截断"

        payload = {
            "msgtype": "markdown",
            "markdown": {"content": full_content},
        }

        try:
            async with httpx.AsyncClient(timeout=15.0) as client:
                resp = await client.post(self.webhook_url, json=payload)
                data = resp.json()
                if data.get("errcode") == 0:
                    logger.info(f"企业微信推送成功: {title}")
                    return True
                else:
                    logger.error(f"企业微信推送失败: {data}")
                    return False
        except Exception as e:
            logger.error(f"企业微信推送异常: {e}")
            return False
