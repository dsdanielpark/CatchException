import urllib3
import json

http = urllib3.PoolManager()

def send_chime_msg(chime_webhook_url: str, msg: str):
    """
    Send a message to a chat room through Chime app's webhook URL.

    :param chime_webhook_url: Webhook URL from Chime app.
    :type chime_webhook_url: str
    :param msg: Message text.
    :type msg: str
    """
    url = chime_webhook_url
    message = {"Content": msg}
    encoded_msg = json.dumps(message).encode("utf-8")
    resp = http.request("POST", url, body=encoded_msg)

    return resp
