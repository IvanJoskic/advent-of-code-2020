input = open('input1.txt')
try:
    list = input.readlines()
    for i in range(len(list)):
        for j in range(i, len(list)):
            if int(list[i]) + int(list[j]) == 2020:
                print("Two sum: ", int(list[i]) * int(list[j]))
            for k in range(j, len(list)):
                if int(list[i]) + int(list[j]) + int(list[k]) == 2020:
                    print("Three sum: ", int(list[i]) * int(list[j]) * int(list[k]))
finally:
    input.close()
