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
        '''
        Manually designate locations for given 'ships'through the command line.

            Parameters:
                ships (list of str) : A list of symbols representing their ships.
        '''

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
        '''
        Tries to place a ship in the sea. 

            Parameters:
                ship (Ship): The ship being placed.
            
            Returns:
                True if the ship was placed successfully.
                False otherwise.
        '''  

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
        '''
        Places ships in a row by row manner in order of ship appearance in the list.
        
            Parameters:
                ships (list of str) : A list of symbols representing their ships.
        '''

        col, direction = 0, 'H'
        for row in range(len(ships)):
            ship = createShip(ships[row], row, col, direction)
            self.__trySetShip(ship)
        print("Automap layout:")
        self.print()

    def randomSetShips(self,ships):
        '''
        Places ships in a random manner on the board.
        
            Parameters:
                ships (list of str) : A list of symbols representing their ships.
        '''

        while len(ships) > 0:
            shipType = random.choice(ships)
            pos = self.getRandomPos()
            direction = random.choice(['H', 'V'])
            ship = createShip(shipType, pos.getX(), pos.getY(), direction)
            
            if self.__trySetShip(ship):
                ships.remove(shipType)

    def allSunk(self):
        '''Checks if all ships on the board have been sunk.'''
        for ship in self.ships:
            if not ship.isSunk():
                return False
        return True
    
    def hit(self,row,col):
        '''
        Logs the shot into the map.

            Parameters:
                row (int): the row of the shot being fired.
                col (int): the column of the shot being fired.

            Returns:
                True if the shot successfully hit a ship,
        '''

        pos = Position(row,col)
        for s in self.ships:
            if s.getHit(pos):
                if s.isSunk():
                    print(f"{s.getName()} sunk!")
                return True
        self.misses.append(pos)
        return False
        
    def getRandomPos(self):
        '''
        Creates a random position that is valid for the board.

            Returns:
                A Position that is bounded within the Sea's dimensions
        '''
        x = random.randint(0, self.width)
        y = random.randint(0, self.height)
        return Position(x, y)
    
    def getRandomShipPos(self):
        '''
        Creates a random position that is guaranteed to contains a ship.
        Guaranteed to be a cell that has not been hit.

            Returns:
                A ship position
        '''
        l = []
        for s in self.ships:
            l2 = s.getUnhitPos()
            l.extend(l2)
        
        return random.choice(l)

    def inSea(self, pos):
        '''
        Checks if the given position is within the boundaries.

            Parameters:
                pos (Position): the position being checked

            Returns:
                True if the position is within bounds.
        '''

        return 0 <= pos.getY() < self.height and 0 <= pos.getX() < self.width

    def getShips(self):
        return self.ships
    
    def getHeight(self):
        return self.height
    
    def getWidth(self):
        return self.width

    def toMap(self):
        '''
        Converts the sea into a 2D array that shows all ships' current positions and where shots have landed.

            Returns:
                sea (2D list of str): reveals all ship locations and shots in the sea's current state.
        '''

        sea = [[Legend.WATER.value for i in range(self.width)] for j in range(self.height)]
        sea = self.showShots(self.showShips(sea))

        return sea

    def showShips(self, sea):
        '''
        Shows where all ships are currently located in the sea.

            Parameters:
                sea (2D list of str): the sea where the ship's locations will be stored in.
            
            Returns:
                sea (2D list of str): the sea with all ships' locations.
        '''

        for ship in self.ships:
            for pos in ship.getPos():
                sea[pos.getX()][pos.getY()] = ship.getType().value
        
        return sea
    
    def showShots(self, sea):
        '''
        Shows where all shots are currently located in the sea.

            Parameters:
                sea (2D list of str): the sea where the shots' locations will be stored in.
            
            Returns:
                sea (2D list of str): the sea with all shots' locations.
        '''

        for ship in self.ships:
            for pos in ship.getPos():
                if ship.getValAtPos(pos):
                    sea[pos.getX()][pos.getY()] = Legend.HIT.value
        
        for miss in self.misses:
            sea[miss.getX()][miss.getY()] = Legend.MISS.value
        
        return sea
        
    def toHiddenMap(self):
        '''
        Reveal only where the shots are located.

            Returns:
                A 2D list containing water, misses and hits.
        '''

        sea = [[Legend.WATER.value for i in range(self.width)] for j in range(self.height)]
        return self.showShots(sea)

    def print(self):
        '''Prints the map to stdout.'''
        sea = self.toMap()
        printMap(sea)