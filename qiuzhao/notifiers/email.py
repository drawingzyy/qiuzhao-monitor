"""邮件推送通知器 — 通过 SMTP 发送邮件。"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from loguru import logger

from qiuzhao.notifiers.base import BaseNotifier
from qiuzhao.config import (
    SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD,
    EMAIL_FROM, EMAIL_TO,
)


class EmailNotifier(BaseNotifier):
    """通过 SMTP 发送邮件通知。"""

    def _markdown_to_html(self, text: str) -> str:
        """简单 Markdown → HTML 转换。"""
        import re

        # 标题
        text = re.sub(r"^### (.*)", r"<h3>\1</h3>", text, flags=re.MULTILINE)
        text = re.sub(r"^## (.*)", r"<h2>\1</h2>", text, flags=re.MULTILINE)
        text = re.sub(r"^# (.*)", r"<h1>\1</h1>", text, flags=re.MULTILINE)

        # 链接: [text](url)
        text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)

        # 粗体
        text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)

        # 分隔线
        text = text.replace("---", "<hr>")

        # 换行
        text = text.replace("\n", "<br>\n")

        return f"""
        <html>
        <body style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
                     max-width: 600px; margin: 0 auto; padding: 20px; line-height: 1.6;">
        {text}
        </body>
        </html>
        """

    async def send(self, title: str, content: str) -> bool:
        if not SMTP_HOST or not SMTP_USER or not SMTP_PASSWORD:
            logger.error("邮件配置不完整，请在 .env 中设置 SMTP_HOST, SMTP_USER, SMTP_PASSWORD")
            return False

        try:
            msg = MIMEMultipart("alternative")
            msg["Subject"] = title
            msg["From"] = EMAIL_FROM or SMTP_USER
            msg["To"] = EMAIL_TO or SMTP_USER

            html_body = self._markdown_to_html(content)
            msg.attach(MIMEText(html_body, "html", "utf-8"))

            # 163 邮箱使用 SSL
            if SMTP_PORT == 465:
                server = smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, timeout=15)
            else:
                server = smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=15)
                server.starttls()

            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(msg["From"], msg["To"], msg.as_string())
            server.quit()

            logger.info(f"邮件发送成功: {title} → {msg['To']}")
            return True

        except Exception as e:
            logger.error(f"邮件发送失败: {e}")
            return False
