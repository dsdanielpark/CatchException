from ExceptNotifier.telegram.sender import send_telegram_msg
from ExceptNotifier.ai_core.bard_receiver import receive_bard_advice
from ExceptNotifier.base.stacker.error_stacker import stack_error_msg
from os import environ



def handle_bard_if_available(func):
    def wrapper(*args, **kwargs):
        if environ.get("_BARD_API_KEY"):
            try:
                bard_advice = receive_bard_advice(
                    environ["_BARD_API_KEY"],
                    stack_error_msg(*args, **kwargs, handler_name="telegram")["advice_msg"],
                )
                send_telegram_msg(environ["_TELEGRAM_TOKEN"], stack_error_msg(*args, **kwargs, handler_name="telegram")["advice_msg"] + bard_advice)
            except Exception as e:
                print(f"Response error during getting advice from Bard: {e}")
                print("Insufficient variables set to receive debugging info from Google Bard.")
                print("Set the following 2 variables as global: _BARD_API_KEY, _BARD_ADVICE_LANG")
        return func(*args, **kwargs)
    return wrapper