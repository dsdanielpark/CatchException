# Copyright 2023 parkminwoo
from os import environ
from ExceptNotifier.base.telegram_sender import send_telegram_msg
from ExceptNotifier.aicore.openai_receiver import receive_openai_advice
from ExceptNotifier.aicore.bard_receiver import receive_bard_advice
from ExceptNotifier.pycore.stacker.error_stacker import stack_error_msg

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

class ExceptTelegram(BaseException):
    """Override excepthook to send error message to Telegram.

    :param etype: Error Type
    :type etype: _type_
    :param value: Error Value
    :type value: _type_
    :param tb: Traceback Information
    :type tb: _type_
    """
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __call__(etype, value, tb):
        data, error_message, advice_msg = stack_error_msg(etype, value, tb, 'telegram')
        send_telegram_msg(environ["_TELEGRAM_TOKEN"], data["text"])
        if environ.get("_OPEN_AI_API") is not None:
            try:
                openai_advice = receive_openai_advice(
                    environ["_OPEN_AI_MODEL"], environ["_OPEN_AI_API"], error_message
                ) 
                openai_advice = advice_msg+openai_advice
                send_telegram_msg(environ["_TELEGRAM_TOKEN"], openai_advice)
            except Exception as e:
                print('Response error during getting advice from chatGPT \n {e} \n Insufficient variables set to receive debugging info from OpenAI ChatGPT. Set the following 2 variables as global: _OPEN_AI_MODEL,_OPEN_AI_API')
        if environ.get("_BARD_API_KEY") is not None:
            try:
                bard_advice = receive_bard_advice(
                    environ["_BARD_API_KEY"], error_message
                ) 
                bard_advice = advice_msg+bard_advice
                send_telegram_msg(environ["_TELEGRAM_TOKEN"], bard_advice)
            except Exception as e:
                print('Response error during getting advice from Bard \n {e} \n Insufficient variables set to receive debugging info from Google Bard. Set the following 2 variables as global: _BARD_API_KEY,_BARD_ADVICE_LANG')
