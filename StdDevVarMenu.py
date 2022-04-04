# StdDevVarMenu.py

from StandardModule import InputPrompt
from InputModule import IntInput
from importlib import reload

print()
print('  This Module Calculates Distribution of Datasets: Standard Deviation and Variance ')
print('  1.Population Standard Deviation and Population Variance')
print('  2.Sample Standard Deviation and Sample Variance')
print()


n = InputPrompt(None)
n = IntInput(None)

valid = [1, 2, 3, 4]
while n not in valid:
    print('  You\'ve entered an Invalid input')
    print('  Valid Numbers Range from: 1 to 4')
    n = IntInput(None)


if n == 1:
    import PopulationStdVarMenu
    reload(PopulationStdVarMenu)

elif n == 2:
    import SampleStdVarMenu
    reload(SampleStdVarMenu)
