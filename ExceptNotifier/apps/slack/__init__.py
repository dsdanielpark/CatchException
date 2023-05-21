import sys
from ExceptNotifier.slack import ExceptSlackIpython, ExceptSlack

except_telegram = ExceptSlackIpython()

if 'ipykernel' in sys.modules:
    try:
        get_ipython().set_custom_exc((Exception,), except_telegram.custom_exc)
    except:
        sys.excepthook = ExceptSlack()
else:
    sys.excepthook = ExceptSlack()
