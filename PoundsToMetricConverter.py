# PoundsToMetricConverter

from StandardModule import InputPrompt, ModuleReload, Logo
from InputModule import IntInput, NonNegative,IntInput, Switch, Loop
from importlib import reload

print()
print('  This Module Converts Weight Measurements from Pounds to Metrics and Vice versa')
print('  1. Pounds to Metrics''        ''2. Metrics to Pounds')

n = None
InputPrompt(n)
n = IntInput(None)

valid = [1, 2]
while n not in valid:
    print('  Valid Numbers Range from: 1 to 2')
    n = IntInput(None)


# Pounds to Metrics
def PoundsToMetric(Pou):
    Kil = Pou * 2.2
    return Kil


# Metrics to Pounds
def MetricToPounds(Kil):
    Pou = Kil / 2.2
    return Pou


def PoundsInput(pound):
    pound = None
    while not pound:
        try:
            pound = float(input('  Enter Weight in pounds: '))
        except ValueError:
            print('  Invalid Input!, Please Enter a Number')
    return pound


def KiloInput(kilo):
    kilo = None
    while not kilo:
        try:
            kilo = float(input('  Enter Weight in Kilograms: '))
        except ValueError:
            print('  Invalid Input!, Please Enter a Number')
    return kilo


for x in Loop:
    if n == 1:
        pound = PoundsInput(None)
        for i in Loop:
            if pound == NonNegative(pound):
                pound = PoundsInput(None)

        print(' ', pound, ' Pounds is:', round(PoundsToMetric(pound), 3), 'Kilograms')
        break

for x in Loop:
    if n == 2:
        kilo = KiloInput(None)
        for i in Loop:
            if kilo == NonNegative(kilo):
                kilo = KiloInput(None)

        print(' ', kilo, ' kilograms is:', round(MetricToPounds(kilo), 3), 'Pounds')
        break

Logo()
ModuleReload()
n = None
n = IntInput(None)
Switch(n)
if n == 1:
    import PoundsToMetricConverter
    reload(PoundsToMetricConverter)

elif n == 2:
    import ExitMenu
    reload(ExitMenu)

import ExitMenu
reload(ExitMenu)

