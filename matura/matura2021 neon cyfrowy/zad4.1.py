def zad4_1(file):
    suma = 0
    ile_odjąć = 0
    for line in file:
        line = line.split()
        if line[0] == 'DOPISZ':
            suma += 1
        elif line[0] == 'USUN':
            ile_odjąć += 1
        else:
            pass
    wynik = suma - ile_odjąć
    return wynik

file = open('instrukcje.txt', 'r')
file2 = open('przyklad.txt', 'r')

print(zad4_1(file))

file.close()
file2.close()
