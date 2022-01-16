from helpers import inputToPos
from position import Position
from legend import Legend

class Ship:
    def __init__(self, type, row, col, length, direction):
        self.type = type
        positions = inputToPos(row, col, length, direction)
        self.positions = dict.fromkeys(positions, False)
        
    
    def isColliding(self, other):
        '''Raises flag if both ships share a coordinate.'''
        collisions = [x for x in self.positions if x in other.positions]
        return bool(collisions)

    
    def inMap(self, sea):
        '''Raises flag if there is a position that is out of bounds.'''
        outOfBounds = [x for x in self.positions.keys() if not (0 <= x.getX() < sea.getWidth() and 0 <= x.getY() < sea.getHeight())]
        return not bool(outOfBounds)
    
    def isSunk(self):
        '''Raise flag if all sections are hit.'''
        return not (False in self.positions.values())


    def getHit(self, pos):
        '''Raises flag if the ship is successfully hit.'''
        if pos in self.positions:
            self.positions[pos] = True
            return True
        return False

    def getType(self):
        return self.type
    
    def getPos(self):
        return self.positions.keys()

    def getUnhitPositions(self):
        '''
        Returns a list of positions that have not been hit.
        '''
        return [x for x in self.positions if not self.positions[x]]
    
    def getValAtPos(self,pos):
        return self.positions.get(pos)

    def getName():
        raise NotImplementedError('Please implement this.')
