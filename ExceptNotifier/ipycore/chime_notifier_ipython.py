# Copyright 2023 parkminwoo
import datetime
from os import environ
from IPython.core.ultratb import AutoFormattedTB
from ExceptNotifier.base.chime_sender import send_chime_msg
from ExceptNotifier.aicore.openai_receiver import receive_openai_advice
from ExceptNotifier.aicore.bard_receiver import receive_bard_advice
from ExceptNotifier.ipycore.base_handler.base_exception import BaseExceptionIpython

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"



class ExceptChimeIpython(BaseExceptionIpython):

        
    def custom_exc(
        shell: object, etype: object, evalue: object, tb: object, tb_offset=1
    ) -> None:
        """ExceptNotifier function for overriding custom execute in ipython for sending Chime message.

        :param shell: Excecuted shell, ZMQInteractiveShell object.
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
        itb = AutoFormattedTB(mode="Plain", tb_offset=1)
        shell.showtraceback((etype, evalue, tb), tb_offset=tb_offset)
        stb = itb.structured_traceback(etype, evalue, tb)
        sstb = itb.stb2text(stb)
        start_time = datetime.datetime.now()
        
        error_message = f"error sheel=={shell}, error_type_document=={etype.__doc__}, error_value=={evalue}, error message in ipython cell=={sstb}"
        data = {
            "text": f"[Except Notifier] :warning: Error! Python Code Exception Detected \n\nIMPORTANT WARNING \nPython Exception Detected in Your Code. \n\nHi there, \nThis is an exception catch notifier. \n\n - :x: Code Status: Fail. \n - :x: Detail: Python Code Ran Exceptions. \n - :clock2: Time: {start_time.strftime(DATE_FORMAT)} \n\n :no_entry:  {sstb}"
        }

        send_chime_msg(environ["_CHIME_WEBHOOK_URL"], data["text"])
        if environ.get("_OPEN_AI_API") is not None:
            try:
                advice_msg = receive_openai_advice(
                    environ["_OPEN_AI_MODEL"], environ["_OPEN_AI_API"], error_message
                )
                send_chime_msg(environ["_CHIME_WEBHOOK_URL"], advice_msg)
            except Exception as e:
                pass

        if environ.get("_BARD_API_KEY") is not None:
            try:
                error_message = f"error sheel=={shell}, error_type_document=={etype.__doc__}, error_value=={evalue}, error message in ipython cell=={sstb}"
                advice_msg = receive_bard_advice(environ["_BARD_API_KEY"], error_message)
                send_chime_msg(environ["_CHIME_WEBHOOK_URL"], advice_msg)

            except Exception as e:
                pass
