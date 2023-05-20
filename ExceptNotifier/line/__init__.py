import sys
from ExceptNotifier.line import ExceptLineIpython, ExceptLine

except_telegram = ExceptLineIpython()

if 'ipykernel' in sys.modules:
    try:
        get_ipython().set_custom_exc((Exception,), except_telegram.custom_exc)
    except:
        sys.excepthook = ExceptLine()
else:
    sys.excepthook = ExceptLine()
