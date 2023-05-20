from ExceptNotifier.utils.time_stamper import get_timestamp
from ExceptNotifier.utils.message_generator import generate_message


DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def stack_send_msg(app_name):
    if app_name == "telegram":
        start_time = get_timestamp()
        send_message = {
            "SUBJECT": "[Codeline Notifier] 👏 Notice! Code Execution Reached Specified Line",
            "BODY": f"\n\nHi there,\nThis is a customized notifier.\n\n- ✅ Code Status: Done.\n- ✅ Detail: Code Execution Reached Specified Line.\n- 🕐 Time: {start_time}\n\nThe code has reached the line where you requested an email to be sent. As per your instruction, we are sending this email.\n\nAll the best,\nExcept Notifier github.com/dsdanielpark/send_message"
        }
        return generate_message(send_message["SUBJECT"], send_message["BODY"])

    return {}
