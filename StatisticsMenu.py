# StatisticsMenu.py

from StandardModule import InputPrompt
from InputModule import IntInput
from importlib import reload
import statistics

print()
print('  This Module Evaluates Various Statistical Concepts')
print('  1. Mean, Median & Mode''    ''2. Data Distribution: Standard Deviation and Variance')
print('  3. Sampling''               ''4. X/Y Coordinates')

n = InputPrompt(None)
n = IntInput(None)

valid = [1, 2, 3, 4]
while n not in valid:
    print('  You\'ve entered an Invalid input')
    print('  Valid Numbers Range from: 1 to 4')
    n = IntInput(None)

if n == 1:
    import MeanMedianModeMenu
    reload(MeanMedianModeMenu)

elif n == 2:
    import StdDevVarMenu
    reload(StdDevVarMenu)

elif n == 3:
    import SamplingMenu
    reload(SamplingMenu)

elif n == 4:
    import XYCoordinates
    reload(XYCoordinates)
