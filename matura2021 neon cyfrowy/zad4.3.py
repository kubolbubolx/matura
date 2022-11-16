def zad4_3(file):
    list = []
    list2 = []
    for line in file:
        line = line.split()
        if line[0] == 'DOPISZ':
            list.append(line[1])
    for i in list:
        list2.append(list.count(i))
    index = list2.index(max(list2))
    wynik = list[index]
    return wynik, max(list2)

file = open('instrukcje.txt', 'r')
file2 = open('przyklad.txt', 'r')

print(zad4_3(file))

file.close()
file2.close()