def czy_pierwsza(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    pierw = int(n**0.5) + 1
    for dzielnik in range(3, pierw, 2):
        if n % dzielnik == 0:
            return False
    return True

def liczby_pierwsze(zakres):
    liczby_pierwsze = []
    for i in range(int(zakres)):
        if czy_pierwsza(i):
            liczby_pierwsze.append(i)
    return liczby_pierwsze

def parzysta_czy_nie(liczba):
    if int(liczba) % 2 == 0:
        return True
    else:
        return False

def zad4_1(file):
    for line in file:
        line = line.split()
        liczby_pierwsze_nieparzyste = []
        if int(line[0]) > 4 and parzysta_czy_nie(line[0]):
            for i in liczby_pierwsze(int(line[0])):
                if parzysta_czy_nie(i) == False:
                    liczby_pierwsze_nieparzyste.append(i)
            list = []
            pierwsza_liczba = []
            druga_liczba = []
            for i in liczby_pierwsze_nieparzyste:
                for j in range(len(liczby_pierwsze_nieparzyste)):
                    wynik = i + liczby_pierwsze_nieparzyste[j]
                    list.append(wynik)
                    pierwsza_liczba.append(i)
                    druga_liczba.append(liczby_pierwsze_nieparzyste[j])
            powtorzenia = []
            for i in list:
                if i == int(line[0]):
                    if i not in powtorzenia:
                        powtorzenia.append(i)
                        j = list.index(i)
                        print('liczba = ', list[j], 'pierwsza = ', pierwsza_liczba[j], 'druga = ', druga_liczba[j])
file = open('pary.txt', 'r')
file2 = open('przyklad.txt', 'r')

print(zad4_1(file))

file.close()
file2.close()