# PerfectSquareRoots.py

from StandardModule import ModuleReload, Logo
from InputModule import IntInput, RangeFrom, RangeTo, NonNegative, GreaterThan, Switch, Loop
from math import sqrt
from importlib import reload

print()
print('  Calculate the Perfect Square Root of Numbers in a Range.')

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
        import PerfectSquareRoots
        reload(PerfectSquareRoots)
        import MainMenu
        reload(MainMenu)


sq = []
rt = []
for num in range(From, To):
    if sqrt(num) % 1 == 0:
        sq.append(num)
        rt.append(sqrt(num))

Rt = []
for x in rt:
    Rt.append(int(x))  # convert from float to integer

print('  These are the Perfect Squares Roots and their Products from', From, 'to', To)
print('  Square Roots:')
print('  ', Rt)
print()
print('  Numbers:')
print('  ', sq)
print()
print('  The Corresponding values of Square Roots and their Products are:(Square roots, Numbers)')
print('  ', list(zip(Rt, sq)))

Logo()
ModuleReload()
n = None
n = IntInput(None)
Switch(n)
if n == 1:
    import PerfectSquareRoots
    reload(PerfectSquareRoots)

elif n == 2:
    import ExitMenu
    reload(ExitMenu)

import ExitMenu
reload(ExitMenu)
