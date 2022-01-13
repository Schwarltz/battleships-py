from helpers import inputToPos
from position import Position

class Ship:
    def __init__(self, type, x, y, length, direction):
        self.type = type
        positions = inputToPos(x, y, length, direction)
        self.pos = dict.fromkeys(positions, False)
        

    '''
    Raises flag if both ships share a coordinate
    '''
    def isColliding(self, other):
        collisions = [x for x in self.pos if x in other.pos]
        return bool(collisions)

    '''
    Raises flag if there is a position that is out of bounds
    '''
    def inMap(self, sea):
        outOfBounds = [x for x in self.pos if not (0 <= x['x'] < sea.getWidth() and 0 <= x['y'] < sea.getHeight())]
        return not bool(outOfBounds)
    
    def isSunk(self):
        return not (False in self.pos.values())
            

    def getType(self):
        return self.type
    
    def getPos(self):
        return self.pos.keys()