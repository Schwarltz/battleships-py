def printMap(map):
    print('\n'.join('  '.join(str(x) for x in row) for row in map))