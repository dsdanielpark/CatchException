import requests


def send_telegram_msg(telegram_token: str, msg: str) -> dict:
    """
    Send a message via Telegram bot.

    :param telegram_token: Telegram secure bot Token
    :type telegram_token: str
    :param msg: Message content
    :type msg: str
    :return: Response dict
    :rtype: dict
    """
    url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
    params = {
        "chat_id": get_bot_id(telegram_token),
        "text": msg
    }
    response = requests.get(url, params=params).json()

    return response


def get_bot_id(telegram_token: str) -> str:
    """
    Get the bot ID associated with the Telegram token.

    :param telegram_token: Telegram secure bot Token
    :type telegram_token: str
    :return: Bot ID
    :rtype: str
    """
    url = f"https://api.telegram.org/bot{telegram_token}/getUpdates"
    response = requests.get(url).json()
    bot_id = response["result"][0]["message"]["from"]["id"]

    return bot_id
