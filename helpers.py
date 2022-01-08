def printMap(map):
    print('\n'.join('  '.join(str(x) for x in row) for row in map))

def shipSizes():
    return {
        'A' : 5,
        'B' : 4,
        'C' : 3,
        'D' : 2,
        'S' : 3
    }