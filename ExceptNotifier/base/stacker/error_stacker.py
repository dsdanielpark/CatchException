import re
import traceback
from ExceptNotifier.utils.time_stamper import get_timestamp
from os import environ


def stack_error_msg(etype, value, tb, app_name):
    exc_type = re.sub(r"(<(type|class ')|'exceptions.|'>|__main__.)", "", str(etype)).strip()
    start_time = get_timestamp()
    stacked_message = {}

    if app_name == "telegram":
        stacked_message["SUBJECT"] = "[Except Notifier] ⚠️ Error! Python Code Exception Detected"
        stacked_message["BODY"] = (
            f"\n\nIMPORTANT WARNING\nPython Exception Detected in Your Code.\n\n"
            f"Hi there,\nThis is an exception catch notifier.\n\n"
            f"- ☑️ Code Status: Fail.🛠\n"
            f"- ☑️ Detail: Python Code Ran Exceptions.\n"
            f"- 🕐 Time: {start_time}\n\n"
            f"⛔️ {exc_type}: %{etype.__doc__}\n\n{value}\n\n"
        )

    elif app_name == "gmail":
        stacked_message["TO"] = environ["_GAMIL_RECIPIENT_ADDR"]
        stacked_message["FROM"] = environ["_GMAIL_SENDER_ADDR"]
        stacked_message["SUBJECT"] = "[Except Notifier] Error! Python Code Exception Detected"
        stacked_message["BODY"] = (
            f"IMPORTANT WARNING:\nPython Exception Detected in Your Code.\n\n"
            f"Hi there,\nThis is an exception catch notifier.\n\n"
            f"{exc_type}: %{etype.__doc__}\n\n{value}\n\n"
        )

    stack_trace = "\n".join(f'\tFile: "{line[0]}"\n\t\t{line[2]} {line[1]}: {line[3]}' for line in traceback.extract_tb(tb))
    stack = traceback.extract_stack()[:-1]
    locals_by_frame = "\n".join(
        f"\nFrame {frame.f_code.co_name} in {frame.f_code.co_filename} at line {frame.f_lineno}\n"
        + "\n".join(f"\t%20s = {val}" % key for key, val in frame.f_locals.items())
        for frame in stack
    )

    stacked_message["BODY"] += "\nLocals by frame, innermost last::::" + locals_by_frame
    last_frame = stack[-1].f_code if stack else None

    data = {
        "text": stacked_message.get("SUBJECT", "") + stacked_message.get("BODY", ""),
        "error_message": f"""
            error_type=={exc_type}
            error_type_document=={etype.__doc__}
            error_value=={value}
            stack infomation=={stack}
            code name=={last_frame.co_name if last_frame else ""}
            file name=={last_frame.co_filename if last_frame else ""}
            file_number=={last_frame.co_firstlineno if last_frame else ""}
        """,
        "advice_msg": stack_trace[-1] if stack_trace else "",
    }

    return data
