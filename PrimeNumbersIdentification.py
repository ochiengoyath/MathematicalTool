# PrimeNumbersIdentification.py

from StandardModule import ModuleReload, Logo
from InputModule import RangeFrom, RangeTo, NonNegative, GreaterThan, IntInput, Switch, Loop
from importlib import reload

print()
print('  Find Prime Numbers in a Range:')
print('  Enter the First Number')
From = RangeFrom(None)
for x in Loop:
    if From == NonNegative(From):
        From = RangeFrom(None)

print('  Enter the Last Number')
To = RangeTo(None)
for x in Loop:
    if To == NonNegative(To):
        To = RangeTo(None)

for i in Loop:
    if GreaterThan(From, To):
        x = input('  Enter Any Key to Reload Module')
        import PrimeNumbersIdentification
        reload(PrimeNumbersIdentification)
        import MainMenu
        reload(MainMenu)

PrimMax = To - From
for e in Loop:
    if PrimMax > 3000:
        print('  Please wait.....')
        break

prime = []
for n in range(From, To):
    numbs = range(2, n)
    nums = []
    for p in numbs:
        nums.append(p)
    floDivs = []
    for p in nums:
        floDivs.append(n % p)
    # print(floDivs)

    for prim in floDivs:
        if 0 not in floDivs:
            prime.append(n)
            break

# print(prime)
for p in prime:
    if p in prime:
        print()
        print('  These are the Prime Numbers between', From, 'and', To)
        break

for p in prime:
    print(' ', p, end='')
print()

Logo()
ModuleReload()
n = None
n = IntInput(None)
Switch(n)
if n == 1:
    import PrimeNumbersIdentification
    reload(PrimeNumbersIdentification)

elif n == 2:
    import ExitMenu
    reload(ExitMenu)

import ExitMenu
reload(ExitMenu)
