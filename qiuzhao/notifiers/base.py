"""通知器抽象基类。"""

from abc import ABC, abstractmethod


class BaseNotifier(ABC):
    """推送通知抽象接口。"""

    @abstractmethod
    async def send(self, title: str, content: str) -> bool:
        """发送通知。

        Args:
            title: 通知标题
            content: 通知内容（Markdown 格式）

        Returns:
            True 表示发送成功。
        """
        ...
