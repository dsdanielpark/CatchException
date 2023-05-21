import sys
from ExceptNotifier.telegram import ExceptTelegramIpython, ExceptTelegram

except_telegram = ExceptTelegramIpython()

if 'ipykernel' in sys.modules:
    try:
        get_ipython().set_custom_exc((Exception,), except_telegram.custom_exc)
    except:
        sys.excepthook = ExceptTelegram()
else:
    sys.excepthook = ExceptTelegram()
