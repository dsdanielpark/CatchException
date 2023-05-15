from abc import ABC
import datetime
from os import environ
from email.message import EmailMessage

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


class BaseSendHandler(ABC):
    def __init__(self) -> None:
        self.data = None

    def __call__(self, *args):
        exceptNotifier = EmailMessage()
        start_time = datetime.datetime.now()
        f"Time Stamp: {start_time.strftime(DATE_FORMAT)}"
        exceptNotifier = {
            "SUBJECT": "[Success Notifier] ** Success! ** Python Code Executed Successfully"
        }
        exceptNotifier[
            "BODY"
        ] = f"\n\nHi there, \nThis is a success notifier.\n\n - Code Status: Success. \n - Detail: Python Code Ran Without Exceptions. \n - Time: {start_time.strftime(DATE_FORMAT)} \n\nI just wanted to let you know that your Python code has run successfully without any exceptions. \n\nAll the best, \nExcept Notifier github.com/dsdanielpark/ExceptNotifier"

        self.data = {"text": exceptNotifier["SUBJECT"] + exceptNotifier["BODY"]}

    
