from pprint import pprint
from helpers import printMap, shipSizes

WIDTH = 10

def main():
    
    playerMap = [['.' for i in range(WIDTH)] for j in range(WIDTH)]
    playerMap = setShips(playerMap)
    AIMap = randomMap()
    printMap(AIMap)

def randomMap():
    randomMap = [['.' for i in range(WIDTH)] for j in range(WIDTH)]
    pos = {
        'x' : 0, 'y' : 0
    }
    for ship in shipSizes().keys():
        cmd = f"{ship} {pos['x']} {pos['y']} H"
        randomMap = placeShip(randomMap, cmd)
        pos['x'] += 1
    
    return randomMap


def setShips(playerMap):
    validShips = ['A','B','C','D','S']
    printMap(playerMap)
    while len(validShips) > 0:
        print(f"Ships remaining: {validShips}")
        print("Enter ship positions:")

        cmd = input()
        if validCommand(validShips,cmd, playerMap):
            playerMap = placeShip(playerMap, cmd)
            print("Ship set.")
            printMap(playerMap)
            validShips.remove(cmd[0])
        else:
            print("Invalid command. Try again")

'''
A valid command consists of 4 arguments
'''
def validCommand(remainingShips, cmd, playerMap):
    ORIENTATIONS = ['H', 'V']
    cmd = cmd.split(' ')
    # check correct number of input arguments
    if len(cmd) != 4:
        return False
    
    ship, x, y, orient = cmd
    # type checking
    if ship not in remainingShips or not (x.isnumeric() and y.isnumeric()) or orient not in ORIENTATIONS:
        return False

    x = int(x)
    y = int(y)

    # checking bounds for x and y
    if x not in range(len(playerMap)) or y not in range(len(playerMap)):
        return False

    # querying locations on the map to check
    checks = checkPositions(ship, x, y, orient)

    # checking that the ship can be placed
    for pos in checks:
        if pos['x'] < 0 or len(playerMap) <= pos['x'] or pos['y'] < 0 or len(playerMap) <= pos['y'] or playerMap[pos['x']][pos['y']] != '.':
            return False
    return True

def checkPositions(ship, x, y, dir):
    validShips = shipSizes()

    if ship not in validShips.keys():
        print(f"Could not find {ship} in validShips.")

    checks = []
    if dir == 'V':
        checks = [{'x' : x + offset, 'y' : y} for offset in [*range(validShips[ship])]]
    elif dir == 'H':
        checks = [{'x' : x, 'y' : y + offset} for offset in [*range(validShips[ship])]]

    return checks

def placeShip(sea, input):
    shipID, x, y, dir = input.split(' ')
    x, y = int(x), int(y)
    positions = checkPositions(shipID, x, y, dir)
    
    for pos in positions:
        sea[pos['x']][pos['y']] = shipID
    
    return sea



if __name__ == "__main__":
    main()