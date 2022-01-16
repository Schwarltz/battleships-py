from ship import Ship
from legend import Legend

class Destroyer(Ship):
    def __init__(self, x, y, direction):
        super().__init__(Legend.DESTROYER, x, y, 2, direction)
        
    def getName(self):
        return 'Destroyer'