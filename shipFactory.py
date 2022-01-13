from battleship import Battleship
from carrier import Carrier
from cruiser import Cruiser
from destroyer import Destroyer
from submarine import Submarine

def createShip(type, x, y, direction):
    if type == 'A':
        return Carrier(x,y,direction)
    elif type == 'B':
        return Battleship(x,y,direction)
    elif type == 'C':
        return Cruiser(x,y,direction)
    elif type == 'D':
        return Destroyer(x,y,direction)
    elif type == 'S':
        return Submarine(x,y,direction)
    else:
        print(f"Unknown type {type}")
        return None