input = open('input3.txt')

try:
    list = input.readlines()
    maxCol = len(list[0]) - 2
    row = 0
    col = 0
    lastRow = len(list) - 1
    finalTreeCount = 1
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    for move in slopes:
        treeCounter = row = col = 0
        while row <= lastRow:
            if list[row][col] == '#':
                treeCounter += 1
            row += move[1]
            col = (col + move[0]) % (maxCol + 1)
        print('Number of trees hit: ' + str(treeCounter))
        finalTreeCount *= treeCounter
    print('Final tree hit count: ' + str(finalTreeCount))


finally:
    input.close()
