# TxtDataProcessorSampling.py

from InputModule import Loop
from importlib import reload

# This Module cleans Text data & returns a list of floats only
print()
print('  Save the file in current directory as txt')

FileName = str(input('  Enter the name of the file:'))
print()

x = ''.join((FileName, '.txt'))
lineList = []

try:
    with open(x) as file:
        for line in file:
            lineList.append(line)
except FileNotFoundError:
    print('  No file named ', x, 'in the current directory')
    print('  Enter any Key to reload module  ')
    input('  ')
    for i in Loop:
        import TxtDataProcessorSampling

        reload(TxtDataProcessorSampling)
        import ExitMenu
        reload(ExitMenu)

# print(lineList)

# Strip the white spaces
newLineList = []
for line in lineList:
    newLineList.append(line.rstrip('\n'))
# print(newLineList)

# split each line into list
bLineList = []
for b in newLineList:
    bLineList.append(b.splitlines())
# print(bLineList)
FinalList = []
for line in bLineList:
    for string in line:
        FinalList.append(string.split())
# print(FinalList)

# Create a single list
GrandList = []
for strings in FinalList:
    for string in strings:
        GrandList.append(string)
# print(GrandList)

# If numerical convert to float, if not pass
TestFloats = []
for s in GrandList:
    try:
        s = float(s)
    except ValueError:
        pass
    TestFloats.append(s)
# print(TestFloats)

# Collect floats only in final list
FloatsOnly = []
for x in TestFloats:
    if type(x) == float:
        FloatsOnly.append(x)

for i in Loop:
    if len(FloatsOnly) == 0:
        FloatsOnly.append(0)

print('  The following Data set is Imported from the text file.')
print('  ', FloatsOnly)
print()

import SetsOfRandomTxt
reload(SetsOfRandomTxt)
