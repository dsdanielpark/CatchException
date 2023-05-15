
from base_handler.base_send_handler import BaseSendHandler
from ExceptNotifier.base.telegram_sender import send_telegram_msg
from os import environ

class SendTelegram(BaseSendHandler):
    """Sending message to telegram
    """

    def __init__(self) -> None:
        super.__init__()

    def __call__(self) -> None:
        super.__call__()
        send_telegram_msg(environ["_TELEGRAM_TOKEN"], self.data["text"])
