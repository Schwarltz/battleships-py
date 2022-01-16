from ship import Ship
from legend import Legend

class Submarine(Ship):
    def __init__(self, x, y, direction):
        super().__init__(Legend.SUBMARINE, x, y, 3, direction)
        
    def getName(self):
        return 'Submarine'