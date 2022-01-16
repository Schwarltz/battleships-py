from ship import Ship
from legend import Legend

class Battleship(Ship):
    def __init__(self, x, y, direction):
        super().__init__(Legend.BATTLESHIP, x, y, 4, direction)

    def getName(self):
        return 'Battleship'