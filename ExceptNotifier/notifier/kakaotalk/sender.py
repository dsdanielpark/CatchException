import requests
import json

from requests import Response


def send_kakaotalk_msg(kakao_token_path: str, msg: str) -> Response:
    """
    Send a message to a chat room through KakaoTalk app's REST API.

    :param kakao_token_path: Path to the KakaoTalk token file.
    :type kakao_token_path: str
    :param msg: Message text.
    :type msg: str
    :return: Response from the REST API request.
    :rtype: requests.Response
    """
    with open(kakao_token_path, "r") as kakao_file:
        tokens = json.load(kakao_file)
        if tokens is None:
            raise ValueError("Please provide a valid KakaoTalk token JSON file path.")
    
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    headers = {"Authorization": "Bearer " + tokens["access_token"]}
    data = {
        "object_type": "text",
        "text": msg,
        "link": {
            "web_url": "https://developers.kakao.com",
            "mobile_web_url": "https://developers.kakao.com",
        },
    }
    data = {"template_object": json.dumps(data)}
    resp = requests.post(url, headers=headers, data=data)

    return resp
