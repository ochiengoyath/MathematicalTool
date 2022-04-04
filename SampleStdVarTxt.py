# SampleStdVarText.py

from StandardModule import Logo, ModuleReload
from InputModule import IntInput, Switch, Loop
from TxtDataProcessorSample import FloatsOnly
from importlib import reload
import statistics

print()


# 1.Sample Variance
def SVar():
    return statistics.variance(FloatsOnly)


# 2.Sample Standard Deviation
def SStD():
    return statistics.stdev(FloatsOnly)

print()
print('  The Sample Variance is:', round(SVar(), 2))
print('  The Sample Standard Deviation is:', round(SStD(), 2))

Logo()
ModuleReload()
n = None
n = IntInput(None)
Switch(n)
if n == 1:
    import StatisticsMenu

    reload(StatisticsMenu)

elif n == 2:
    import ExitMenu

    reload(ExitMenu)

import ExitMenu
reload(ExitMenu)
