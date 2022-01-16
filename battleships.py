from pprint import pprint
from helpers import printMap, shipSizes, print2Maps
from legend import Legend
from sea import Sea
import re

HEIGHT = 10
WIDTH = 10

def main():
    player = Sea(HEIGHT, WIDTH)
    player.autoSetShips2(['A','B','C','D','S'])
    ai = Sea(HEIGHT, WIDTH)
    ai.autoSetShips2(['A','B','C','D','S'])
    while not (player.allSunk() or ai.allSunk()):
        playGame(player, ai)
    
    if player.allSunk():
        print('Game Over!')
    else:
        print('You won!')

def playGame(player, ai):
    print2Maps(player.toMap(), ai.toMap())
    # prompt the player to select a coordinate
    print("Select a coordinate to hit:")
    cmd = input()
    validCmd = re.match(r'[0-9]+ [0-9]+', cmd)
    if not validCmd:
        print('Invalid Command.')
        return

    row, col = cmd.split()
    row, col = int(row), int(col)
    PSuccess = ai.hit(row,col)
    if PSuccess:
        print('Hit confirmed!')
    else:
        print('That one missed...')


if __name__ == "__main__":
    main()