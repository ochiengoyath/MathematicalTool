# MeanMedianModeMenu.py

from InputModule import IntInput
from importlib import reload
import statistics

print()
print('  This Module Calculates the Mean, Median & Mode of Data sets.')
print('  Choose a Number to Enter Data Manually or Import from Other Sources')
print('  1. Enter Data Manually''   ''2. Import Data')

n = IntInput(None)

valid = [1, 2]
while n not in valid:
    print('  Valid Numbers Range from: 1 to 2')
    n = IntInput(None)

if n == 1:
    import ManualInputProcessorMean
    reload(ManualInputProcessorMean)

elif n == 2:
    import FileFormatMeanMenu
    reload(FileFormatMeanMenu)
