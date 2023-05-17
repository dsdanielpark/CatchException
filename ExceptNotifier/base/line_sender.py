import requests
from requests import Response


def send_line_msg(line_notify_api_token: str, msg: str) -> Response:
    """Send message to chat room through Line app's REST API.

    :param line_notify_api_token: Line notify API token
    :type line_notify_api_token: str
    :param msg: Message text
    :type msg: str
    :return: Response according to REST API request
    :rtype: dict
    """
    api_url = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": "Bearer " + line_notify_api_token}
    message = {"message": msg}
    resp = requests.post(api_url, headers=headers, data=message)
    return resp
