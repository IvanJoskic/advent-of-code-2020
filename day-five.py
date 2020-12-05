from math import floor
from math import ceil

input = open('input5.txt')

i = j = rez = l = m = 0  # start and end indexes

try:
    lines = input.readlines()
    highestID = 0
    listIDs = ['o'] * (127 * 8 + 7)
    for line in lines:
        line = line.strip()
        i = 0
        j = 127
        row = 0
        col = 0
        l = 0
        m = 7
        for k in range(len(line)):
            print(str(k) + ' - ' + str(line[k]))
            if line[k] == 'F':
                j = floor((i + j) / 2)
                row = j
            elif line[k] == 'B':
                i = ceil((i + j) / 2)
                row = i
            elif line[k] == 'L':
                m = floor((l + m) / 2)
                col = m
            elif line[k] == 'R':
                l = ceil((l + m) / 2)
                col = l
            if k == 6:
                print('row: ' + str(row))
            elif k == 9:
                print('col: ' + str(col))
        rez = row * 8 + col
        listIDs[rez] = 'x'
        print('SeatID: ' + str(rez))
        highestID = highestID if rez <= highestID else rez
    print('HighestID: ' + str(highestID))
    listIDsString = ''

    for el in listIDs:
        listIDsString += el
    print('My seat: ' + str(listIDsString.find('xox') + 1))


finally:
    input.close()