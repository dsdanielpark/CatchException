import sys
from ExceptNotifier.sms import ExceptSMSIpython, ExceptSMS

except_sms = ExceptSMSIpython()

if 'ipykernel' in sys.modules:
    try:
        get_ipython().set_custom_exc((Exception,), except_sms.custom_exc)
    except:
        sys.excepthook = ExceptSMS()
else:
    sys.excepthook = ExceptSMS()
