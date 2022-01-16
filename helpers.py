from position import Position

def printMap(map):
    print('\n'.join('  '.join(str(x) for x in row) for row in map))

def print2Maps(map1, map2):
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
    return {
        'A' : 5,
        'B' : 4,
        'C' : 3,
        'D' : 2,
        'S' : 3
    }