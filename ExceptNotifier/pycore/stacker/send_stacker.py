import datetime
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

def stack_send_msg(app_name):
    send_message = dict()
    start_time = datetime.datetime.now()
    f"Time Stamp: {start_time.strftime(DATE_FORMAT)}"
    if app_name in ['telegram']:
        send_message = {
            "SUBJECT": "[Codeline Notifier] 👏 Notice! Code Execution Reached Specified Line"
        }
        send_message[
            "BODY"
        ] = f"\n\nHi there, \nThis is a customized notifier.\n\n- ✅ Code Status: Done. \n- ✅ Detail: Code Execution Reached Specified Line.  \n- 🕐 Time: {start_time.strftime(DATE_FORMAT)} \n\nThe code has reached the line where you requested an email to be sent. As per your instruction, we are sending this email. \n\nAll the best, \nExcept Notifier github.com/dsdanielpark/send_message"
    data = {"text": send_message["SUBJECT"] + send_message["BODY"]}
    return data