from ExceptNotifier.base.utils.time_stamper import get_timestamp
from ExceptNotifier.base.utils.message_generator import generate_message
from email.message import EmailMessage
from os import environ
from typing import Optional



send_message_dict = {
    "telegram": {
        "SUBJECT": "[Codeline Notifier] 👏 Notice! Code Execution Reached Specified Line",
        "BODY": "Hi there,\n\nThis is a customized notifier.\n\n"
                "- ✅ Code Status: Done.\n"
                "- ✅ Detail: Code Execution Reached Specified Line.\n"
    },
    "gmail": {
        "SUBJECT": "[Codeline Notifier] Notice! Code Execution Reached Specified Line",
        "BODY": "Hi there,\n\nThis is a customized notifier.\n\n"
                "- Code Status: Done.\n"
                "- Detail: Code Execution Reached Specified Line.\n"
    },
    "kakaotalk": {
        "SUBJECT": "[Codeline Notifier] ** Notice! ** Code Execution Reached Specified Line",
        "BODY": "Hi there,\n\nThis is a customized notifier.\n\n"
                "- Code Status: Done.\n"
                "- Detail: Code Execution Reached Specified Line.\n"
    },
    "chime": {
        "SUBJECT": "[Codeline Notifier] :clap: Notice! Code Execution Reached Specified Line",
        "BODY": "Hi there,\n\nThis is a customized notifier.\n\n"
                "- ✅ Code Status: Done.\n"
                "- ✅ Detail: Code Execution Reached Specified Line.\n"
    },
    "discord": {
        "SUBJECT": "[Codeline Notifier] :clap: Notice! Code Execution Reached Specified Line",
        "BODY": "Hi there,\n\nThis is a customized notifier.\n\n"
                "- ✅ Code Status: Done.\n"
                "- ✅ Detail: Code Execution Reached Specified Line.\n"
    },
    "slack": {
        "SUBJECT": "[Codeline Notifier] :clap: Notice! Code Execution Reached Specified Line",
        "BODY": "Hi there,\n\nThis is a customized notifier.\n\n"
                "- ✅ Code Status: Done.\n"
                "- ✅ Detail: Code Execution Reached Specified Line.\n"
    },
    "desktop": {
        "SUBJECT": "[Codeline Notifier] :clap: Notice! Code Execution Reached Specified Line",
        "BODY": "Hi there,\n\nThis is a customized notifier.\n\n"
                "- ✅ Code Status: Done.\n"
                "- ✅ Detail: Code Execution Reached Specified Line.\n"
    },
    "line": {
        "SUBJECT": "[Codeline Notifier] :clap: Notice! Code Execution Reached Specified Line",
        "BODY": "Hi there,\n\nThis is a customized notifier.\n\n"
                "- ✅ Code Status: Done.\n"
                "- ✅ Detail: Code Execution Reached Specified Line.\n"
    },
    "teams": {
        "SUBJECT": "[Codeline Notifier] :clap: Notice! Code Execution Reached Specified Line",
        "BODY": "Hi there,\n\nThis is a customized notifier.\n\n"
                "- ✅ Code Status: Done.\n"
                "- ✅ Detail: Code Execution Reached Specified Line.\n"
    },
    "wechat": {
        "SUBJECT": "[Codeline Notifier] :clap: Notice! Code Execution Reached Specified Line",
        "BODY": "Hi there,\n\nThis is a customized notifier.\n\n"
                "- ✅ Code Status: Done.\n"
                "- ✅ Detail: Code Execution Reached Specified Line.\n"
    },
    "sms": {
        "SUBJECT": "[Codeline Notifier] ** Notice! ** Code Execution Reached Specified Line",
        "BODY": "Hi there,\n\nThis is a customized notifier.\n\n"
                "- Code Status: Done.\n"
                "- Detail: Code Execution Reached Specified Line.\n"
    }
}




def stack_send_msg(app_name: str) -> Optional[EmailMessage]:
    """
    Generate a send message for the given app name.

    Args:
        app_name: Name of the application.

    Returns:
        EmailMessage: The send message as an EmailMessage object, or None if app_name is not found.
    """
    start_time = get_timestamp()


    send_message = send_message_dict.get(app_name)
    if send_message is None:
        return None

    send_message["BODY"] += f"- Time: {start_time}"

    if app_name == "gmail":
        send_message_obj = EmailMessage()
        send_message_obj.set_content(send_message["BODY"])
        send_message_obj["Subject"] = send_message["SUBJECT"]
        send_message_obj["From"] = environ.get("_GMAIL_SENDER_ADDR", "")
        send_message_obj["To"] = environ.get("_GAMIL_RECIPIENT_ADDR", "")
        return send_message_obj

    return generate_message(send_message["SUBJECT"], send_message["BODY"])
