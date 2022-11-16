def zad4_1(file):
    list = []
    counter = 0
    for line in file:
        line = line.strip()
        # print(line)
        # print(line[0], line[-1])
        if line[0] == line[-1]:
            list.append(line)
            counter += 1
    return counter, list

file = open('liczby.txt', 'r')
file2 = open('przyklad.txt', 'r')

print(zad4_1(file))

file.close()
file2.close()