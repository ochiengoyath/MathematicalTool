#  LCM_GCDMenu

from StandardModule import InputPrompt
from InputModule import IntInput, Loop
from importlib import reload

print()
print('  To find the L.C.M. or the G.C.D. of Two Numbers')

n = None
InputPrompt(n)
print('  1. L.C.M.''    ''2. G.C.D')

n = IntInput(None)

valid = [1, 2]
while n not in valid:
    print('  Valid Numbers Range from: 1 to 2')
    n = IntInput(None)

if n == 1:
    import LcmGenerator

    reload(LcmGenerator)

elif n == 2:
    import GcdGenerator

    reload(GcdGenerator)
