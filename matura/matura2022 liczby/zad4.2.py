def rozkład(liczba):
    czynniki = []
    dzielnik = 2
    while liczba != 1:
        while liczba % dzielnik == 0:
            liczba = liczba // dzielnik
            czynniki.append(dzielnik)
        dzielnik += 1
    return czynniki

def zad4_2a(file):
    najwięcej = 0
    liczba = []
    for line in file:
        line = line.strip()
        a = rozkład(int(line))
        if len(a) > najwięcej:
            liczba = []
            najwięcej = len(a)
            liczba.append(line)
        elif len(a) == najwięcej:
            liczba.append(line)
    return najwięcej, liczba

def zad4_2b(file):
    najwięcej = 0
    liczba = []
    for line in file:
        line = line.strip()
        a = set(rozkład(int(line)))
        if len(a) > najwięcej:
            liczba = []
            najwięcej = len(a)
            liczba.append(line)
        elif len(a) == najwięcej:
            liczba.append(line)
    return najwięcej, liczba


file = open('liczby.txt', 'r')
file2 = open('przyklad.txt', 'r')

# print(zad4_2a(file))
print(zad4_2b(file))

file.close()
file2.close()