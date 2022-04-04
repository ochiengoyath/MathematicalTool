# GeometryMenu.py

from StandardModule import InputPrompt
from InputModule import IntInput, Loop
from importlib import reload

print()

print('  This Module Calculates Various Dimension in Polygons ')
n = None
InputPrompt(n)
print('  1. Area of Polygons''        ''2. Perimeter of Polygons')
print('  3. Volume of Solids''       '' 4. Surface Area of Solids')

n = IntInput(None)
valid = [1, 2, 3, 4]
while n not in valid:
    print('  You\'ve entered an Invalid input')
    print('  Valid Numbers Range from: 1 to 4')
    n = IntInput(None)

for x in Loop:
    if n == 1:
        import AreaMenu
        reload(AreaMenu)

    elif n == 2:
        import PerimeterMenu
        reload(PerimeterMenu)

    elif n == 3:
        import VolumeMenu
        reload(VolumeMenu)

    elif n == 4:
        import SurfaceAreaMenu
        reload(SurfaceAreaMenu)
