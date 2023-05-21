from ExceptNotifier.apps.telegram.sender import send_telegram_msg
from ExceptNotifier.base.ai.openai_receiver import receive_openai_advice
from ExceptNotifier.base.stacker.error_stacker import stack_error_msg
from os import environ


def handle_openai_if_available(app_name):
    def app_handler(func):
        def wrapper(*args, **kwargs):
            if environ.get("_OPEN_AI_API"):
                try:
                    openai_advice = receive_openai_advice(
                        environ["_OPEN_AI_MODEL"],
                        environ["_OPEN_AI_API"],
                        stack_error_msg(*args, **kwargs, app_name)["error_message"],
                    )
                    send_telegram_msg(environ["_TELEGRAM_TOKEN"], stack_error_msg(*args, **kwargs, app_name)["advice_msg"] + openai_advice)
                except Exception as e:
                    print(f"Response error during getting advice from chatGPT: {e}")
                    print("Insufficient variables set to receive debugging info from OpenAI ChatGPT.")
                    print("Set the following 2 variables as global: _OPEN_AI_MODEL, _OPEN_AI_API")
            return func(*args, **kwargs) + app_name
        return wrapper
    return app_handler