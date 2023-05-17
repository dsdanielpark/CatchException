# Copyright 2023 parkminwoo

import requests
from requests import Response


def send_slack_msg(slack_webhook_url: str, msg: str) -> Response:
    """Send message to chat room through slack app's api.

    :param slack_webhook_url: slack_webhook_url from slack app
    :type _SLACK_WEBHOOK_URL: str
    :param msg: Message text
    :type msg: str
    :return: Response according to REST API request
    :rtype: dict
    """
    data = {"text": msg}
    resp = requests.post(url=slack_webhook_url, json=data)

    return resp
