import requests


def send_slack_msg(slack_webhook_url, msg):
    """
    Send a message to a chat room through the Slack app's API.

    :param slack_webhook_url: Slack webhook URL.
    :param msg: Message text.
    :return: Response from the REST API request.
    :rtype: requests.Response
    """
    return requests.post(url=slack_webhook_url, json={"text": msg})
