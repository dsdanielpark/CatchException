import sys
from ExceptNotifier.apps.teams.notifier import ExceptTeamsIpython, ExceptTeams

except_teams = ExceptTeamsIpython()

if 'ipykernel' in sys.modules:
    try:
        get_ipython().set_custom_exc((Exception,), except_teams.custom_exc)
    except:
        sys.excepthook = ExceptTeams()
else:
    sys.excepthook = ExceptTeams()
