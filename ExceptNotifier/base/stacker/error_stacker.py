import traceback
from email.message import EmailMessage
from os import environ
from ExceptNotifier.base.utils.time_stamper import get_timestamp
from ExceptNotifier.base.template.error_template import error_message_template as errormsgtemplate


def stack_error_msg(etype, value, tb, app_name):
    exc_type = str(etype).strip("'<>() ").split()[1]
    start_time = get_timestamp()

    message_dict = errormsgtemplate.get(app_name)
    if message_dict is None:
        return None

    message = EmailMessage() if app_name == "gmail" else {}
    message['TO'] = environ.get("_GAMIL_RECIPIENT_ADDR", "") if app_name == "gmail" else ""
    message['FROM'] = environ.get("_GMAIL_SENDER_ADDR", "") if app_name == "gmail" else ""
    message['SUBJECT'] = message_dict["SUBJECT"]
    message['BODY'] = message_dict["BODY"] + f"\nTime Stamp: {start_time}"

    if app_name == "gmail":
        message.set_content(message['BODY'])

    stack_trace = "\n".join(
        f'\tFile: "{line[0]}"\n\t\t{line[2]} {line[1]}: {line[3]}' for line in traceback.extract_tb(tb)
    )
    stack = traceback.extract_stack()[:-1]
    locals_by_frame = "\n".join(
        f"\nFrame {frame.f_code.co_name} in {frame.f_code.co_filename} at line {frame.f_lineno}\n"
        + "\n".join(f"\t%20s = {val}" % key for key, val in frame.f_locals.items())
        for frame in stack
    )

    message['BODY'] += "\nLocals by frame, innermost last::::" + locals_by_frame
    last_frame = stack[-1].f_code if stack else None

    error_message = f"""
        error_type=={exc_type}
        error_type_document=={etype.__doc__}
        error_value=={value}
        stack infomation=={stack}
        code name=={last_frame.co_name if last_frame else ""}
        file name=={last_frame.co_filename if last_frame else ""}
        file_number=={last_frame.co_firstlineno if last_frame else ""}
    """

    advice_msg = stack_trace[-1] if stack_trace else ""

    data = {
        "text": message["SUBJECT"] + message["BODY"] if app_name != "gmail" else None,
        "error_message": error_message,
        "advice_msg": advice_msg,
    }

    if app_name == "gmail":
        data["message_dict"] = message
    else:
        data["message_dict"] = message["SUBJECT"] + message["BODY"]

    return data


