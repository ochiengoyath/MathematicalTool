# FibonacciNumbers

from StandardModule import ModuleReload, Logo
from InputModule import FirstNumber, SecondNumber, IntInput, RangeOfNumbers, TooLarge, FltIntConverter, NonNegative, Switch, Loop
from importlib import reload

print()
print('  This Module Produces a Series of Numbers in which Each Number is the Sum of the Two Previous Ones.')
print('  Also Called Fibonacci Numbers')

Range = 1000

num1 = FirstNumber(None)
num2 = SecondNumber(None)
num1 = FltIntConverter(num1)
num2 = FltIntConverter(num2)
Ran = RangeOfNumbers(None)
for x in Loop:
    if TooLarge(Ran, Range):
        Ran = RangeOfNumbers(None)
    elif NonNegative(Ran):
        Ran = RangeOfNumbers(None)

fibs = [num1, num2]
for i in range(Ran):
    fibs.append(fibs[-2] + fibs[-1])
print(' ', Ran, 'Series of Numbers after', num1, 'and', num2, ':')
RoundFibs = []
for Round in fibs:
    RoundFibs.append(round(Round, 2))

print(' ', RoundFibs)

print()
Logo()
ModuleReload()
n = None
n = IntInput(None)
Switch(n)

if n == 1:
    import FibonacciNumbers

    reload(FibonacciNumbers)

elif n == 2:
    import ExitMenu

    reload(ExitMenu)

import ExitMenu
reload(ExitMenu)


