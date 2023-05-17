# Copyright 2023 parkminwoo
import smtplib
from email.message import EmailMessage


def send_gmail_msg(
    sender_gmail: str,
    recipient_gamil: str,
    sender_gmail_app_password: str,
    subject_msg: str,
    body_msg: str,
) -> dict:
    """Send mail through gmail smtp server

    :param sender_gmail: Gmail address who send message
    :type sender_gmail: str
    :param recipient_gamil: Gmail address who receive message
    :type recipient_gamil: str
    :param sender_gmail_app_password: Google app password
    :type sender_gmail_app_password: str
    :param subject_msg: Mail title
    :type subject_msg: str
    :param body_msg: Mail body
    :type body_msg: str
    :return: Response according to sending request
    :rtype: dict
    """
    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp.login(sender_gmail, sender_gmail_app_password)
    message = EmailMessage()
    message.set_content(body_msg)
    message["Subject"] = subject_msg
    message["From"] = sender_gmail
    message["To"] = recipient_gamil
    resp = smtp.send_message(message)
    smtp.quit()

    return resp
