import requests


def send_whatsapp_msg(
    msg: str,
    sender_phone_number_id: str,
    TOKEN: str,
    receiver_number: str,
    recipient_type: str = "individual"
) -> dict:
    """
    Send a message via WhatsApp.

    :param msg: Message content.
    :param sender_phone_number_id: Sender phone number.
    :param TOKEN: WhatsApp personal token.
    :param receiver_number: Recipient phone number.
    :param recipient_type: Type of recipient (default is "individual").
    :return: Response from the API.
    """

    url = f"https://graph.facebook.com/v16.0/{sender_phone_number_id}/messages"

    data = {
        "messaging_product": "whatsapp",
        "to": receiver_number,
        "type": "text",
        "text": msg
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN}"
    }
    resp = requests.post(url, headers=headers, json=data)
    return resp
