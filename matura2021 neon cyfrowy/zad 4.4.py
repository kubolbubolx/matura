def zad4_4(file):
    napis = []
    wynik = ''
    for line in file:
        line = line.split()
        if line[0] == 'DOPISZ':
            napis.append(line[1])
        elif line[0] == 'ZMIEN':
            napis.pop(-1)
            napis.append(line[1])
        elif line[0] == 'USUN':
            napis.pop(-1)
        elif line[0] == 'PRZESUN':
            ascii = ord(line[1])
            if ascii == 90:
                ascii = 65
            else:
                ascii += 1
            index = int(napis.index(line[1]))
            napis.pop(index)
            napis.insert(index, chr(ascii))
    for i in napis:
        wynik += i
    return wynik



file = open('instrukcje.txt', 'r')
file2 = open('przyklad.txt', 'r')

print(zad4_4(file))

file.close()
file2.close()
