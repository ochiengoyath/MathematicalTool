# MilesToKilometerConverter

from StandardModule import InputPrompt, ModuleReload, Logo
from InputModule import IntInput, NonNegative, Switch,  Loop
from importlib import reload

print()
print('  This Module Converts Distance Measurements from Miles to Kilometers and Vice Versa ')
print('  1. Miles to Kilometers''             ''2. Kilometers to Miles')

n = None
InputPrompt(n)
n = IntInput(None)

valid = [1, 2]
while n not in valid:
    print('  Valid Numbers Range from: 1 to 2')
    n = IntInput(None)


# mile to kilometer
# 1 mile = 0.621 kilometer
def MilesToKilometers(Mil):
    Kil = Mil / 0.621
    return Kil


# kilometer to mile
def KilometersToMiles(Kil):
    Mil = Kil * 0.621
    return Mil


def MilesInput(mile):
    mile = None
    while not mile:
        try:
            mile = float(input('  Enter Distance in Miles: '))
        except ValueError:
            print('  Invalid Input!, Please Enter a Number')
    return mile


def KilometersInput(kilometer):
    kilometer = None
    while not kilometer:
        try:
            kilometer = float(input('  Enter Distance in Kilometers: '))
        except ValueError:
            print('  Invalid Input!, Please Enter an Integer')
    return kilometer


for x in Loop:
    if n == 1:
        print()
        Miles = MilesInput(None)

        for i in Loop:
            if Miles == NonNegative(Miles):
                Miles = MilesInput(None)

        print(' ', Miles, ' Miles is:', round(MilesToKilometers(Miles), 3), 'Kilometers')
        break

for x in Loop:
    if n == 2:
        print()
        Kilometers = KilometersInput(None)

        for i in Loop:
            if Kilometers == NonNegative(Kilometers):
                Kilometers = KilometersInput(None)

        print(' ', Kilometers, ' Kilometers is:', round(KilometersToMiles(Kilometers), 3), 'Miles')
        break
Logo()
ModuleReload()
n = None
n = IntInput(None)
Switch(n)
if n == 1:
    import MilesToKilometerConverter
    reload(MilesToKilometerConverter)

elif n == 2:
    import ExitMenu
    reload(ExitMenu)

import ExitMenu
reload(ExitMenu)

