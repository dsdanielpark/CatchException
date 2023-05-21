import smtplib
from email.message import EmailMessage


def send_mail_msg(
    gmail_sender_address: str,
    gmail_recipient_address: str,
    gamil_app_pw_of_sender: str,
    subject_msg: str,
    body_msg: str,
) -> dict:
    """Send mail through Gmail SMTP server.

    :param gmail_sender_address: Gmail address of the sender.
    :type gmail_sender_address: str
    :param gmail_recipient_address: Gmail address of the recipient.
    :type gmail_recipient_address: str
    :param gamil_app_pw_of_sender: Google app password.
    :type gamil_app_pw_of_sender: str
    :param subject_msg: Mail title.
    :type subject_msg: str
    :param body_msg: Mail body.
    :type body_msg: str
    :return: Response according to the sending request.
    :rtype: dict
    """
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 465

    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.login(gmail_sender_address, gamil_app_pw_of_sender)
        message = EmailMessage()
        message.set_content(body_msg)
        message["subject"] = subject_msg
        message["from"] = gmail_sender_address
        message["to"] = gmail_recipient_address
        resp = smtp.send_message(message)

    return resp
