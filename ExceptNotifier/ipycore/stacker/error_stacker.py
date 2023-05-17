# Copyright 2023 parkminwoo
import datetime
from os import environ
from IPython.core.ultratb import AutoFormattedTB


def stack_error_msg(etype, evalue, tb, app_name):
    itb = AutoFormattedTB(mode="Plain", tb_offset=1)
    stb = itb.structured_traceback(etype, evalue, tb)
    sstb = itb.stb2text(stb)
    start_time = datetime.datetime.now()
    if app_name in ['telegram']:
        data = {
            "text": f"[Except Notifier] ⚠️ Error! Python Code Exception Detected \n \n\nIMPORTANT WARNING \nPython Exception Detected in Your Code. \n\nHi there, \nThis is an exception catch notifier. \n\n - ☑️ Code Status: Fail.🛠 \n - ☑️ Detail: Python Code Ran Exceptions. \n - 🕐 Time: {start_time.strftime(DATE_FORMAT)} \n\n ⛔️ {sstb}"
            }
    data['error_message'] = f"error_type_document=={etype.__doc__}, error_value=={evalue}, error message in ipython cell=={sstb}"
    return data