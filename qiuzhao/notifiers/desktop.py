"""macOS 桌面通知器 — 通过系统通知中心推送，零配置。"""

import subprocess
from loguru import logger

from qiuzhao.notifiers.base import BaseNotifier


class DesktopNotifier(BaseNotifier):
    """使用 macOS osascript 发送系统通知。"""

    async def send(self, title: str, content: str) -> bool:
        # 将 Markdown 内容转成纯文本摘要
        plain_text = _markdown_to_plain(content)

        try:
            script = (
                f'display notification "{_escape(plain_text)}"'
                f' with title "{_escape(title)}"'
                f' sound name "Glass"'
            )
            subprocess.run(
                ["osascript", "-e", script],
                capture_output=True,
                timeout=10,
            )
            logger.info(f"桌面通知已发送: {title}")
            return True
        except Exception as e:
            logger.error(f"桌面通知失败: {e}")
            return False


def _escape(s: str) -> str:
    """转义 AppleScript 字符串中的特殊字符。"""
    return s.replace("\\", "\\\\").replace('"', '\\"')


def _markdown_to_plain(text: str) -> str:
    """简单地将 Markdown 转为纯文本摘要。"""
    # 去掉 Markdown 链接，保留文字
    import re
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    # 去掉 Markdown 格式标记
    text = text.replace("**", "").replace("###", "").replace("🏢", "")
    # 取前几条
    lines = [l.strip() for l in text.split("\n") if l.strip() and not l.strip().startswith("---")]
    # 取前 5 行作为摘要
    summary = "\n".join(lines[:5])
    if len(lines) > 5:
        summary += f"\n... 等共 {len(lines)} 条"
    return summary
