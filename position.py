class Position:
    def __init__(self,row,col):
        self.row = row
        self.col = col

    def toDict(self):
        return {'row': self.row, 'col': self.col}

    def getX(self):
        return self.row
    
    def getY(self):
        return self.col
    
    def __eq__(self, other):
        if not isinstance(other, Position):
            return NotImplemented
        return self.row == other.row and self.col == other.col
    
    def __hash__(self):
        return hash((self.row, self.col))
         
    

    
    