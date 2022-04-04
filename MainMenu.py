# MainMenu.py

from StandardModule import InputPrompt
from InputModule import IntInput, Loop
from importlib import reload

print()
print('  Main Menu:')

n = None
InputPrompt(n)
print('  1. Calculator''        ''2. Generators''       ''3. Converters''      ''4. Geometry''      ''5. Statistics')
# print('  6. Trigonometry''      ''7. Calculus')


n = IntInput(None)
valid = [1, 2, 3, 4, 5]
while n not in valid:
    print('  Valid Numbers Range from: 1 to 5')
    n = IntInput(None)

if n == 1:
    for x in Loop:
        import Calculator
        reload(Calculator)


elif n == 2:
    import GeneratorMenu

    reload(GeneratorMenu)

elif n == 3:
    import ConverterMenu

    reload(ConverterMenu)

elif n == 4:
    import GeometryMenu

    reload(GeometryMenu)

elif n == 5:
    import StatisticsMenu

    reload(StatisticsMenu)

elif n == 6:
    pass

elif n == 7:
    pass
