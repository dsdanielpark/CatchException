import bardapi
from os import environ


def get_input_text(error_message: str) -> str:
    lang = environ.get("_BARD_ADVICE_LANG")
    if lang == "ko":
        return f"다음 에러와 관련된 더 많은 설명을 알려줘. 그리고 만약 이 오류와 관련된 코드 예제 및 유용한 자료가 있다면 가능한 많이 알려줘. 오류는 {error_message}이다."
    if lang == "jp":
        return f"いくつかのリンクまたはコード例を見つけてください。このエラーに関する詳細情報と、この問題に関連する StackOverflow URL を教えてください。エラーは {error_message} です."
    print("You can only use ko or jp for the _BARD_ADVICE_LANG variable. Hence, answers will be provided in English.")
    return f"Give me more explanation for the following error. And if you have a code example and a way to solve it, please suggest it. Please provide as much information as possible. Error is {error_message}."


def receive_bard_advice(bard_api_key: str, error_message: str) -> str:
    environ["_BARD_API_KEY"] = bard_api_key
    input_text = get_input_text(error_message) if not environ.get("_PROMPT_COMMAND") else f"{environ['_PROMPT_COMMAND']} error=={error_message}"
    return bardapi.core.Bard().get_answer(input_text)["content"]


def get_response_bard_advice(bard_api_key: str) -> dict:
    return bardapi.core.Bard(token=bard_api_key).get_answer("test")
