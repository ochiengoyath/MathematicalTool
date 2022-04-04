# FileFormatPopulationMenu.py

from InputModule import IntInput, Loop

print()
# This module chooses & opens imported files from various formats
print('  Choose file format to Import Data from.')
print('  1. csv file''    ''2. text file')

n = IntInput(None)

valid = [1, 2]
while n not in valid:
    print('  Valid Numbers Range from: 1 to 2')
    n = IntInput(None)

if n == 1:
    for x in Loop:
        try:
            from CsvDataProcessorPopulation import FloatsOnly
        except FileNotFoundError:
            print('  No file with such name in the Current Directory')

elif n == 2:
    for x in Loop:
        try:
            from TxtDataProcessorPopulation import FloatsOnly
        except FileNotFoundError:
            print('  No file with such name in the Current Directory')
