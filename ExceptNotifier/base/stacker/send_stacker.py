from ExceptNotifier.base.utils.time_stamper import get_timestamp
from ExceptNotifier.base.utils.message_generator import generate_message
from email.message import EmailMessage
from os import environ
from typing import Optional
from ExceptNotifier.base.template.send_template import SEND_MESSAGE_TEMPLATE as SEND_TEMPLATE


def stack_send_msg(app_name: str) -> Optional[EmailMessage]:
    """
    Generate a send message for the given app name.

    Args:
        app_name: Name of the application.

    Returns:
        EmailMessage: The send message as an EmailMessage object, or None if app_name is not found.
    """
    start_time = get_timestamp()


    send_message = SEND_TEMPLATE.get(app_name)
    if send_message is None:
        return None

    send_message["body"] += f"- Time: {start_time}"

    if app_name == "gmail":
        send_message_obj = EmailMessage()
        send_message_obj.set_content(send_message["body"])
        send_message_obj["subject"] = send_message["subject"]
        send_message_obj["from"] = environ.get("_GMAIL_SENDER_ADDR", "")
        send_message_obj["to"] = environ.get("_GAMIL_RECIPIENT_ADDR", "")
        send_message_obj["app_password"] = environ.get("_GMAIL_APP_PASSWORD_OF_SENDER", "")
        return send_message_obj

    return generate_message(send_message["subject"], send_message["body"])
