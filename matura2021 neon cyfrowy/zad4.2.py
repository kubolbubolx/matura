def zad4_2(file):
    list = []
    counter = 1
    last = ''
    for line in file:
        line = line.split()
        if last == line[0]:
            last = line[0]
            counter += 1
            list.append(counter)
            instrukcja = line[0]
        else:
            last = line[0]
            counter = 1
    list = max(list)
    return list, instrukcja

file = open('instrukcje.txt', 'r')
file2 = open('przyklad.txt', 'r')

print(zad4_2(file))

file.close()
file2.close()