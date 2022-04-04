# SquaresAndRootsMenu.py

from StandardModule import InputPrompt
from InputModule import IntInput
from importlib import reload

print()
print('  This Module Returns Perfect Squares and Perfect Square roots of Whole Numbers .')

n = None
n = InputPrompt(n)
print('  1. Perfect Squares''          ''2.Perfect Square Roots')

n = IntInput(None)

valid = [1, 2]
while n not in valid:
    print('  Valid Numbers Range from: 1 to 2')
    n = IntInput(None)

if n == 1:
    import PerfectSquares
    reload(PerfectSquares)

elif n == 2:
    import PerfectSquareRoots
    reload(PerfectSquareRoots)
