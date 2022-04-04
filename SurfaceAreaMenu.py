# SurfaceAreaMenu

from StandardModule import InputPrompt, ModuleReload, Logo
from InputModule import IntInput, NonNegative, Switch, Loop
from FormulaOfPolygons import TetSur, CubSur, CuboSur, SphSur, CylSur, ConSur, SqPyrSur, RePyrSur
from GeometryInput import EdgeLength, Slope, Length, Width, Height, Radius
from importlib import reload

print()
print('  Calculate the Surface Area of Solids.')
print('  1. Tetrahedron''    ''2. Cube''     ''3. Cuboid''     ''4. Sphere''     ''5. Cylinder''     ')
print('  6. Cone''           ''7. Square Pyramid''         ''8. Rectangular Pyramid')

n = None
InputPrompt(n)
n = IntInput(None)

valid = [1, 2, 3, 4, 5, 6, 7, 8]
while n not in valid:
    print('  Valid Numbers Range from: 1 to 7')
    n = IntInput(None)

if n == 1:
    print()
    print('  Calculate the Surface Area of a Regular Tetrahedron')
    print('  The edges are all equal')

    edgeLength = EdgeLength(None)
    for x in Loop:
        if edgeLength == NonNegative(edgeLength):
            edgeLength = EdgeLength(None)

    print('  Surface Area = (Edge ** 2) X (square root of 3)')
    print('  Surface Area = (', edgeLength, '** 2) X (3 ** 0.5) =', round(TetSur(edgeLength), 2))

if n == 2:
    print()
    print('  Calculate the Surface Area of a Cube')

    length = Length(None)
    for x in Loop:
        if length == NonNegative(length):
            length = Length(None)

    print('  Surface Area = 6 X length ** 2')
    print('  Surface Area = 6 X ', length ** 2, '=', round(CubSur(length), 2))

elif n == 3:
    print()
    print('  Calculate the Surface Area of a Cuboid')

    length = Length(None)
    for x in Loop:
        if length == NonNegative(length):
            length = Length(None)

    width = Width(None)
    for x in Loop:
        if width == NonNegative(width):
            width = Width(None)

    height = Height(None)
    for x in Loop:
        if height == NonNegative(height):
            height = Height(None)

    print('  Surface Area = 2(length X width) + 2(length X height)+ 2(width X height)')
    print('  Surface Area = 2(', length, 'X', width, ')+ 2(', length, 'X', height, ')+ 2(', width, 'X', height, ')=',
          round(CuboSur(length, width, height), 2))

elif n == 4:
    print()
    print('  Calculate the Surface Area of a Sphere')

    radius = Radius(None)
    for x in Loop:
        if radius == NonNegative(radius):
            radius = Radius(None)

    print('  Surface Area = 4 X "pie" X radius ** 2')
    print('  Surface Area = 4 X 3.14 X ', radius ** 2, '=', round(SphSur(radius), 2))

elif n == 5:
    print()
    print('  Calculate the Surface Area of a Cylinder')

    radius = Radius(None)
    for x in Loop:
        if radius == NonNegative(radius):
            radius = Radius(None)

    height = Height(None)
    for x in Loop:
        if height == NonNegative(height):
            height = Height(None)

    print('  Surface Area = 2 X "pie" X radius **2 + 2 X "pie" X radius X height')
    print('  Surface Area = 2 X 3.14 X ', radius ** 2, '+ 2 X 3.14 X ', radius, 'X', height, '=',
          round(CylSur(radius, height), 2))

elif n == 6:
    print()
    print('  Calculate the Surface Area of a Regular Cone')

    radius = Radius(None)
    for x in Loop:
        if radius == NonNegative(radius):
            radius = Radius(None)

    slope = Slope(None)
    for x in Loop:
        if slope == NonNegative(slope):
            slope = Slope(None)

    print('  Surface Area = "pie" X Radius**2 + 2 X "pie" X Radius X Slope')
    print('  Surface Area = 3.14 X ', radius ** 2, '+ 2 X 3.14 X ', radius, 'X', slope, '=',
          round(ConSur(radius, slope), 2))

elif n == 7:
    print()
    print('  Calculate the Surface Area of a Right Square Pyramid ')

    length = Length(None)
    for x in Loop:
        if length == NonNegative(length):
            length = Length(None)

    slope = Slope(None)
    for x in Loop:
        if slope == NonNegative(slope):
            slope = Slope(None)

    height = Height(None)
    for x in Loop:
        if height == NonNegative(height):
            height = Height(None)

    print('  Surface Area = Length**2 + 2 X Slope X Height')
    print('  Surface Area =', length ** 2, 'X', '+ 2 X', slope, 'X', height, '=',
          round(SqPyrSur(length, slope, height), 2))


elif n == 8:
    print()
    print('  Calculate the Surface Area of a Right Rectangular Pyramid ')

    length = Length(None)
    for x in Loop:
        if length == NonNegative(length):
            length = Length(None)

    width = Width(None)
    for x in Loop:
        if width == NonNegative(width):
            width = Width(None)

    slope = Slope(None)
    for x in Loop:
        if slope == NonNegative(slope):
            slope = Slope(None)

    height = Height(None)
    for x in Loop:
        if height == NonNegative(height):
            height = Height(None)

    print('  Surface Area = (Length X Width) + (Width X Height) + (2 X Length X Slope)')
    print('  Surface Area =', (length * width), '+', (width * height), '+', (2 * length * slope), '=',
          round(RePyrSur(length, width, height, slope), 2))

Logo()
ModuleReload()
n = None
n = IntInput(None)
Switch(n)

if n == 1:
    import SurfaceAreaMenu

    reload(SurfaceAreaMenu)

elif n == 2:
    import ExitMenu

    reload(ExitMenu)

import ExitMenu
reload(ExitMenu)
