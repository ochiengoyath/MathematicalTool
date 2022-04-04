# PerimeterMenu.py

from StandardModule import ModuleReload, Logo
from InputModule import IntInput, NonNegative, Switch, Loop
from FormulaOfPolygons import TriPer, SquPer, RecPer, CirPer
from GeometryInput import Length1, Length2, Length3, Length, Width, Radius
from importlib import reload

print()
print('  Calculate the Perimeter of Polygons.')
print('  1. Triangle''     ''2. Square''   ''3. Rectangle''   ''4. Circle')

n = IntInput(None)
valid = [1, 2, 3, 4]
while n not in valid:
    print('  You\'ve entered an Invalid input')
    print('  Valid Numbers Range from: 1 to 4')
    n = IntInput(None)

if n == 1:
    print()
    print('  Calculate the Perimeter of a Triangle')

    len1 = Length1(None)
    for x in Loop:
        if len1 == NonNegative(len1):
            len1 = Length1(None)

    len2 = Length2(None)
    for x in Loop:
        if len2 == NonNegative(len2):
            len2 = Length2(None)

    len3 = Length3(None)
    for x in Loop:
        if len3 == NonNegative(len3):
            len3 = Length3(None)

    print('  Perimeter = Sum of 3 sides')
    print('  Perimeter = ', len1, '+', len2, '+', len3, '=', round(TriPer(len1, len2, len3), 2))


elif n == 2:
    print()
    print('  Calculate the Perimeter of a Square')

    length = Length(None)
    for x in Loop:
        if length == NonNegative(length):
            length = Length(None)

    print('  Perimeter = 4 X length')
    print('  Perimeter = 4 X', length, '=', round(SquPer(length), 2))


elif n == 3:
    print()
    print('  Calculate the Perimeter of a Rectangle')

    length = Length(None)
    for x in Loop:
        if length == NonNegative(length):
            length = Length(None)

    width = Width(None)
    for x in Loop:
        if width == NonNegative(width):
            width = Width(None)

    print('  Perimeter = (length + width) X 2')
    print('  Perimeter = (', length, '+', width, ') X 2 =', round(RecPer(length, width), 2))


elif n == 4:
    print()
    print('  Calculate the Circumference of a Circle')

    radius = Radius(None)
    for x in Loop:
        if radius == NonNegative(radius):
            radius = Radius(None)

    print('  Circumference = 2 X "pie" X Radius')
    print('  Circumference = 2 X 3.14 X', radius, '=', round(CirPer(radius)))

Logo()
ModuleReload()
n = None
n = IntInput(None)
Switch(n)
if n == 1:
    import PerimeterMenu
    reload(PerimeterMenu)

elif n == 2:
    import ExitMenu
    reload(ExitMenu)

import ExitMenu
reload(ExitMenu)
