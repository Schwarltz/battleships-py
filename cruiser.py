from ship import Ship
from legend import Legend

class Cruiser(Ship):
    def __init__(self, x, y, direction):
        super().__init__(Legend.CRUISER, x, y, 3, direction)
        
    def getName(self):
        return 'Cruiser'