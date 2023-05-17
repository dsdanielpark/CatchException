# Copyright 2023 parkminwoo
from ExceptNotifier.ipycore.telegram_notifier_ipython import ExceptTelegramIpython


try:
    get_ipython().set_custom_exc((Exception,), ExceptTelegramIpython)
except:
    pass
