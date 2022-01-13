class Position:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def toDict(self):
        return {'x': self.x, 'y': self.y}

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    # def __eq__(self, other):
    #     if isinstance(other, Position):
    #         return self.x == other.x and self.y == other.y
    #     return False
    
    