from os import environ
from email.message import EmailMessage
from typing import Optional
from ExceptNotifier.base.utils.time_stamper import get_timestamp
from ExceptNotifier.base.utils.message_generator import generate_message
from ExceptNotifier.base.template.success_template import SUCCESS_MESSAGE_TEMPLATE as SUCCESS_TEMPLATE


def stack_success_msg(app_name: str) -> Optional[EmailMessage]:
    """
    Generate a success message for the given app name.

    Args:
        app_name: Name of the application.

    Returns:
        EmailMessage: The success message as an EmailMessage object, or None if app_name is not found in the dictionary.
    """
    start_time = get_timestamp()
    message_dict = SUCCESS_TEMPLATE.get(app_name)

    if app_name == "gmail":
        success_message_obj = EmailMessage()
        success_message_obj.set_content(message_dict["body"])
        success_message_obj["subject"] = message_dict["subject"]
        success_message_obj["from"] = environ.get("_GMAIL_SENDER_ADDR", "")
        success_message_obj["to"] = environ.get("_GAMIL_RECIPIENT_ADDR", "")
        success_message_obj["app_password"] = environ.get("_GMAIL_APP_PASSWORD_OF_SENDER", "")
        return success_message_obj
    
    elif app_name == "desktop":
        message_dict["body"] += f"\n - Time: {start_time}"
        return message_dict

    if message_dict:
        message_dict["body"] += f"\n - Time: {start_time}"
        return generate_message(message_dict["subject"], message_dict["body"])

    return None
