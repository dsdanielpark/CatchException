import openai
from os import environ


def receive_openai_advice(open_ai_model: str, open_ai_api: str, error_message: str) -> str:
    """
    Receive debugging information about your code from models in OpenAI.

    :param open_ai_model: Model name of OpenAI.
    :param open_ai_api: API KEY value of OpenAI.
    :param error_message: Error message.
    :return: Description and example of the code, the location of the error, and a debugging code example.
    """
    openai.api_key = open_ai_api
    input_text = f"How can I fix this error? Give me short information about the next error. Let me know which code line and which code is incorrect. And try to provide a fix or a fix example. error== {error_message}"
    if environ.get("_PROMPT_COMMAND"):
        input_text = f"{environ['_PROMPT_COMMAND']} error=={error_message}"
    resp = openai.ChatCompletion.create(model=open_ai_model, messages=[{"role": "user", "content": input_text}])
    return resp["choices"][0]["message"]["content"]


def get_resp_openai_advice(open_ai_model: str, open_ai_api: str) -> dict:
    """
    Check the response of OpenAI API status.

    :param open_ai_model: Model name of OpenAI.
    :param open_ai_api: API KEY value of OpenAI.
    :return: Response dict from OpenAI.
    """
    openai.api_key = open_ai_api
    input_text = "test"
    return openai.ChatCompletion.create(model=open_ai_model, messages=[{"role": "user", "content": input_text}])
