from position import Position


def printMap(map):
    '''
    Prints the map into stdout.

        Parameters:
            map (2D list of char): the map to be printed.
    '''
    print('\n'.join('  '.join(str(x) for x in row) for row in map))

def print2Maps(map1, map2):
    '''
    Prints both maps side by side into stdout.

        Parameters:
            map1 (2D list of char): the map to be printed on the left.
            map2 (2D list of char): the map to be printed on the right.
    '''
    if len(map1) != len(map2):
        print("map1 did not match length of map2")
        print("Map 1")
        printMap(map1)
        print("Map 2")
        printMap(map2)
        exit(1)
        
    for i in range(len(map1)):
        print('  '.join(str(x) for x in map1[i]) + '    ' + '  '.join(str(x) for x in map2[i]))

def inputToPos(row, col, length, direction):
    '''
    Converts a coordinate with a length and direction into the corresponding list of positions.

        Parameters:
            row (int): the row of the starting coordinate.
            col (int): the column of the starting coordinate.
            length (int): how far the list should extend.
            direction (str) : the direction the list should move.
        
        Returns:
            l (list of Position): Positions that start from the given coordinate and is 'length' long.
    '''
    row, col = int(row), int(col)
    l = []
    if direction == 'H':
        for i in range(length):
            l.append(Position(row, col+i))
    elif direction == 'V':
        for i in range(length):
            l.append(Position(row+i, col))
    return l    

def shipSizes():
    '''
    The length of all playable ships.
    '''
    return {
        'A' : 5,
        'B' : 4,
        'C' : 3,
        'D' : 2,
        'S' : 3
    }