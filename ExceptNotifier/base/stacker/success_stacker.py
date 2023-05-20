from os import environ
from email.message import EmailMessage
from typing import Optional
from ExceptNotifier.base.utils.time_stamper import get_timestamp
from ExceptNotifier.base.utils.message_generator import generate_message
from ExceptNotifier.base.template.success_template import success_message_template as successmsgtemplate


def stack_success_msg(app_name: str) -> Optional[EmailMessage]:
    """
    Generate a success message for the given app name.

    Args:
        app_name: Name of the application.

    Returns:
        EmailMessage: The success message as an EmailMessage object, or None if app_name is not found in the dictionary.
    """
    start_time = get_timestamp()
    message_dict = successmsgtemplate.get(app_name)

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
