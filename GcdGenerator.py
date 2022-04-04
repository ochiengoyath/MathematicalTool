# GcdGenerator.py

from StandardModule import ModuleReload, Logo
from InputModule import IntNum1, IntNum2, IntInput, TooLarge, NonNegative, Switch, Loop
from math import gcd
from importlib import reload

print()
print('  Find the G.C.D of Two Numbers:')

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

factors = range(1, 10000)
divisors1 = []
divisors2 = []

for factor in factors:
    divisors1.append(int1 / factor)
    divisors2.append(int2 / factor)
print()
print('  Divisors of', int1)

IntMultiples1 = []  # filter non-whole divisors
for val in divisors1:
    if val % 1 == 0:
        IntMultiples1.append(int(val))  # int changes floats back to integers
SorMul1 = sorted(IntMultiples1)[1:]  # Remove 1 as a multiple by slicing
for mul1 in SorMul1:
    print(' ', mul1, end='')

print()
print()
print('  Divisors of', int2)

IntMultiples2 = []
for val in divisors2:
    if val % 1 == 0:
        IntMultiples2.append(int(val))

SorMul2 = sorted(IntMultiples2)[1:]  # Remove 1 as a multiple by slicing
for mul2 in SorMul2:
    print(' ', mul2, end='')

print()
print()
print('  The Common Divisors of', int1, 'and', int2, 'are:')
ComDivs = []
for divs in IntMultiples1:
    if divs in IntMultiples2:
        ComDivs.append(divs)

SorComDiv = sorted(ComDivs)[1:]  # Remove 1 as a multiple by slicing
for comdiv in SorComDiv:
    print(' ', comdiv, end='')

print()
print()
print('  The G.C.D. of', int1, 'and', int2, 'is :', gcd(int1, int2))

print()
Logo()
ModuleReload()
n = None
n = IntInput(None)
Switch(n)

if n == 1:
    import GcdGenerator

    reload(GcdGenerator)

elif n == 2:
    import ExitMenu

    reload(ExitMenu)

import ExitMenu
reload(ExitMenu)
