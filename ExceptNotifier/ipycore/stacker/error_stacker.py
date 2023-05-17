# Copyright 2023 parkminwoo
import datetime
from IPython.core.ultratb import AutoFormattedTB

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def stack_error_msg(etype, evalue, tb, app_name):

    itb = AutoFormattedTB(mode="Plain", tb_offset=1)
    stb = itb.structured_traceback(etype, evalue, tb)
    sstb = itb.stb2text(stb)
    start_time = datetime.datetime.now()
    data = dict()
    if app_name in ["telegram"]:
        data = {
            "text": f"[Except Notifier] ⚠️ Error! Python Code Exception Detected "
                    f"\n \n\nIMPORTANT WARNING \nPython Exception Detected in Your Code. "
                    f"\n\nHi there, \nThis is an exception catch notifier. "
                    f"\n\n - ☑️ Code Status: Fail.🛠 \n - ☑️ Detail: Python Code Ran Exceptions. "
                    f"\n - 🕐 Time: {start_time.strftime(DATE_FORMAT)} \n\n ⛔️ {sstb}"
        }
    data[
        "error_message"
    ] = f"error_type_document=={etype.__doc__}, error_value=={evalue}, error message in ipython cell=={sstb}"
    return data
