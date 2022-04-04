# AreaMenu.py

from StandardModule import InputPrompt, ModuleReload, Logo
from InputModule import IntInput, NonNegative, Switch, Loop
from FormulaOfPolygons import TriAre, SquAre, RecAre, CirAre
from GeometryInput import Base, Height, Length, Width, Radius
from importlib import reload

print()
print('  Calculate the Area of Polygons.')
print('  1. Triangle''     ''2. Square''   ''3. Rectangle''   ''4. Circle')

n = None
InputPrompt(n)

n = IntInput(None)
valid = [1, 2, 3, 4]
while n not in valid:
    print('  Valid Numbers Range from: 1 to 4')
    n = IntInput(None)

if n == 1:
    print()
    print('  Calculate the Area of a Triangle')

    base = Base(None)
    for x in Loop:
        if base == NonNegative(base):
            base = Base(None)

    height = Height(None)
    for x in Loop:
        if height == NonNegative(height):
            height = Height(None)

    print('  Area = 1/2 X Base X Height')
    print('  Area = 1/2 X ', base, 'X', height, '=', round(TriAre(base, height), 2))

elif n == 2:
    print()
    print('  Calculate the Area of a Square')

    length = Length(None)
    for x in Loop:
        if length == NonNegative(length):
            length = Length(None)
    print('  Area = Length ** 2')
    print('  Area =', length, '** 2 =', round(SquAre(length), 2))

elif n == 3:
    print()
    print('  Calculate the Area of a Rectangle')

    length = Length(None)
    for x in Loop:
        if length == NonNegative(length):
            length = Length(None)

    width = Width(None)
    for x in Loop:
        if width == NonNegative(width):
            width = Width(None)

    print('  Area = Length X Width')
    print('  Area =', length, 'X', width, '=', round(RecAre(length, width), 2))

elif n == 4:
    print()
    print('  Calculate the Area of a Circle')

    radius = Radius(None)
    for x in Loop:
        if radius == NonNegative(radius):
            radius = Radius(None)

    print('  Area =  "pie" X radius ** 2')
    print('  Area =  3.14 X (', radius, '** 2) =', round(CirAre(radius), 2))

Logo()
ModuleReload()
n = None
n = IntInput(None)
Switch(n)

if n == 1:
    import AreaMenu
    reload(AreaMenu)

elif n == 2:
    import ExitMenu
    reload(ExitMenu)

import ExitMenu
