input = open('input2.txt')
try:
    list = input.readlines()
    validLines = 0
    for line in list:
        splitted = line.split()
        letter = splitted[1][0]
        bounds = splitted[0].split('-')
        i = int(bounds[0])
        j = int(bounds[1])
        counter = 0
        for x in splitted[2]:
            if x == letter:
                counter += 1
        if counter >= i and counter <= j:
            validLines += 1
    print('1. Valid lines: ' + str(validLines))

    validLines = 0
    for line in list:
        splitted = line.split()
        passwd = splitted[2]
        letter = splitted[1][0]
        bounds = splitted[0].split('-')
        i = int(bounds[0]) - 1
        j = int(bounds[1]) - 1
        try:
            if (passwd[i] == letter and passwd[j] != letter) or (passwd[i] != letter and passwd[j] == letter):
                validLines += 1
        except:
            pass
            # ignore

    print('2. Valid lines: ' + str(validLines))
finally:
    input.close()
