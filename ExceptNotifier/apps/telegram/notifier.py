from ExceptNotifier.base.notifier import BaseSuccessHandler, BaseSendHandler, BaseExceptionIpython
from ExceptNotifier.apps.telegram.sender import send_telegram_msg
from ExceptNotifier.base.stacker.success_stacker import stack_success_msg
from ExceptNotifier.base.stacker.send_stacker import stack_send_msg
from ExceptNotifier.base.stacker.error_stacker import stack_error_msg
from ExceptNotifier.decorators.bard_ai_decorator import handle_bard_if_available
from ExceptNotifier.decorators.open_ai_decorator import handle_openai_if_available

from os import environ


class SuccessTelegram(BaseSuccessHandler):
    """
    Sends success message to Telegram.
    """

    def __call__(self, *args, **kwargs):
        """
        Sends success message to Telegram.

        :param args: Positional arguments
        :param kwargs: Keyword arguments
        :return: Result of the decorated function call
        """
        send_telegram_msg(environ["_TELEGRAM_TOKEN"], stack_success_msg("telegram")["text"])
        return super().__call__(*args, **kwargs)


class SendTelegram(BaseSendHandler):
    """
    Sends specific line arrival message to Telegram.
    """

    def __call__(self, *args, **kwargs):
        """
        Sends send message to Telegram.

        :param args: Positional arguments
        :param kwargs: Keyword arguments
        :return: Result of the decorated function call
        """
        send_telegram_msg(environ["_TELEGRAM_TOKEN"], stack_send_msg("telegram")["text"])
        return super().__call__(*args, **kwargs)


class ExceptTelegram(BaseException):
    """
    Custom exception that sends error message to Telegram.
    """

    @handle_openai_if_available
    @handle_bard_if_available
    def __call__(self, *args, **kwargs):
        """
        Sends error message to Telegram.

        :param args: Positional arguments
        :param kwargs: Keyword arguments
        :return: Result of the decorated function call
        """
        send_telegram_msg(
            environ["_TELEGRAM_TOKEN"],
            stack_error_msg(*args, **kwargs, "telegram")["text"],
        )


class ExceptTelegramIpython(BaseExceptionIpython):
    def __init__(self):
        super().__init__()
        pass

    @handle_openai_if_available
    @handle_bard_if_available
    def custom_exc(
        self, shell: object, etype: object, evalue: object, tb: object, tb_offset=1
    ) -> None:
        """ExceptNotifier function for overriding custom execute in IPython for sending Telegram.

        :param shell: Executed shell, ZMQInteractiveShell object.
        :type shell: object
        :param etype: Error type
        :type etype: object
        :param evalue: Error value
        :type evalue: object
        :param tb: TraceBack object of IPython
        :type tb: object
        :param tb_offset: Offset of traceback, defaults to 1
        :type tb_offset: int, optional
        """
        shell.showtraceback((etype, evalue, tb), tb_offset=tb_offset)
        data = stack_error_msg(etype, evalue, tb, "telegram")
        send_telegram_msg(environ["_TELEGRAM_TOKEN"], data["text"])

        return None