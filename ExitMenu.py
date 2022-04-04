# ExitMenu.py

from InputModule import Loop
from importlib import reload

for i in Loop:
    import MainMenu
    reload(MainMenu)




