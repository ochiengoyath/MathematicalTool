# Exponentials

from StandardModule import ModuleReload, Logo
from InputModule import IntInput, RangeOfNumbers, NonNegative, Switch, Loop
from importlib import reload

print()
print('  This Module Simulates Exponential Growth from a Base Value')
print('  Choose the Base Value')

n = IntInput(None)
for x in Loop:
    if n == NonNegative(n):
        n = IntInput(None)
print('  Choose the Range of Values')

Ran = RangeOfNumbers(None)
for x in Loop:
    if Ran == NonNegative(Ran):
        Ran = RangeOfNumbers(None)

print('  Choose the Power of Growth ie. Exponential ')
i = IntInput(None)
for x in Loop:
    if i == NonNegative(i):
        i = IntInput(None)

Exp = [n]

loop = range(Ran - 1)

for x in loop:
    try:
        Exp.append(Exp[-1] * i)
    except MemoryError:
        print('  Numbers too large to compute')
        x = input('  Enter any key to Reload Module ')
        import Exponentials
        reload(Exponentials)
        import MainMenu
        reload(MainMenu)

print()
print(' ', Ran, 'Times Growth of', n, 'by a Factor of', i, ':')
print(' ', Exp)

print()
Logo()
ModuleReload()
n = None
n = IntInput(None)
Switch(n)

if n == 1:
    import Exponentials
    reload(Exponentials)

elif n == 2:
    import ExitMenu
    reload(ExitMenu)

import ExitMenu
reload(ExitMenu)

