# ConverterMenu

from StandardModule import InputPrompt
from InputModule import IntInput, Loop
from importlib import reload

print()
print('  This Module Converts Values Into Various Formats.')

n = None
InputPrompt(n)
print('  1. Fahrenheit/Celsius''          ''2. Miles/kilometers''        ''3. Yards/Meters')
print('  4. Decimals/Percentages''        ''5. Pounds/Kilogrammes')

n = IntInput(None)

valid = [1, 2, 3, 4, 5]
while n not in valid:
    print('  You\'ve entered an Invalid input')
    print('  Valid Numbers Range from: 1 to 5')
    n = IntInput(None)

if n == 1:
    import CelsiusFahrenheitConverter

    reload(CelsiusFahrenheitConverter)

elif n == 2:
    import MilesToKilometerConverter

    reload(MilesToKilometerConverter)

elif n == 3:
    import YardsToMetersConverter

    reload(YardsToMetersConverter)

elif n == 4:
    import DecimalToPercentageConverter

    reload(DecimalToPercentageConverter)

elif n == 5:
    import PoundsToMetricConverter

    reload(PoundsToMetricConverter)
