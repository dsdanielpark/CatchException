import datetime


def get_timestamp():
    DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
    return datetime.datetime.now().strftime(DATE_FORMAT)