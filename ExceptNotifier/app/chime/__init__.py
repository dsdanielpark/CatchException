import sys
from ExceptNotifier.notifier.chime import ExceptChimeIpython, ExceptChime

except_chime = ExceptChimeIpython()

if 'ipykernel' in sys.modules:
    try:
        get_ipython().set_custom_exc((Exception,), except_chime.custom_exc)
    except:
        sys.excepthook = ExceptChime()
else:
    sys.excepthook = ExceptChime()
