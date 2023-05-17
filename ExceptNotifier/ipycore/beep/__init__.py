from ExceptNotifier.ipycore.telegram.telegram_notifier import (
    ExceptTelegramIpython,
)

except_telegram = ExceptTelegramIpython()


try:
    get_ipython().set_custom_exc((Exception,), except_telegram.custom_exc)
finally:
    pass
