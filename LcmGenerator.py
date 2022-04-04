# LcmGenerator.py

from StandardModule import ModuleReload, Logo
from InputModule import IntInput, IntNum1, IntNum2, TooLarge, NonNegative, Switch, Loop
from importlib import reload

print()
print('  Find the L.C.M. of Two Numbers:')

int1 = IntNum1(None)
Max = 10000
for x in Loop:
    if int1 == NonNegative(int1):
        int1 = IntNum1(None)

    elif int1 == TooLarge(int1, Max):
        int1 = IntNum1(None)

int2 = IntNum2(None)
for x in Loop:
    if int2 == NonNegative(int2):
        int2 = IntNum2(None)

    elif int2 == TooLarge(int2, Max):
        int2 = IntNum2(None)

# Checks for the greater value of the 2 inputs
Max = max(int1, int2)

factors = range(1, Max * 2)
multiples1 = []
multiples2 = []

for factor in factors:
    multiples1.append(int1 * factor)
    multiples2.append(int2 * factor)
print()
print('  Multiples of', int1)
for multiples in multiples1:
    print(' ', multiples, end='')

print()
print()
print('  Multiples of', int2)
for multiples in multiples2:
    print(' ', multiples, end='')

print()
cms = []

for lcm in multiples1:
    if lcm in multiples2:
        cms.append(lcm)
print()
print('  The Common Multiples of ', int1, 'and', int2, 'are:')
for ComMults in cms:
    print(' ', ComMults, end='')

print()
print()
print('  The L.C.M. of', int1, 'and', int2, 'is :', cms[0])
# print(cms[0])

Logo()
ModuleReload()
n = None
n = IntInput(None)
Switch(n)

if n == 1:
    import LcmGenerator

    reload(LcmGenerator)

elif n == 2:
    import ExitMenu

    reload(ExitMenu)

import ExitMenu

reload(ExitMenu)
