from twilio.rest import Client


def send_sms_msg(
    twilio_sid: str,
    twilio_token: str,
    sender_phone_number: str,
    recipient_phone_number: str,
    msg: str
) -> dict:
    """
    Send an SMS through the Twilio platform.

    :param twilio_sid: Twilio account SID.
    :param twilio_token: Twilio authentication token.
    :param sender_phone_number: Sender phone number.
    :param recipient_phone_number: Recipient phone number.
    :param msg: SMS content.
    :return: Response dictionary.
    """
    client = Client(twilio_sid, twilio_token)
    resp = client.messages.create(
        to=recipient_phone_number,
        from_=sender_phone_number,
        body=msg[:1500]
    )
    return resp
