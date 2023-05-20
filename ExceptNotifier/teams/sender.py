import requests


def send_teams_msg(teams_webhook_url: str, msg: str) -> dict:
    """
    Send a message to a chat room through Microsoft Teams app's webhook URL.

    :param teams_webhook_url: Webhook URL from Microsoft Teams app.
    :type teams_webhook_url: str
    :param msg: Message text.
    :type msg: str
    :return: Response from the REST API request.
    :rtype: dict
    """
    payload = {"text": msg}
    headers = {"Content-Type": "application/json"}
    resp = requests.post(teams_webhook_url, headers=headers, json=payload)
    resp.raise_for_status()  # Raise an exception for any HTTP errors

    return resp.json()
