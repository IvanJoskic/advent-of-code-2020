inputFile = open('input6.txt')

try:
    lines = inputFile.read()

    totalA = totalB = 0
    groups = lines.split('\n\n')

    for group in groups:
        answers = group.replace('\n', '')
        uniqueAnswers = set(answers)
        totalA += len(uniqueAnswers)
        numOfPeople = len(group.split('\n'))
        # print(answers, len(uniqueAnswers), numOfPeople)

        for letter in uniqueAnswers:
            if answers.count(letter) == numOfPeople:
                totalB += 1
    print("Total number of answers anyone said 'Yes' to: " + str(totalA))
    print("Total number of answers everyone said 'Yes' to: " + str(totalB))
finally:
    inputFile.close()
