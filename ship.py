from helpers import inputToPos
from position import Position
from legend import Legend

class Ship:
    def __init__(self, type, row, col, length, direction):
        self.type = type
        positions = inputToPos(row, col, length, direction)
        self.positions = dict.fromkeys(positions, False)
        
    '''
    Raises flag if both ships share a coordinate
    '''
    def isColliding(self, other):
        collisions = [x for x in self.positions if x in other.positions]
        return bool(collisions)

    '''
    Raises flag if there is a position that is out of bounds
    '''
    def inMap(self, sea):
        outOfBounds = [x for x in self.positions.keys() if not (0 <= x.getX() < sea.getWidth() and 0 <= x.getY() < sea.getHeight())]
        return not bool(outOfBounds)
    
    '''
    Raise flag if all sections are hit 
    '''
    def isSunk(self):
        return not (False in self.positions.values())

    '''
    Returns a flag for success if the ship is hit
    '''
    def getHit(self, pos):
        if pos in self.positions:
            self.positions[pos] = True
            return True
        return False

    def getType(self):
        return self.type
    
    def getPos(self):
        return self.positions.keys()
    
    def getValAtPos(self,pos):
        return self.positions.get(pos)

    def getName():
        raise NotImplementedError('Please implement this.')
