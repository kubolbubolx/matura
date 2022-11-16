def silnia(liczba):
    wynik = 1
    for i in range(int(liczba)):
        i += 1
        wynik = wynik * i
    return wynik

def zad4_2(file):
    wyniki = []
    for line in file:
        line = line.strip()
        suma = 0
        for i in line:
            suma = suma + silnia(int(i))
        if int(line) == suma:
            wyniki.append(line)
    return wyniki

file = open('liczby.txt', 'r')
file2 = open('przyklad.txt', 'r')

print(zad4_2(file))

file.close()
file2.close()