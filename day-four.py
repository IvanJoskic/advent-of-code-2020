import re


def checkfield(field, value):
    if field == 'byr':
        return 1920 <= int(value) <= 2002
    elif field == 'iyr':
        return 2010 <= int(value) <= 2020
    elif field == 'eyr':
        return 2020 <= int(value) <= 2030
    elif field == 'hgt':
        if re.search("^[0-9]+cm$", value) is not None:
            number = re.search("^[0-9]+", value).group()
            return 150 <= int(number) <= 193
        elif re.search("^[0-9]+in$", value) is not None:
            number = re.search("^[0-9]+", value).group()
            return 59 <= int(number) <= 76
        else:
            return False
    elif field == 'hcl':
        return re.search("^#([0-9]*[a-f]*){6}", value) is not None
    elif field == 'ecl':
        return ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'].count(value) == 1
    elif field == 'pid':
        return re.search("^[0-9]{9}$", value) is not None
    elif field == 'cid':
        return True
    return False


inputData = open('input4.txt')

try:
    lines = inputData.readlines()
    result = ''
    for line in lines:
        result += line
    final = result.split('\n\n')
    for i in range(len(final)):
        final[i] = final[i].replace("\n", " ")
    counter = 0
    validLines = []
    for line in final:
        lines = line.split()
        hasFields = []
        for line2 in lines:
            fields = line2.split(':')
            hasFields.append(fields[0])
        if len(hasFields) == 8 or len(hasFields) == 7 and hasFields.count('cid') <= 0:
            counter += 1
            validLines.append(line)
    print('Nubmer of valid passports: ' + str(counter))

    for line in validLines:
        fields = line.split()
        fieldValPair = []
        for x in fields:
            fieldValPair = x.split(':')
            if not checkfield(fieldValPair[0], fieldValPair[1]):
                counter -= 1
                # print(fieldValPair)
                break

    print('Number after validation: ' + str(counter))
finally:
    inputData.close()
