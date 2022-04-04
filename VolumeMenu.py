# VolumeMenu

from StandardModule import ModuleReload, Logo
from InputModule import IntInput, NonNegative, Switch, Loop
from FormulaOfPolygons import TetVol, CubVol, CuboVol, SphVol, CylVol, ConVol, SqPyrVol, RePyrVol
from GeometryInput import Height, Length, Width, Radius, BaseLenth, BaseWidth, EdgeLength
from importlib import reload

print()
print('  Calculate the Volume of Solids.')
print('  1. Tetrahedron''    ''2. Cube''     ''3. Cuboid''     ''4. Sphere''     ''5. Cylinder''     ')
print('  6. Cone''           ''7. Square Pyramid''         ''8. Rectangular Pyramid')

n = IntInput(None)

valid = [1, 2, 3, 4, 5, 6, 7, 8]
while n not in valid:
    print('  You\'ve entered an Invalid input')
    print('  Valid Numbers Range from: 1 to 8')
    n = IntInput(None)

if n == 1:
    print()
    print('  Calculate the Volume of a Regular Tetrahedron')
    print('  All the edges are equal')
    edgeLength = EdgeLength(None)
    for x in Loop:
        if edgeLength == NonNegative(edgeLength):
            edgeLength = EdgeLength(None)

    print('  Volume = (Edge ** 3) / (6 X (2 ** 0.5))')
    print('  Volume = (', edgeLength, '** 3) / (6 X 1.414)  =', round(TetVol(edgeLength), 2))


elif n == 2:
    print()
    print('  Calculate the Volume of a Cube')

    length = Length(None)
    for x in Loop:
        if length == NonNegative(length):
            length = Length(None)

    print('  Volume = length**3')
    print('  Volume = ', length, '**3', '=', round(CubVol(length), 2))

elif n == 3:
    print()
    print('  Calculate the Volume of a Cuboid')

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

    print('  Volume = length X width X height')
    print('  Volume = ', length, 'X', width, 'X', height, '=', round(CuboVol(length, width, height), 2))

elif n == 4:
    print()
    print('  Calculate the Volume of a Sphere')

    radius = Radius(None)
    for x in Loop:
        if radius == NonNegative(radius):
            radius = Radius(None)

    print('  Volume = 4/3 X "pie" X radius**3')
    print('  Volume = 4/3 X 3.14 X', radius, '**3 =', round(SphVol(radius), 2))


elif n == 5:
    print()
    print('  Calculate the Volume of a Cylinder')

    radius = Radius(None)
    for x in Loop:
        if radius == NonNegative(radius):
            radius = Radius(None)

    height = Height(None)
    for x in Loop:
        if height == NonNegative(height):
            height = Height(None)

    print('  Volume = "pie" X radius**2 X height')
    print('  Volume = 3.14 X', radius, '**2 X', height, '=', round(CylVol(radius, height), 2))

elif n == 6:
    print()
    print('  Calculate the Volume of a Cone')

    radius = Radius(None)
    for x in Loop:
        if radius == NonNegative(radius):
            radius = Radius(None)

    height = Height(None)
    for x in Loop:
        if height == NonNegative(height):
            height = Height(None)

    print('  Volume = 1/3 X "pie" X Radius**2 X height')
    print('  Volume = 1/3 X 3.14 X', radius ** 2, 'X', height, '=', round(ConVol(radius, height), 2))

elif n == 7:
    print()
    print('  Calculate the Volume of a Square Pyramid')

    baselenth = BaseLenth(None)
    for x in Loop:
        if baselenth == NonNegative(baselenth):
            baselenth = BaseLenth(None)

    height = Height(None)
    for x in Loop:
        if height == NonNegative(height):
            height = Height(None)

    print('  Volume = 1/3 X base length ** 2 X height')
    print('  Volume = 1/3 X ', baselenth ** 2, 'X', height, '=', round(SqPyrVol(baselenth, height), 2))


elif n == 8:
    print()
    print('  Calculate the Volume of a Rectangular Pyramid')

    baselenth = BaseLenth(None)
    for x in Loop:
        if baselenth == NonNegative(baselenth):
            baselenth = BaseLenth(None)

    basewidth = BaseWidth(None)
    for x in Loop:
        if basewidth == NonNegative(basewidth):
            basewidth = BaseWidth(None)

    height = Height(None)
    for x in Loop:
        if height == NonNegative(height):
            height = Height(None)

    print('  Volume = (1/3 X base length X height) + (1/3 X base width X height)')
    print('  Volume = (1/3 X ', baselenth * height, ') + (1/3 X ', basewidth * height, ') =',
          round(RePyrVol(baselenth, basewidth, height), 2))

print()

Logo()
ModuleReload()
n = None
n = IntInput(None)
Switch(n)
if n == 1:
    import VolumeMenu

    reload(VolumeMenu)

elif n == 2:
    import ExitMenu

    reload(ExitMenu)

import ExitMenu
reload(ExitMenu)
