def drukowanie(znak, ilosc):
    zmienna = ''
    for i in range(ilosc):
        zmienna = znak * ilosc
    return zmienna

def zad4_2(file):
    for line in file:
            line = line.split()
            # print(line[1])
            last = ''
            counter = 1
            list = []
            list_l = []
            for char in line[1]:
                if last == char:
                    last = char
                    counter += 1
                    list.append(counter)
                    list_l.append(char)
                else:
                    last = char
                    counter = 1
                    list_l.append(char)
            try:
                list = max(list)
                print(list_l[list] * list, list)
            except ValueError:
                print(list_l[0], 1)




file = open('pary.txt', 'r')
file2 = open('przyklad.txt', 'r')

print(zad4_2(file))

file.close()
file2.close()