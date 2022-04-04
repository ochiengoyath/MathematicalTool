# MeanMedianModeTxt.py

from StandardModule import ModuleReload, Logo
from InputModule import IntInput, Loop, Switch
from TxtDataProcessorMean import FloatsOnly
from importlib import reload
from math import ceil

print()
print('  The Summary is as follows.')
print('  Data Set')

total = 0
index = 0
print('  Index', ' ', 'value', '         ', 'Sum Total', '       ', 'Mean', '     ', 'Counts')
for value in FloatsOnly:
    total = round(total + value, 2)
    index = round(index + 1, 2)
    mean = round(total / index, 2)
    count = FloatsOnly.count(value)
    print('  ', index, '    ', value, '           ', total, '          ', mean, '        ', count)

print()

# print('The Average is:')
# Average = total/index
# print(Average)
Mean = sum(FloatsOnly) / len(FloatsOnly)
FloatsOnlySorted = sorted(FloatsOnly)

Index = []
Value = []
Count = []
for val in FloatsOnlySorted:
    pos = FloatsOnlySorted.index(val)
    Index.append(pos)
    Value.append(val)
    Count.append(FloatsOnlySorted.count(val))
# print(Index)
# print(Value)
print()

TupList = (list(zip(Index, Value, Count)))

# print(TupList)
Center = len(Index)
Middle = ceil(Center / 2)
# print('Middle is ', Middle)
Most = max(Count)
# print('most count is', Most)

print('  The Mean of the values is :', round(Mean, 2))
for Val in TupList:
    if Middle <= Val[0]:
        print('  The Median of the values is :', round(Val[1], 2))
        break

for Val in TupList:
    if Most == Val[2]:
        print('  The Mode of the values is :', round(Val[1], 2))
        break

"""
print('  The Mean of the values is : % s ' % round(statistics.mean(FloatsOnly), 2))
print('  The Median of the values is : % s ' % round(statistics.median(FloatsOnly), 2))
print('  The Mode of the values is : % s ' % round(statistics.mode(FloatsOnly), 2))
"""
Max = max(FloatsOnly)
Min = min(FloatsOnly)

print()
print('  The Maximum Value is:', round(Max, 2))
print('  The Minimum Value is:', round(Min, 2))
print('  The Data Range is:', round(Max - Min, 2))

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
