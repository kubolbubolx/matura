def zad1(file):
    counter = 0
    for line in file:
        line = line.strip()
        if line[0] == line[-1]:
            counter += 1

    return counter


def zad2(file):
    counter = 0
    for line in file:
        line = line.strip()
        line = str(int(str(line), 8))
        if line[0] == line[-1]:
            counter += 1

    return counter


def zad3(file):
    counter = 0
    list = []
    for line in file:
        line = line.strip()
        for i in range(len(line) - 1):
            print(i)
            if line[i] <= line[i + 1]:
                x = True
            else:
                x = False
                break
        if x == True:
            counter += 1
            list.append(int(line))

    return 'ile', counter, 'min', min(list), 'max', max(list)



file = open('dane.txt', 'r')

print(zad3(file))

file.close()