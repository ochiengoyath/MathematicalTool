# DataAccessPopulationMenu.py

# This module chooses & opens imported files from various formats
from InputModule import IntInput
from importlib import reload

print()
print('  Choose file format to Import Data from.')
print('  1. csv file''    ''2. text file')

n = IntInput(None)

valid = [1, 2]
while n not in valid:
    print('  Valid Numbers Range from: 1 to 2')
    n = IntInput(None)

if n == 1:
    import CsvDataProcessorPopulation

    reload(CsvDataProcessorPopulation)

elif n == 2:
    import TxtDataProcessorPopulation

    reload(TxtDataProcessorPopulation)
