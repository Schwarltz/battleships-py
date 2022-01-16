from battleship import Battleship
from carrier import Carrier
from cruiser import Cruiser
from destroyer import Destroyer
from submarine import Submarine

def createShip(type, row, col, direction):
    '''
    Creates a ship matching starting parameters.

        Parameters:
            type (str): the type of ship being created.
            row (int): the row the ship should be placed in first.
            col (int): the column of the ship should be placed in first.
            direction (str): which way the ship should go (either horizontal or vertical).
        
        Returns:
            A Ship instance.
    '''
    if type == 'A':
        return Carrier(row, col, direction)
    elif type == 'B':
        return Battleship(row,col,direction)
    elif type == 'C':
        return Cruiser(row,col,direction)
    elif type == 'D':
        return Destroyer(row,col,direction)
    elif type == 'S':
        return Submarine(row,col,direction)
    else:
        print(f"Unknown type {type}")
        return None