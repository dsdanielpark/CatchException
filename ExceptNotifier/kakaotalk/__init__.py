import sys
from ExceptNotifier.kakaotalk import ExceptKakaotalkIpython, ExceptKakaotalk

except_telegram = ExceptKakaotalkIpython()

if 'ipykernel' in sys.modules:
    try:
        get_ipython().set_custom_exc((Exception,), except_telegram.custom_exc)
    except:
        sys.excepthook = ExceptKakaotalk()
else:
    sys.excepthook = ExceptKakaotalk()
