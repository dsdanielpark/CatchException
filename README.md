# Python: ExceptCatch
With Python's try-except statement, experience a significantly more flexible way to receive notifications. You can receive alerts through various messaging platforms such as email, Slack, and Discord. This package offers an extensive range of notification options to suit your needs.

Python package `ExceptCatch` can give a single line alarm with an error message, whereas Python package [`knockknock`](https://github.com/huggingface/knockknock) gives a process ending alarm with decorator and cli.

# Quick Start: install ExceptCatch

```
pip insall exceptcatch
```



<br>

# Features
## 1. `Mail`
- Log in with the sender's email ID. <br>
- Obtain an app password for sending Google Mail at the following [link](https://myaccount.google.com/u/3/apppasswords?utm_source=google-account&utm_medium=myaccountsecurity&utm_campaign=tsv-settings&rapt=AEjHL4N2bMRWO46VaMp_jP06zQK14BWNPv66l2o59iJ99CkO8BjYnmoRUe9dtSchkkbubHZMUhevkAnwVJRHb9ygO3afispNlw). 

```python
from exceptcatch import ExceptionMail, SuccessMail

# 01. Set variable.
global gmail_receiver, gmail_sender, gmail_app_password_of_sender
gmail_receiver = 'parkminwoo1991@gmail.com'
gmail_sender = 'heydudenotice@gmail.com'
gmail_app_password_of_sender = 'xxxxxxxxxxx'

sys.excepthook = ExceptionMail.__call__

try:
    # 02. Locate your code.
    print(1/0)             


# 03-a. Mail Sent: When strike exception
except ExceptionMail as e:                    
    sys.exit()

# 03-b. Mail Sent:  When code exit without exception
SuccessMail().__call__()     
```