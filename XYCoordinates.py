# XYCoordinates.py

from StandardModule import ModuleReload, Logo
from InputModule import IntInput, RangeFrom, RangeTo, Interval, NonNegative, GreaterThan, TooLarge, Switch,  Loop
from importlib import reload

# To calculate corresponding y co-ordinates
print()
print('  This Module Returns Corresponding Values of Y in an Equation from Given Set of X-Coordinates')
print('  Enter the Co-ordinates of X:')

Max = 10000
From = RangeFrom(None)
for x in Loop:
    if TooLarge(From, Max):
        From = RangeFrom(None)

To = RangeTo(None)
for x in Loop:
    if TooLarge(To, Max):
        To = RangeTo(None)

for i in Loop:
    if GreaterThan(From, To):
        input('  Enter any key to Reload Module ')
        import XYCoordinates
        reload(XYCoordinates)
        import ExitMenu
        reload(ExitMenu)

Of = Interval(None)
for e in Loop:
    if Of == NonNegative(Of):
        Of = Interval(None)

# Guarantees at least 2 data points
InterCheck = To - From - 2

# Checks that Interval is not out of range
for e in Loop:
    if TooLarge(Of, InterCheck):
        Of = Interval(None)

Xcoods = list(range(From, To, Of))
print()
print('  You\'ve entered the following X coordinates.')
print('  ''X:', Xcoods)
print()
print('  Enter the y equation:(e.g. for y = 2X + 7, enter \'2*x + 7\' )')

StrInput = input('  y = ')

Ycoods = []
for x in Xcoods:
    for i in Loop:  # iterates evaluation until the correct format is entered
        try:  # evaluates if and only if the format is correct
            i = (eval(StrInput))
        except NameError:
            print(' ', StrInput, 'is an Invalid Format. For example; for \'3x - 5\', enter \'3*x - 5\'')
            print('  Enter the correct format')
            StrInput = input('  y = ')

    Ycoods.append(round(i))
print('  For equation: y = ', StrInput)
print('  The following are the Corresponding Y coordinates.')
print('  Y:', Ycoods)

print()
print('  The corresponding values of X & Y are:')
print('  (X,Y)', list(zip(Xcoods, Ycoods)))

print()
Logo()
ModuleReload()
n = None
n = IntInput(None)
Switch(n)

if n == 1:
    import XYCoordinates
    reload(XYCoordinates)

elif n == 2:
    import ExitMenu
    reload(ExitMenu)

import ExitMenu
reload(ExitMenu)

