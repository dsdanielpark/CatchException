from ExceptNotifier.ipycore.base_handler.base_exception import BaseExceptionIpython
from ExceptNotifier.base.beep_sender import beep

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


class ExceptBeepIpython(BaseExceptionIpython):
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
        beep()
        beep()
        beep()
