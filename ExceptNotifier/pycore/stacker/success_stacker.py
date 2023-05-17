import datetime

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def stack_success_msg(app_name):
    success_message = dict()
    start_time = datetime.datetime.now()
    f"Time Stamp: {start_time.strftime(DATE_FORMAT)}"
    if app_name in ["telegram"]:
        success_message = {
            "SUBJECT": "[Success Notifier] 🎉 Success! Python Code Executed Successfully"
        }
        success_message[
            "BODY"
        ] = f"\n\nHi there, \nThis is a success notifier.\n\n - ✅ Code Status: Success. \n - ✅ Detail: Python Code Ran Without Exceptions. \n - 🕐 Time: {start_time.strftime(DATE_FORMAT)} \n\nI just wanted to let you know that your Python code has run successfully without any exceptions. \n\nAll the best, \nExcept Notifier github.com/dsdanielpark/success_message"

        data = {"text": success_message["SUBJECT"] + success_message["BODY"]}

    return data
