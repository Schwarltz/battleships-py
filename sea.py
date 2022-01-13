from legend import Legend
from shipFactory import createShip
from helpers import printMap
class Sea:
    def __init__(self, height, width):
        self.ships = []
        self.shots = []
        self.height = height
        self.width = width
    
    def setShips(self, ships):
        self.print()
        while len(ships) > 0:
            print(f"Ships remaining: {ships}")
            print("Enter ship positions:")

            cmd = input()
            type, x, y, direction = cmd.split()
            ship = createShip(type, x, y, direction)
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
        y, direction = 0, 'V'
        for x in range(len(ships)):
            ship = createShip(ships[x], x, y, direction)
            self.__trySetShip(ship)
        print("Automap layout:")
        self.print()

    def allSunk(self):
        for ship in self.ships:
            if not ship.isSunk():
                return False
        

        return True

    def getShips(self):
        return self.ships
    
    def getHeight(self):
        return self.height
    
    def getWidth(self):
        return self.width

    def print(self):
        sea = [['.' for i in range(self.width)] for j in range(self.height)]
        for ship in self.ships:
            for pos in ship.getPos():
                sea[pos.getY()][pos.getX()] = ship.getType().value
        printMap(sea)