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
        y, direction = 0, 'H'
        for x in range(len(ships)):
            ship = createShip(ships[x], x, y, direction)
            self.__trySetShip(ship)

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
                sea[pos['y']][pos['x']] = ship.getType().value
        printMap(sea)



# def setShips(playerMap):
#     validShips = ['A','B','C','D','S']
#     printMap(playerMap)
#     while len(validShips) > 0:
#         print(f"Ships remaining: {validShips}")
#         print("Enter ship positions:")

#         cmd = input()
#         if validCommand(validShips,cmd, playerMap):
#             playerMap = placeShip(playerMap, cmd)
#             print("Ship set.")
#             printMap(playerMap)
#             validShips.remove(cmd[0])
#         else:
#             print("Invalid command. Try again")

# def validCommand(remainingShips, cmd, playerMap):
#     ORIENTATIONS = ['H', 'V']
#     cmd = cmd.split(' ')
#     # check correct number of input arguments
#     if len(cmd) != 4:
#         return False
    
#     ship, x, y, orient = cmd
#     # type checking
#     if ship not in remainingShips or not (x.isnumeric() and y.isnumeric()) or orient not in ORIENTATIONS:
#         return False

#     x = int(x)
#     y = int(y)

#     # checking bounds for x and y
#     if x not in range(len(playerMap)) or y not in range(len(playerMap)):
#         return False

#     # querying locations on the map to check
#     checks = checkPositions(ship, x, y, orient)

#     # checking that the ship can be placed
#     for pos in checks:
#         if pos['x'] < 0 or len(playerMap) <= pos['x'] or pos['y'] < 0 or len(playerMap) <= pos['y'] or playerMap[pos['x']][pos['y']] != '.':
#             return False
#     return True