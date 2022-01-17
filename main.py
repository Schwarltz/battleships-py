from pprint import pprint
from helpers import printMap, shipSizes, print2Maps
from legend import Legend
from sea import Sea
import re
import random

HEIGHT = 10
WIDTH = 10

def main():
    player = Sea(HEIGHT, WIDTH)
    player.setShips(['A','B','C','D','S'])
    ai = Sea(HEIGHT, WIDTH)
    ai.randomSetShips(['A','B','C','D','S'])
    while not (player.allSunk() or ai.allSunk()):
        print2Maps(player.toMap(), ai.toMap())
        playerMove(ai)
        aiMove(player)
    
    # player wins if the final turns kill both player and ai's board
    if ai.allSunk():
        print('You won!')
    else:
        print('Game Over!')

'''
Logic for player's actions
'''
def playerMove(ai):
    # prompt the player to select a coordinate to shoot at
    print("Select a coordinate to hit: <row> <col>")
    cmd = input()
    validCmd = re.match(r'[0-9]+ [0-9]+', cmd)
    if not validCmd:
        print('Invalid Command.')
        return

    # determine if the shot was a success
    row, col = cmd.split()
    row, col = int(row), int(col)
    ai.hit(row,col)
'''
Logic for AI's actions
'''
def aiMove(player):
    # determine if  the ai should be able to hit the player's ships
    isSmart= random.random() < 0.3

    if isSmart:
        pos = player.getRandomShipPos()
    else:
        pos = player.getRandomPos()

    player.hit(pos.getX(), pos.getY())    
    


if __name__ == "__main__":
    main()