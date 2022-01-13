from pprint import pprint
from helpers import printMap, shipSizes, print2Maps
from legend import Legend
from sea import Sea

WIDTH = 10

def main():
    player = Sea(WIDTH, WIDTH)
    player.setShips(['A', 'B', 'C', 'D', 'S'])
    ai = Sea(WIDTH, WIDTH)
    ai.autoSetShips(['A', 'B', 'C', 'D', 'S'])
    while not (player.allSunk() or ai.allSunk()):
        playGame(player, ai)
        break

def playGame(player, ai):
    pass


if __name__ == "__main__":
    main()