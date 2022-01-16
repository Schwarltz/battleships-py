from legend import Legend
from shipFactory import createShip
from helpers import printMap
from position import Position
import random
import re

class Sea:
    def __init__(self, height, width):
        self.ships = []
        self.misses = []
        self.height = height
        self.width = width
    
    def setShips(self, ships):
        self.print()
        while len(ships) > 0:
            print(f"Ships remaining: {ships}")
            print("Enter ship positions: <shipname> <row> <col> <H,V>")

            cmd = input()
            validCmd =  re.match(r'^[ABCDS] [0-9]+ [0-9]+ [VH]$', cmd)
            if not validCmd:
                print("Invalid command format. Please try again")
                continue

            type, row, col, direction = cmd.split()
            ship = createShip(type, row, col, direction)
            
            if self.__trySetShip(ship):
                print("Ship set.")
                self.print()
                ships.remove(type)
            else:
                print("Invalid coordinates. Please try again.")
      
    def __trySetShip(self, ship):
        # in bounds
        if not ship.inMap(self):
            return False
        
        # not colliding with other ships
        for other in self.ships:
            if ship.isColliding(other):
                return False
        
        self.ships.append(ship)
        return True

    def autoSetShips(self, ships):
        col, direction = 0, 'H'
        for row in range(len(ships)):
            ship = createShip(ships[row], row, col, direction)
            self.__trySetShip(ship)
        print("Automap layout:")
        self.print()

    def autoSetShips2(self,ships):
        while len(ships) > 0:
            shipType = random.choice(ships)
            pos = self.getRandomPos()
            direction = random.choice(['H', 'V'])
            ship = createShip(shipType, pos.getX(), pos.getY(), direction)
            
            if self.__trySetShip(ship):
                ships.remove(shipType)

    def allSunk(self):
        for ship in self.ships:
            if not ship.isSunk():
                return False
        return True
    
    def hit(self,row,col):
        pos = Position(row,col)
        for s in self.ships:
            if s.getHit(pos):
                if s.isSunk():
                    print(f"{s.getName()} sunk!")
                return True
        self.misses.append(pos)
        return False
        
    def getRandomPos(self):
        x = random.randint(0, self.width)
        y = random.randint(0, self.height)
        return Position(x, y)

    def inSea(self, pos):
        return 0 <= pos.getY() < self.height and 0 <= pos.getX() < self.width

    def getShips(self):
        return self.ships
    
    def getHeight(self):
        return self.height
    
    def getWidth(self):
        return self.width

    def toMap(self):
        sea = [[Legend.WATER.value for i in range(self.width)] for j in range(self.height)]
        sea = self.showShots(self.showShips(sea))

        return sea

    def showShips(self, sea):
        for ship in self.ships:
            for pos in ship.getPos():
                sea[pos.getX()][pos.getY()] = ship.getType().value
        
        return sea
    
    def showShots(self, sea):
        for ship in self.ships:
            for pos in ship.getPos():
                if ship.getValAtPos(pos):
                    sea[pos.getX()][pos.getY()] = Legend.HIT.value
        
        for miss in self.misses:
            sea[miss.getX()][miss.getY()] = Legend.MISS.value
        
        return sea
        
    def toHiddenMap(self):
        sea = [[Legend.WATER.value for i in range(self.width)] for j in range(self.height)]
        return self.showShots(sea)

    def print(self):
        sea = self.toMap()
        printMap(sea)