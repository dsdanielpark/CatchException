import re
import traceback
import datetime
from os import environ


def stack_error_msg(etype, value, tb, app_name):
    excType = re.sub(
        "(<(type|class ')|'exceptions.|'>|__main__.)", "", str(etype)
    ).strip()
    start_time = datetime.datetime.now()
    if app_name in ['telegram']:
        stacked_message = {
            "SUBJECT": "[Except Notifier] ⚠️ Error! Python Code Exception Detected",
            "BODY": f"\n\nIMPORTANT WARNING \nPython Exception Detected in Your Code. \n\nHi there, \nThis is an exception catch notifier. \n\n - ☑️ Code Status: Fail.🛠 \n - ☑️ Detail: Python Code Ran Exceptions. \n - 🕐 Time: {start_time.strftime(DATE_FORMAT)} \n\n ⛔️ {excType}: %{etype.__doc__}\n\n {value} \n\n",
        }
    elif app_name in ['gmail']:
        stacked_message = {
            "TO": environ["_GAMIL_RECIPIENT_ADDR"],
            "FROM": environ["_GMAIL_SENDER_ADDR"],
            "SUBJECT": "[Except Notifier] Error! Python Code Exception Detected",
            "BODY": f"IMPORTANT WARNING: \nPython Exception Detected in Your Code. \n\nHi there, \nThis is an exception catch notifier.\n\n{excType}: %{etype.__doc__}\n\n {value} \n\n",
        }
    for line in traceback.extract_tb(tb):
        stacked_message["BODY"] += '\tFile: "%s"\n\t\t%s %s: %s\n' % (
            line[0],
            line[2],
            line[1],
            line[3],
        )
    while 1:
        if not tb.tb_next:
            break
        tb = tb.tb_next
    stack = []
    f = tb.tb_frame
    while f:
        stack.append(f)
        f = f.f_back
    stack.reverse()
    stacked_message["BODY"] += "\nLocals by frame, innermost last::::"
    for frame in stack:
        stacked_message["BODY"] += "\nFrame %s in %s at line %s" % (
            frame.f_code.co_name,
            frame.f_code.co_filename,
            frame.f_lineno,
        )
        for key, val in frame.f_locals.items():
            stacked_message["BODY"] += "\n\t%20s = " % key
            try:
                stacked_message["BODY"] += str(val)
            except:
                stacked_message["BODY"] += "<ERROR WHILE PRINTING VALUE>"
    data = {"text": stacked_message["SUBJECT"] + stacked_message["BODY"]}
    error_message = f"error_type=={excType} error_type_document=={etype.__doc__} error_value=={value} stack infomation=={stack} code name=={frame.f_code.co_name}file name=={frame.f_code.co_filename} file_number=={frame.f_lineno}"
    advice_msg = '\tFile: "%s"\n\t\t%s %s: %s\n' % (
        line[0],
        line[2],
        line[1],
        line[3],
    )
    return data, error_message, advice_msg