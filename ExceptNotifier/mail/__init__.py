import sys
from ExceptNotifier.mail import ExceptMailIpython, ExceptMail

except_telegram = ExceptMailIpython()

if 'ipykernel' in sys.modules:
    try:
        get_ipython().set_custom_exc((Exception,), except_telegram.custom_exc)
    except:
        sys.excepthook = ExceptMail()
else:
    sys.excepthook = ExceptMail()
