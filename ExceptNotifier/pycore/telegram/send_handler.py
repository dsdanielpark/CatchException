# Copyright 2023 parkminwoo
from typing import Any
from ExceptNotifier.pycore.base_handler.base_send_handler import BaseSendHandler
from ExceptNotifier.base.telegram_sender import send_telegram_msg
from ExceptNotifier.pycore.stacker.send_stacker import stack_send_msg
from os import environ


class SendTelegram(BaseSendHandler):
    """Sending send message to telegram"""
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        data = stack_send_msg("telegram")
        send_telegram_msg(environ["_TELEGRAM_TOKEN"], data["text"])
        return super().__call__(*args, **kwargs)
