# FactorialsMenu.py

from StandardModule import InputPrompt, ModuleReload, Logo
from InputModule import IntInput, IntNum1, IntNum2, NonNegative, TooLarge, GreaterThan, Switch, Loop
from math import factorial
from importlib import reload

print()
print('  This Module Calculates Factorials, Permutations and Combinations from a Set of Items')
print('  1. Factorials''     ''2. Permutations''     ''3. Combinations')

n = None
InputPrompt(n)
n = IntInput(None)

valid = [1, 2, 3]
while n not in valid:
    print('  Valid Numbers Range from: 1 to 3')
    n = IntInput(None)

Max = 10000
if n == 1:
    print()
    print('  Factorials of a Given Number is:')
    print('  How many times can items of a given number be arranged ?')

    n = IntInput(None)
    for x in Loop:
        if n == NonNegative(n):
            n = IntInput(None)

    for i in Loop:
        if n == TooLarge(n, Max):
            n = IntInput(None)

    i = n
    val = i
    FactoList = [val, ]
    for num in range(1, i):
        i -= 1
        FactoList.append(i)

    print(' ', val, 'Factorials is the product of:')
    print(' ', FactoList)
    print()
    print(' ', val, 'Factorials is:', (factorial(n)))

elif n == 2:
    print()
    print('  Permutation of a Set is:')
    print('  How Many Ordered Set of Items can be arranged from a Pool ?')
    print('  Enter the Total Number of Items')

    Total = IntNum1(None)
    for x in Loop:
        if Total == NonNegative(Total):
            Total = IntNum1(None)

    for i in Loop:
        if Total == TooLarge(Total, Max):
            Total = IntInput(None)

    print('  Enter the Set Number of Items')

    Set = IntNum2(None)
    for x in Loop:
        if Set == NonNegative(Set):
            Set = IntNum1(None)

    for i in Loop:
        if Set == TooLarge(Set, Max):
            Set = IntInput(None)

    for r in Loop:
        if GreaterThan(Set, Total):
            input('  Enter any key to Reload Module ')
            import FactorialsMenu

            reload(FactorialsMenu)
            import ExitMenu
            reload(FactorialsMenu)

    print(' ', Total, 'Permutation ', Set, '=', Total, '! /(', Total, '-', Set, '!) = ', Total, '!/', Total - Set,
          '!')

    perm = (factorial(Total)) / (factorial(Total - Set))
    print(' ', Total, 'Permutation ', Set, 'is:', perm)


elif n == 3:
    print()
    print('  Combination of a Set is:')
    print('  How Many Un-ordered Set of Items can be Arranged from a Pool ?')
    print('  Enter the Total Number of Items')

    Total = IntNum1(None)
    for x in Loop:
        if Total == NonNegative(Total):
            Total = IntNum1(None)

    for i in Loop:
        if Total == TooLarge(Total, Max):
            Total = IntInput(None)

    print('  Enter the Set Number of Items')

    Set = IntNum2(None)
    for x in Loop:
        if Set == NonNegative(Set):
            Set = IntNum1(None)

    for i in Loop:
        if Set == TooLarge(Set, Max):
            Set = IntInput(None)

    for r in Loop:
        if GreaterThan(Set, Total):
            input('  Enter any key to Reload Module ')
            import importlib
            import FactorialsMenu

            importlib.reload(FactorialsMenu)
            import ExitMenu

    print(' ', Total, 'Combination ', Set, '=', Total, '!/ (', Total, '-', Set, ')! X', Set, '! = ', Total, '!/ (',
          Set,
          '! X', Total - Set, '!)')
    comb = (factorial(Total)) / (factorial(Set))*(factorial(Total - Set))
    print(' ', Total, 'Combination ', Set, 'is:', comb)

print()
Logo()
ModuleReload()
n = None
n = IntInput(None)
Switch(n)

if n == 1:
    import FactorialsMenu

    reload(FactorialsMenu)

elif n == 2:
    import ExitMenu

    reload(ExitMenu)

import ExitMenu
reload(ExitMenu)
