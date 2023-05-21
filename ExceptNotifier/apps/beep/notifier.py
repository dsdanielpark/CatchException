from ExceptNotifier.base.notifier import BaseSuccessHandler, BaseSendHandler, BaseExceptionIpython
from ExceptNotifier.notifier.beep.sender import beep

class SuccessBeep(BaseSuccessHandler):
    """
    Sends success message to Beep.
    """

    def __call__(self, *args, **kwargs):
        """
        Sends success message to Beep.

        :param args: Positional arguments
        :param kwargs: Keyword arguments
        :return: Result of the decorated function call
        """
        beep()
        return super().__call__(*args, **kwargs)


class SendBeep(BaseSendHandler):
    """
   Sends specific line arrival message to Beep.
    """

    def __call__(self, *args, **kwargs):
        """
       Sends specific line arrival message to Beep.

        :param args: Positional arguments
        :param kwargs: Keyword arguments
        :return: Result of the decorated function call
        """
        beep()
        return super().__call__(*args, **kwargs)


class ExceptBeep(BaseException):
    """
    Custom exception that sends error message to Beep.
    """

    def __call__(self, *args, **kwargs):
        """
        Sends error message to Beep.

        :param args: Positional arguments
        :param kwargs: Keyword arguments
        :return: Result of the decorated function call
        """
        beep()
        

class ExceptBeepIpython(BaseExceptionIpython):
    def __init__(self):
        super().__init__()
        pass

    def custom_exc(
        self, shell: object, etype: object, evalue: object, tb: object, tb_offset=1
    ) -> None:
        """ExceptNotifier function for overriding custom execute in IPython for sending Beep.

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
        beep()
        