from ship import Ship
from legend import Legend

class Carrier(Ship):
    def __init__(self, x, y, direction):
        super().__init__(Legend.CARRIER, x, y, 5, direction)