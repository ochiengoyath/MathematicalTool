# DataAccessManual.py

# This module gives options on how to access a file
from InputModule import IntInput
n = IntInput(None)

valid = [1, 2]
while n not in valid:
    print('  Valid Numbers Range from: 1 to 2')
    n = IntInput(None)

if n == 1:
    from ManualInputProcessorMean import FloatsOnly
    print('  ', FloatsOnly)
elif n == 2:
    from FileFormatMeanMenu import FloatsOnly
    print('  ', FloatsOnly)



