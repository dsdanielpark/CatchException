from ExceptNotifier.base.utils.time_stamper import get_timestamp
from ExceptNotifier.base.utils.message_generator import generate_message
from email.message import EmailMessage
from os import environ
from typing import Optional
from ExceptNotifier.base.template.send_template import send_message_template as sendmsgtemplate


def stack_send_msg(app_name: str) -> Optional[EmailMessage]:
    """
    Generate a send message for the given app name.

    Args:
        app_name: Name of the application.

    Returns:
        EmailMessage: The send message as an EmailMessage object, or None if app_name is not found.
    """
    start_time = get_timestamp()


    send_message = sendmsgtemplate.get(app_name)
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
