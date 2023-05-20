from os import environ
from email.message import EmailMessage
from typing import Optional
from ExceptNotifier.base.utils.time_stamper import get_timestamp
from ExceptNotifier.base.utils.message_generator import generate_message


success_message_dict = {
    "telegram": {
        "SUBJECT": "[Success Notifier] 🎉 Success! Python Code Executed Successfully",
        "BODY": "\n\nHi there,\nThis is a success notifier."
                "\n\n - ✅ Code Status: Success.\n - ✅ Detail: Python Code Ran Without Exceptions."
    },
    "desktop": {
        "SUBJECT": "[Success Notifier] 🎉 Success! Python Code Executed Successfully",
        "BODY": "\n\nHi there,\nThis is a success notifier."
                "\n\n - ✅ Code Status: Success.\n - ✅ Detail: Python Code Ran Without Exceptions."
    },
    "line": {
        "SUBJECT": "[Success Notifier] 🎉 Success! Python Code Executed Successfully",
        "BODY": "\n\nHi there,\nThis is a success notifier."
                "\n\n - ✅ Code Status: Success.\n - ✅ Detail: Python Code Ran Without Exceptions."
    },
    "teams": {
        "SUBJECT": "[Success Notifier] 🎉 Success! Python Code Executed Successfully",
        "BODY": "\n\nHi there,\nThis is a success notifier."
                "\n\n - ✅ Code Status: Success.\n - ✅ Detail: Python Code Ran Without Exceptions."
    },
    "wechat": {
        "SUBJECT": "[Success Notifier] 🎉 Success! Python Code Executed Successfully",
        "BODY": "\n\nHi there,\nThis is a success notifier."
                "\n\n - ✅ Code Status: Success.\n - ✅ Detail: Python Code Ran Without Exceptions."
    },
    "gmail": {
        "SUBJECT": "[Success Notifier] Success! Python Code Executed Successfully",
        "BODY": "Hi there, \nThis is a success notifier.\n\n"
                "- Code Status: Done. \n - Detail: Python Code Ran Without Exceptions."
    },
    "kakaotalk": {
        "SUBJECT": "[Success Notifier] ** Success! ** Python Code Executed Successfully",
        "BODY": "\n\nHi there, \nThis is a success notifier.\n\n"
                "- Code Status: Success. \n - Detail: Python Code Ran Without Exceptions."
    },
    "sms": {
        "SUBJECT": "[Success Notifier] ** Success! ** Python Code Executed Successfully",
        "BODY": "\n\nHi there, \nThis is a success notifier.\n\n"
                "- Code Status: Success. \n - Detail: Python Code Ran Without Exceptions."
    },
    "chime": {
        "SUBJECT": "[Success Notifier] :tada: Success! Python Code Executed Successfully",
        "BODY": "\n\nHi there, \nThis is a success notifier.\n\n"
                "- :white_check_mark: Code Status: Success. \n - :white_check_mark: Detail: Python Code Ran Without Exceptions."
    },
    "discord": {
        "SUBJECT": "[Success Notifier] :tada: Success! Python Code Executed Successfully",
        "BODY": "\n\nHi there, \nThis is a success notifier.\n\n"
                "- :white_check_mark: Code Status: Success. \n - :white_check_mark: Detail: Python Code Ran Without Exceptions."
    },
    "slack": {
        "SUBJECT": "[Success Notifier] :tada: Success! Python Code Executed Successfully",
        "BODY": "\n\nHi there, \nThis is a success notifier.\n\n"
                "- :white_check_mark: Code Status: Success. \n - :white_check_mark: Detail: Python Code Ran Without Exceptions."
    },
    "discord": {
        "SUBJECT": "[Success Notifier] :tada: Success! Python Code Executed Successfully",
        "BODY": "\n\nHi there, \nThis is a success notifier.\n\n"
                "- :white_check_mark: Code Status: Success. \n - :white_check_mark: Detail: Python Code Ran Without Exceptions."
    }
}


def stack_success_msg(app_name: str) -> Optional[EmailMessage]:
    """
    Generate a success message for the given app name.

    Args:
        app_name: Name of the application.

    Returns:
        EmailMessage: The success message as an EmailMessage object, or None if app_name is not found in the dictionary.
    """
    start_time = get_timestamp()
    message_dict = success_message_dict.get(app_name)

    if app_name == "gmail":
        message = EmailMessage()
        message.set_content(message_dict["BODY"])
        message["Subject"] = message_dict["SUBJECT"]
        message["From"] = environ.get("_GMAIL_SENDER_ADDR", "")
        message["To"] = environ.get("_GAMIL_RECIPIENT_ADDR", "")
        return message

    if message_dict:
        message_dict["BODY"] += f"\n - Time: {start_time}"
        return generate_message(message_dict["SUBJECT"], message_dict["BODY"])

    return None
