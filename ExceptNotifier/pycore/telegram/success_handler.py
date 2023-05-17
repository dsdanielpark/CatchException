# Copyright 2023 parkminwoo
from typing import Any
from ExceptNotifier.pycore.base_handler.base_success_handler import BaseSuccessHandler
from ExceptNotifier.base.telegram_sender import send_telegram_msg
from ExceptNotifier.pycore.stacker.success_stacker import stack_success_msg
from os import environ


class SuccessTelegram(BaseSuccessHandler):
    """Sending success message to telegram"""
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        data = stack_success_msg("telegram")
        send_telegram_msg(environ["_TELEGRAM_TOKEN"], data["text"])
        return super().__call__(*args, **kwargs)
