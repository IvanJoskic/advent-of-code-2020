inputFile = open('input9.txt')

try:
    numbers = inputFile.readlines()
    numToCheck = 0
    for i in range(25, len(numbers)):
        numToCheck = int(numbers[i])

        checkPassed = False
        for j in range(i - 25, i):
            for k in range(j + 1, i):
                num1 = int(numbers[j])
                num2 = int(numbers[k])
                if num1 + num2 == numToCheck:
                    checkPassed = True
        if not checkPassed:
            print("This number didn't pass the check: " + str(numToCheck))
            break
    end = False
    for i in range(len(numbers)):
        sum = 0
        j = i
        smallest = largest = int(numbers[i])
        while sum < numToCheck:
            tmpNum = int(numbers[j])
            sum += tmpNum
            smallest = tmpNum if tmpNum < smallest else smallest
            largest = tmpNum if tmpNum > largest else largest

            if sum == numToCheck:
                print('The encryption weakness is:', smallest + largest)
                end = True
            else:
                j += 1
        if end:
            break
finally:
    inputFile.close()
