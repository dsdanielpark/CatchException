from ExceptNotifier.base.notifier import BaseSuccessHandler, BaseSendHandler, BaseExceptionIpython
from ExceptNotifier.base.stacker.success_stacker import stack_success_msg
from ExceptNotifier.base.stacker.send_stacker import stack_send_msg
from ExceptNotifier.base.stacker.error_stacker import stack_error_msg
from ExceptNotifier.decorators.bard_ai_decorator import handle_bard_if_available
from ExceptNotifier.decorators.open_ai_decorator import handle_openai_if_available
from ExceptNotifier.apps.line.sender import send_line_msg


from os import environ


class SuccessLine(BaseSuccessHandler):
    """
    Sends success message to Line.
    """

    def __call__(self, *args, **kwargs):
        """
        Sends success message to Line.

        :param args: Positional arguments
        :param kwargs: Keyword arguments
        :return: Result of the decorated function call
        """
        send_line_msg(environ["_LINE_NOTIFY_API_TOKEN"], stack_success_msg("line")["text"])
        return super().__call__(*args, **kwargs)


class SendLine(BaseSendHandler):
    """
    Sends specific line arrival message to Line.
    """

    def __call__(self, *args, **kwargs):
        """
        Sends send message to Line.

        :param args: Positional arguments
        :param kwargs: Keyword arguments
        :return: Result of the decorated function call
        """
        send_line_msg(environ["_LINE_NOTIFY_API_TOKEN"], stack_send_msg("line")["text"])
        return super().__call__(*args, **kwargs)


class ExceptLine(BaseException):
    """
    Custom exception that sends error message to Line.
    """

    @handle_openai_if_available
    @handle_bard_if_available
    def __call__(etype: object, value: object, tb: object):
        """
        Sends error message to Line.

        :param args: Positional arguments
        :param kwargs: Keyword arguments
        :return: Result of the decorated function call
        """
        error_msg = stack_error_msg(etype, value, tb, "line")
        send_line_msg(
            environ["_LINE_NOTIFY_API_TOKEN"],
            error_msg["text"],
        )


class ExceptLineIpython(BaseExceptionIpython):
    def __init__(self):
        super().__init__()
        pass

    @handle_openai_if_available
    @handle_bard_if_available
    def custom_exc(
        self, shell: object, etype: object, evalue: object, tb: object, tb_offset=1
    ) -> None:
        """ExceptNotifier function for overriding custom execute in IPython for sending Line.

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
        data = stack_error_msg(etype, evalue, tb, "line")
        send_line_msg(environ["_LINE_NOTIFY_API_TOKEN"], data["text"])

        return None
