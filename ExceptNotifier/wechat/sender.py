import requests


def send_wechat_msg(wechat_webhook_url: str, msg: str) -> None:
    """
    Send a message to WeChat.

    :param wechat_webhook_url: WeChat Webhook URL.
    :param msg: Message to send.
    """
    msg_template = {"msgtype": "text", "text": {"content": ""}}
    msg_template["text"]["content"] = "\n".join(msg)
    resp = requests.post(wechat_webhook_url, json=msg_template)
    return resp
