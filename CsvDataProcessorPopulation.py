# CsvDataProcessorPopulation.py

from csv import reader
from InputModule import Loop
from importlib import reload

# This Module cleans Csv data & returns a list of floats only
print()
print('  Save the Spreed sheet file in current directory as csv')
FileName = str(input('  Enter the name of the file:'))

x = ''.join((FileName, '.csv'))
OneList = []
try:
    with open(x, 'r') as read_obj:

        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)

        # Pass reader object to list() to get a list of lists
        list_of_rows = list(csv_reader)
        # print(list_of_rows)

        for lists in list_of_rows:
            for List in lists:
                OneList.append(List)

except FileNotFoundError:
    print('  No file named ', x, 'in the current directory')
    print('  Enter any Key to reload module  ')
    input('  ')
    for i in Loop:
        import importlib
        import CsvDataProcessorPopulation

        importlib.reload(CsvDataProcessorPopulation)
        import ExitMenu

# print(OneList)

WithFloats = []
for s in OneList:
    try:
        s = float(s)
    except ValueError:
        pass
    WithFloats.append(s)
# print(WithFloats)

FloatsOnly = []
for x in WithFloats:
    if type(x) == float:
        FloatsOnly.append(x)

for i in Loop:
    if len(FloatsOnly) == 0:
        for r in range(2):
            FloatsOnly.append(0)

print()
print('  The following Data Set is Imported from the csv file.')
print('  ', FloatsOnly)

import PopulationStdVarCsv
reload(PopulationStdVarCsv)
