# DecimalToPercentageConverter

from StandardModule import InputPrompt, ModuleReload, Logo
from InputModule import IntInput, NonNegative, Switch, Loop
from importlib import reload

print()
print('  This Module Converts Unit Formats from Decimals to Percentages and Vice Versa ')
print('  1. Decimal to Percentage''             ''2. Percentage to Decimals')

n = None
InputPrompt(n)
n = IntInput(None)

valid = [1, 2]
while n not in valid:
    print('  Valid Numbers Range from: 1 to 2')
    n = IntInput(None)


# Decimals to Percentage
def DecimalsToPercentage(Dec):
    Per = Dec * 100
    return Per


# Percentage to Decimal
def PercentageToDecimal(Per):
    Dec = Per / 100
    return Dec


def DecimalInput(decimal):
    decimal = None
    while not decimal:
        try:
            decimal = float(input('  Enter Value in Decimal: '))
        except ValueError:
            print('  Invalid Input!, Please Enter a Number')
    return decimal


def PercentInput(percent):
    percent = None
    while not percent:
        try:
            percent = float(input('  Enter Value in Percentage: '))
        except ValueError:
            print('  Invalid Input!, Please Enter a Number')
    return percent


for x in Loop:
    if n == 1:
        print()
        print('  Convert Decimal Value into Percentage')
        decimal = DecimalInput(None)

        for i in Loop:
            if decimal == NonNegative(decimal):
                decimal = DecimalInput(None)

        print(' ', decimal, ' is:', round(DecimalsToPercentage(decimal), 3), '%')
        break

for x in Loop:
    if n == 2:
        print()
        print('  Convert Percentage Value into Decimal')
        percent = PercentInput(None)

        for i in Loop:
            if percent == NonNegative(percent):
                percent = PercentInput(None)
        print(' ', percent, ' % is:', round(PercentageToDecimal(percent), 3), )
        break

print()
Logo()
ModuleReload()
n = None
n = IntInput(None)
Switch(n)

if n == 1:
    import DecimalToPercentageConverter

    reload(DecimalToPercentageConverter)

elif n == 2:
    import ExitMenu

    reload(ExitMenu)

import ExitMenu
reload(ExitMenu)
