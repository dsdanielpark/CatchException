import traceback
from email.message import EmailMessage
from os import environ
from ExceptNotifier.base.utils.time_stamper import get_timestamp
from ExceptNotifier.base.template.error_template import ERROR_MESSAGE_TEMPLATE as ERROR_TEMPLATE


def stack_error_msg(etype, value, tb, app_name):
    """
    Generate a stack error message for exception handling.

    :param etype: Exception type.
    :type etype: type
    :param value: Exception value.
    :type value: Any
    :param tb: Traceback object.
    :type tb: TracebackType
    :param app_name: Application name.
    :type app_name: str
    :return: Stack error message data.
    :rtype: dict
    """
    exc_type = str(etype).strip("'<>() ").split()[1]
    start_time = get_timestamp()
    message_dict = ERROR_TEMPLATE.get(app_name)
    if message_dict is None:
        return None

    error_message_object = EmailMessage() if app_name == "gmail" else {}
    error_message_object['to'] = environ.get("_GAMIL_RECIPIENT_ADDR", "") if app_name == "gmail" else ""
    error_message_object['from'] = environ.get("_GMAIL_SENDER_ADDR", "") if app_name == "gmail" else ""
    error_message_object['subject'] = message_dict["subject"]
    error_message_object['body'] = message_dict["body"] + f"\nTime Stamp: {start_time}"
    if app_name == "gmail":
        error_message_object.set_content(error_message_object['body'])

    stack_trace = "\n".join(f'\tFile: "{line[0]}"\n\t\t{line[2]} {line[1]}: {line[3]}' for line in traceback.extract_tb(tb))
    stack = traceback.extract_stack()[:-1]
    locals_by_frame = "\n".join(f"\nFrame {frame.f_code.co_name} in {frame.f_code.co_filename} at line {frame.f_lineno}\n"
                                + "\n".join(f"\t%20s = {val}" % key for key, val in frame.f_locals.items()) for frame in stack)

    error_message_object['body'] += "\nLocals by frame, innermost last::::" + locals_by_frame
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
        "to": error_message_object['to'],
        "from" : error_message_object['from'],
        "subject": error_message_object["subject"],
        "body": error_message_object["body"],
        "text": error_message_object["subject"] + error_message_object["body"] if app_name != "gmail" else None,
        "error_message": error_message,
        "advice_msg": advice_msg,
        "message_dict": error_message_object if app_name == "gmail" else error_message_object["subject"] + error_message_object["body"],
    }

    return data
