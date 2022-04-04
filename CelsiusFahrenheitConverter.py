#  CelsiusFahrenheitConverter

from StandardModule import InputPrompt, ModuleReload, Logo
from InputModule import IntInput, Switch, Loop
from importlib import reload

print()
print('  This Module Makes Temperature Conversions from  Celsius to Fahrenheit and Vice Versa')
print('  1. Celsius to Fahrenheit''        ''2.  Fahrenheit to Celsius')
n = None

InputPrompt(n)
n = IntInput(None)

valid = [1, 2]
while n not in valid:
    print('  Valid Numbers Range from: 1 to 2')
    n = IntInput(None)


# Celsius to Fahrenheit
def CelsiusToFahrenheit(Cel):
    Fah = (Cel * 9 / 5) + 32
    return Fah


# Fahrenheit To Celsius
def FahrenheitToCelsius(Fah):
    Cel = (Fah - 32) * 5 / 9
    return Cel


def CelsiusInput(celsius):
    celsius = None
    while not celsius:
        try:
            celsius = float(input('  Enter Temperature in Celsius: '))
        except ValueError:
            print('  Invalid Input! Please Enter a Number')
    return celsius


def FahrenheitInput(fahrenheit):
    fahrenheit = None
    while not fahrenheit:
        try:
            fahrenheit = float(input('  Enter Temperature in Fahrenheit: '))
        except ValueError:
            print('  Invalid Input!, Please Enter a Number')
    return fahrenheit


for x in Loop:
    if n == 1:
        celsius = CelsiusInput(None)
        print(' ', celsius, ' Celsius is: Fahrenheit', round(CelsiusToFahrenheit(celsius), 3))
        break

for x in Loop:
    if n == 2:
        fahrenheit = FahrenheitInput(None)
        print(' ', fahrenheit, ' Fahrenheit is: Celsius', round(FahrenheitToCelsius(fahrenheit), 3))
        break

print()
Logo()
ModuleReload()
n = None
n = IntInput(None)
Switch(n)
if n == 1:
    import CelsiusFahrenheitConverter

    reload(CelsiusFahrenheitConverter)

elif n == 2:
    import ExitMenu

    reload(ExitMenu)

import ExitMenu

reload(ExitMenu)
