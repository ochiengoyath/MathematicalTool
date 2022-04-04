# PerfectSquares.py

from StandardModule import ModuleReload, Logo
from InputModule import RangeFrom, RangeTo, IntInput, GreaterThan, NonNegative,Switch,  Loop
from math import sqrt
from importlib import reload

print()
print('  Find the Perfect Squares from a Range of Numbers.')

From = RangeFrom(None)
for x in Loop:
    if From == NonNegative(From):
        From = RangeFrom(None)

To = RangeTo(None)
for x in Loop:
    if To == NonNegative(To):
        To = RangeTo(None)
for i in Loop:
    if GreaterThan(From, To):
        input('  Enter Any Key to Reload Module')
        import PerfectSquares
        reload(PerfectSquares)
        import MainMenu
        reload(MainMenu)


perfect = []
for num in range(From, To):
    if num ** 0.5 % 1 == 0:
        perfect.append(num)

print('  These are the Perfect Squares from', From, 'to', To)
print('  ', perfect)

rt = []
for x in perfect:
    rt.append(sqrt(x))
Rt = []
for y in rt:
    Rt.append(int(y))

print()
print('  The Corresponding Values of Perfect Squares and their Square Roots are:(Perfect Squares,Square roots)')
print('  ', list(zip(perfect, Rt)))

Logo()
ModuleReload()
n = None
n = IntInput(None)
Switch(n)
if n == 1:
    import PerfectSquares
    reload(PerfectSquares)

elif n == 2:
    import ExitMenu
    reload(ExitMenu)

import ExitMenu
reload(ExitMenu)
