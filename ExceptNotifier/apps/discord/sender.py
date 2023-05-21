from discord import Webhook, RequestsWebhookAdapter, SyncWebhook


def send_discord_msg(discord_webhook_url: str, msg: str) -> dict:
    """
    Send a message to a chat room through Discord app's webhook URL.

    :param discord_webhook_url: Webhook URL from Discord app.
    :type discord_webhook_url: str
    :param msg: Message text.
    :type msg: str
    :return: Response according to the REST API request.
    :rtype: dict
    """
    try:
        webhook = Webhook.from_url(discord_webhook_url, adapter=RequestsWebhookAdapter())
        resp = webhook.send(msg)
    except:
        webhook = SyncWebhook.from_url(discord_webhook_url)
        resp = webhook.send(content=msg[:1900])
    
    return resp
