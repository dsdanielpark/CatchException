from os import environ
from ExceptNotifier.utils.time_stamper import get_timestamp
from ExceptNotifier.utils.message_generator import generate_message


def stack_success_msg(app_name):
    if app_name == "telegram":
        start_time = get_timestamp()
        success_message = {
            "SUBJECT": "[Success Notifier] 🎉 Success! Python Code Executed Successfully",
            "BODY": f"\n\nHi there,\nThis is a success notifier."
                    f"\n\n - ✅ Code Status: Success.\n - ✅ Detail: Python Code Ran Without Exceptions."
                    f"\n - 🕐 Time: {start_time}\n\nI just wanted to let you know that your Python code has run successfully without any exceptions.\n\nAll the best,\nExcept Notifier github.com/dsdanielpark/success_message"
        }
        return generate_message(success_message["SUBJECT"], success_message["BODY"])

    return {}
