# Copyright 2023 parkminwoo
from os import environ
from ExceptNotifier.base.telegram_sender import send_telegram_msg
from ExceptNotifier.aicore.openai_receiver import receive_openai_advice
from ExceptNotifier.aicore.bard_receiver import receive_bard_advice
from ExceptNotifier.ipycore.base_handler.base_exception import BaseExceptionIpython
from ExceptNotifier.ipycore.stacker.error_stacker import stack_error_msg

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


class ExceptTelegramIpython(BaseExceptionIpython):
    def __init__(self):
        super().__init__()
        pass

    def custom_exc(
        self, shell: object, etype: object, evalue: object, tb: object, tb_offset=1
    ) -> None:
        """ExceptNotifier function for overriding custom execute in ipython for sending Telegram.

        :param shell: Executed shell, ZMQInteractiveShell object.
        :type shell: object
        :param etype: Error type
        :type etype: object
        :param evalue: Error value
        :type evalue: object
        :param tb: TraceBack object of Ipython
        :type tb: object
        :param tb_offset: Offset of traceback, defaults to 1
        :type tb_offset: int, optional
        """
        shell.showtraceback((etype, evalue, tb), tb_offset=tb_offset)
        data = stack_error_msg(etype, evalue, tb, "telegram")
        send_telegram_msg(environ["_TELEGRAM_TOKEN"], data["text"])

        if environ.get("_OPEN_AI_API") is not None:
            try:
                advice_msg = receive_openai_advice(
                    environ["_OPEN_AI_MODEL"],
                    environ["_OPEN_AI_API"],
                    data["error_message"],
                )
                send_telegram_msg(environ["_TELEGRAM_TOKEN"], advice_msg)
            finally:
                pass
        if environ.get("_BARD_API_KEY") is not None:
            try:
                advice_msg = receive_bard_advice(
                    environ["_BARD_API_KEY"], data["error_message"]
                )
                send_telegram_msg(environ["_TELEGRAM_TOKEN"], advice_msg)
            finally:
                pass
