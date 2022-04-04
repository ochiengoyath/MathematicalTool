# YardsToMetersConverter

from StandardModule import InputPrompt, ModuleReload, Logo
from InputModule import IntInput, NonNegative, Switch, Loop
from importlib import reload

print()
print('  This Module Converts Length Measurements from Yards to Meters and Vice Versa ')
print('  1. Yards to Meters''             ''2. Meters to Yards')

n = None
InputPrompt(n)
n = IntInput(None)

valid = [1, 2]
while n not in valid:
    print('  Valid Numbers Range from: 1 to 2')
    n = IntInput(None)


# Yards to Meters
def YardsToMeters(Yar):
    Met = Yar / 1.094
    return Met


# Meters to Yards
def MetersToYards(Met):
    Yar = Met * 1.094
    return Yar


def YardsInput(yard):
    yard = None
    while not yard:
        try:
            yard = float(input('  Enter Length in Yards: '))
        except ValueError:
            print('  Invalid Input!, Please Enter a Number')
    return yard


def MetersInput(meter):
    meter = None
    while not meter:
        try:
            meter = float(input('  Enter Length in Meters: '))
        except ValueError:
            print('  Invalid Input!, Please Enter a Number')
    return meter


for x in Loop:
    if n == 1:
        yard = YardsInput(None)

        for i in Loop:
            if yard == NonNegative(yard):
                yard = YardsInput(None)

        print(' ', yard, ' Yards is:', round(YardsToMeters(yard), 3), 'Meters')
        break

for x in Loop:
    if n == 2:
        meter = MetersInput(None)

        for i in Loop:
            if meter == NonNegative(meter):
                meter = MetersInput(None)

        print(' ', meter, ' Meters is:', round(MetersToYards(meter), 3), 'Yards')
        break

print()

Logo()
ModuleReload()
n = None
n = IntInput(None)
Switch(n)

if n == 1:
    import YardsToMetersConverter
    reload(YardsToMetersConverter)

elif n == 2:
    import ExitMenu
    reload(ExitMenu)

import ExitMenu
reload(ExitMenu)


