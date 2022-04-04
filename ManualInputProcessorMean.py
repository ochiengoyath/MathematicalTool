# ManualInputProcessorMean.py
from InputModule import Loop
from importlib import reload

# This module returns input data as a list of floats only
print()
ListArrays = []
a = list(input('  Enter the Data Separated by a Space: ').split())
for val in a:
    ListArrays.append(val)

# print(ListArrays)

ConvertToFloats = []
for f in ListArrays:
    try:
        f = float(f)
    except ValueError:
        pass
    ConvertToFloats.append(f)

FloatsOnly = []
for s in ConvertToFloats:
    if type(s) == float:
        FloatsOnly.append(s)
for i in Loop:
    if len(FloatsOnly) == 0:
        FloatsOnly.append(0)


print('  The following is your Data set.')
print('  ', FloatsOnly)

import MeanMedianModeManual
reload(MeanMedianModeManual)

