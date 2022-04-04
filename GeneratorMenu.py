# GeneratorMenu.py

from StandardModule import InputPrompt, ModuleReload
from InputModule import IntInput, Loop
from importlib import reload

print()
print('  This Module Generates Values from Various Concepts.')

print('  1. Least Common Multiples(L.C.M) and Greatest Common Divisors (G.C.D)''    ''2. Perfect Squares and Roots')
print('  3. Prime Numbers''        ''4. Factorials''        ''5. Fibonacci Numbers''        ''6. Exponentials')

n = None
InputPrompt(n)
n = IntInput(None)

valid = [1, 2, 3, 4, 5, 6]
while n not in valid:
    print('  You\'ve entered an Invalid input')
    print('  Valid Numbers Range from: 1 to 6')
    n = IntInput(None)

for x in Loop:
 if n == 1:
    import LCM_GCDMenu
    reload(LCM_GCDMenu)

 elif n == 2:
    import SquaresAndRootsMenu
    reload(SquaresAndRootsMenu)

 elif n == 3:
    import PrimeNumbersIdentification
    reload(PrimeNumbersIdentification)

 elif n == 4:
    import FactorialsMenu
    reload(FactorialsMenu)

 elif n == 5:
    import FibonacciNumbers
    reload(FibonacciNumbers)

 elif n == 6:
    import Exponentials
    reload(Exponentials)
