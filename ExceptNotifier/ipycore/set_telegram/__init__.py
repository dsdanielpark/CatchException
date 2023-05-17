# Copyright 2023 parkminwoo
from ExceptNotifier.ipycore.telegram_notifier_ipython import ExceptTelegramIpython
except_telegram = ExceptTelegramIpython()


try:
    get_ipython().set_custom_exc((Exception,), except_telegram.cus_exc)
except:
    pass
