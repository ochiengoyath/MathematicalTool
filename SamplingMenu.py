# SamplingMenu.py

from InputModule import IntInput
from importlib import reload

print()
print('  This Module Samples a Given Number of Data Sets')
print('  Choose a Number to Enter Data Manually or Import from Other Sources')
print('  1. Enter Data Manually''   ''2. Import Data')

n = IntInput(None)

valid = [1, 2]
while n not in valid:
    print('  Valid Numbers Range from: 1 to 2')
    n = IntInput(None)

if n == 1:
    import ManualInputProcessorSampling
    reload(ManualInputProcessorSampling)

elif n == 2:
    import FileFormatSamplingMenu
    reload(FileFormatSamplingMenu)
