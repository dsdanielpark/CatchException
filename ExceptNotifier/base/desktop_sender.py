from plyer import notification


def send_desktop_msg(title_msg: str, body_msg: str, disp_time=5) -> None:
    """Sending notification to desktop

    :param title_msg: Title of message
    :type title_msg: str
    :param body_msg: Body of message
    :type body_msg: str
    :param disp_time: Time duration, defaults to 5
    :type disp_time: int, optional
    """
    notification.notify(title=title_msg[:20], message=body_msg[:200], timeout=disp_time)
