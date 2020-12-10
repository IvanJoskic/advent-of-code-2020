import re

inputRules = open('input7.txt')
inputRules2 = open('input7.txt')
f = open('log.txt', 'w')


def getnumofinnerbags(bagname, bagrules, i):
    pattern = bagname + r' contain .*\.'
    rule = re.findall(pattern, bagrules)[0].replace('.', '')
    # print(rule)
    rez = 0
    for bag in rule.split(' contain ')[1].split(', '):
        print('-' * i, bag[0], bag[2:])
        rez += (int(bag[0]) + int(bag[0]) * getnumofinnerbags(bag[2:], bagrules, i + 1)) if bag[0] != 'n' else 0
    print(rez)
    return rez


try:
    bagRules = inputRules.readlines()

    outerBag = []
    innerBags = []
    printText = "{:<20} - {:<50}"
    for rule in bagRules:
        splitRule = rule.split('contain')
        outerBag.append(splitRule[0].split()[0] + ' ' + splitRule[0].split()[1])
        # print(outerBag[len(outerBag) - 1])

        f.write(printText.format(splitRule[0], splitRule[1].strip()))
        f.write('\n')
        innerBags.append(splitRule[1].strip())
    stack = ['shiny gold']
    alreadyCountedTheseBags = []
    shinyBagCounter = 0
    while len(stack) > 0:
        bagToCount = stack.pop()
        f.write('Counting bag: ' + bagToCount + ' - ' + str(alreadyCountedTheseBags.count(bagToCount)))
        f.write('\n')
        for bagList in innerBags:
            if bagList.count(bagToCount) == 1 and alreadyCountedTheseBags.count(outerBag[innerBags.index(bagList)]) == 0:
                stack.append(outerBag[innerBags.index(bagList)])
                shinyBagCounter += 1
                f.write(outerBag[innerBags.index(bagList)])
                f.write('\n')
        alreadyCountedTheseBags.append(bagToCount)
        f.write('Already counted: ')
        for x in alreadyCountedTheseBags:
            f.write(x)
        f.write('\n')
    print('Shiny gold bag count: ' + str(shinyBagCounter))

    bagRules = inputRules2.read()
    bagRules = bagRules.replace(' bags', '').replace(' bag', '')

    stack = ['shiny gold']
    while len(stack) > 0:
        bagName = stack.pop()
        pattern = bagName + r' contain .*\.'
        rule = re.findall(pattern, bagRules)
        print(rule)
    print('The number of bags inside of gold bags is: ', getnumofinnerbags('shiny gold', bagRules, 0))

finally:
    inputRules.close()
    f.close()

