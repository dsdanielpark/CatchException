
from ExceptNotifier.pycore.base_handler.base_success_handler import BaseSuccessHandler
from ExceptNotifier.base.telegram_sender import send_telegram_msg
from os import environ


class SuccessTelegram(BaseSuccessHandler):
    """Sending success message to telegram
    """

    def __init__(self) -> None:
        super.__init__()

    def __call__(self) -> None:
        super.__call__()
        send_telegram_msg(environ["_TELEGRAM_TOKEN"], self.data["text"])
