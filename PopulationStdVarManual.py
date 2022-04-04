#  PopulationStdVarManual.py

from StandardModule import Logo, ModuleReload
from InputModule import IntInput, Loop, Switch
from ManualInputProcessorPopulation import FloatsOnly
from importlib import reload
import statistics


# 1.Population Variance
def PVar():
    return statistics.pvariance(FloatsOnly)


# 2.Population Standard Deviation
def PStD():
    return statistics.pstdev(FloatsOnly)


print()
print('  The Population Variance is:', round(PVar(), 2))
print('  The Population Standard Deviation is:', round(PStD(), 2))

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
