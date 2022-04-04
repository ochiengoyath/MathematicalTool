# Calculator.py

from StandardModule import ModuleReload, Logo
from InputModule import FirstNumber, SecondNumber, IntInput, Switch, Loop
from importlib import reload

print()
print('  Arithmetic Calculator.')
print('  This Module Evaluates the value of Two Numbers')

num1 = FirstNumber(None)

op = None
ops = ['+', '-', '*', '/', '//', '%', '**']
print('  Valid Operators: (+,-,*,/,//,%,**)')
op = input('  Enter an Operator: ')
while op not in ops:
    print(' ', op, 'is not a valid operator')
    op = input('  Enter an Operator: ')

num2 = SecondNumber(None)

# print('  The Result is as follows.')
if op == '+':
    ans = (num1 + num2)
    print(' ', num1, op, num2, '=', round(ans, 3))

elif op == '-':
    ans = (num1 - num2)
    print(' ', num1, op, num2, '=', round(ans, 3))

elif op == '*':
    ans = (num1 * num2)
    print(' ', num1, op, num2, '=', round(ans, 3))

elif op == '/':
    ans = (num1 / num2)
    print(' ', num1, op, num2, '=', round(ans, 3))

elif op == '//':
    ans = (num1 // num2)
    print(' ', num1, op, num2, '=', round(ans, 3))

elif op == '%':
    ans = (num1 % num2)
    print(' ', num1, op, num2, '=', round(ans, 3))

elif op == '**':
    try:
        ans = (num1 ** num2)
    except OverflowError:
        print('  Number too large to Compute')
        for i in Loop:
            import Calculator

            reload(Calculator)
            import MainMenu
    else:
        print(' ', num1, op, num2, '=', round(ans, 3))

Logo()
ModuleReload()
n = None
n = IntInput(None)
Switch(n)
if n == 1:
    for x in Loop:
        import Calculator

        reload(Calculator)

elif n == 2:
    for x in Loop:
        import ExitMenu

        reload(ExitMenu)

import ExitMenu

reload(ExitMenu)
