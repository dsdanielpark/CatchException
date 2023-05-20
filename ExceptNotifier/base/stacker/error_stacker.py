import traceback
from email.message import EmailMessage
from os import environ
from ExceptNotifier.base.utils.time_stamper import get_timestamp


def stack_error_msg(etype, value, tb, app_name):
    exc_type = str(etype).strip("'<>() ").split()[1]
    start_time = get_timestamp()

    message_dict = APP_MESSAGES.get(app_name)
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





# import re
# import traceback
# from os import environ
# from ExceptNotifier.base.utils.time_stamper import get_timestamp
# from email.message import EmailMessage

# def stack_error_msg(etype, value, tb, app_name):
#     exc_type = re.sub(r"(<(type|class ')|'exceptions.|'>|__main__.)", "", str(etype)).strip()
#     start_time = get_timestamp()
    
#     if app_name in ["telegram", "desktop", "line", "teams", "wechat"]:
#         message_dict = {
#             "SUBJECT": "[Except Notifier] ⚠️ Error! Python Code Exception Detected",
#             "BODY": f"\n\nIMPORTANT WARNING\nPython Exception Detected in Your Code.\n\n"
#                     f"Hi there,\nThis is an exception catch notifier.\n\n"
#                     f"- ☑️ Code Status: Fail.🛠\n"
#                     f"- ☑️ Detail: Python Code Ran Exceptions.\n"
#                     f"- 🕐 Time: {start_time}\n\n"
#                     f"⛔️ {exc_type}: %{etype.__doc__}\n\n{value}\n\n"
#         }

#     elif app_name == "gmail":
#         excType = re.sub(
#             "(<(type|class ')|'exceptions.|'>|__main__.)", "", str(etype)
#         ).strip()
#         message_dict = EmailMessage()
#         message_dict = {
#             "TO": environ["_GAMIL_RECIPIENT_ADDR"],
#             "FROM": environ["_GMAIL_SENDER_ADDR"],
#             "SUBJECT": "[Except Notifier] Error! Python Code Exception Detected",
#             "BODY": f"IMPORTANT WARNING: \nPython Exception Detected in Your Code. \n\nHi there, \nThis is an exception catch notifier.\n\n{excType}: %{etype.__doc__}\n\n {value} \n\n",
#         }
#         message_dict.set_content(message_dict['BODY'])
#         for line in traceback.extract_tb(tb):
#             message_dict["BODY"] += '\tFile: "%s"\n\t\t%s %s: %s\n' % (
#                 line[0],
#                 line[2],
#                 line[1],
#                 line[3],
#             )
#         while 1:
#             if not tb.tb_next:
#                 break
#             tb = tb.tb_next
#         stack = []
#         f = tb.tb_frame
#         while f:
#             stack.append(f)
#             f = f.f_back
#         stack.reverse()
#         message_dict["BODY"] += f"\nTime Stamp: {start_time}"
#         message_dict["BODY"] += "\nLocals by frame, innermost last::::"
#         for frame in stack:
#             message_dict["BODY"] += "\nFrame %s in %s at line %s" % (
#                 frame.f_code.co_name,
#                 frame.f_code.co_filename,
#                 frame.f_lineno,
#             )
#             for key, val in frame.f_locals.items():
#                 message_dict["BODY"] += "\n\t%20s = " % key
#                 try:
#                     message_dict["BODY"] += str(val)
#                 except:
#                     message_dict["BODY"] += "<ERROR WHILE PRINTING VALUE>"
#         message_dict['error_message'] = f"""
#             error_type=={exc_type}
#             error_type_document=={etype.__doc__}
#             error_value=={value}
#             stack infomation=={stack}
#             code name=={last_frame.co_name if last_frame else ""}
#             file name=={last_frame.co_filename if last_frame else ""}
#             file_number=={last_frame.co_firstlineno if last_frame else ""}
#         """

#         message_dict["advice_msg"] =  stack_trace[-1] if stack_trace else ""
#         data = message_dict

#         return data

#     elif app_name in ["chime", "discord", "slack"]:
#         message_dict = {
#             "SUBJECT": "[Except Notifier] :warning: Error! Python Code Exception Detected",
#             "BODY": f"\n\nIMPORTANT WARNING \nPython Exception Detected in Your Code. \n\n"
#                     f"Hi there, \nThis is an exception catch notifier. \n\n"
#                     f"- :x: Code Status: Fail. \n"
#                     f"- :x: Detail: Python Code Ran Exceptions. \n"
#                     f"- :clock2: Time: {start_time} \n\n"
#                     f":no_entry: {exc_type}: %{etype.__doc__}\n\n {value} \n\n",
#         }

#     elif app_name in ["kakaotalk", "sms"]:
#         message_dict = {
#             "SUBJECT": "[Except Notifier] ** Error! ** Python Code Exception Detected",
#             "BODY": f"\n\nIMPORTANT WARNING \nPython Exception Detected in Your Code. \n\n"
#                     f"Hi there, \nThis is an exception catch notifier. \n\n"
#                     f"- Code Status: Fail. \n"
#                     f"- Detail: Python Code Ran Exceptions. \n"
#                     f"- Time: {start_time} \n\n"
#                     f":no_entry: {exc_type}: %{etype.__doc__}\n\n {value} \n\n",
#         }

#     stack_trace = "\n".join(f'\tFile: "{line[0]}"\n\t\t{line[2]} {line[1]}: {line[3]}' for line in traceback.extract_tb(tb))
#     stack = traceback.extract_stack()[:-1]
#     locals_by_frame = "\n".join(
#         f"\nFrame {frame.f_code.co_name} in {frame.f_code.co_filename} at line {frame.f_lineno}\n"
#         + "\n".join(f"\t%20s = {val}" % key for key, val in frame.f_locals.items())
#         for frame in stack
#     )

#     message_dict["BODY"] += "\nLocals by frame, innermost last::::" + locals_by_frame
#     last_frame = stack[-1].f_code if stack else None

#     data = {
#         "text": message_dict.get("SUBJECT", "") + message_dict.get("BODY", ""),
#         "error_message": f"""
#             error_type=={exc_type}
#             error_type_document=={etype.__doc__}
#             error_value=={value}
#             stack infomation=={stack}
#             code name=={last_frame.co_name if last_frame else ""}
#             file name=={last_frame.co_filename if last_frame else ""}
#             file_number=={last_frame.co_firstlineno if last_frame else ""}
#         """,
#         "advice_msg": stack_trace[-1] if stack_trace else "",
#     }

#     return data
