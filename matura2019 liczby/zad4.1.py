def zad4_1(file):
    potegi_3 = []
    wynik = []
    counter = 0
    for i in range(20):
        potegi_3.append(3 ** i)
    for line in file:
        line = line.strip()
        if int(line) in potegi_3:
            wynik.append(line)
            counter += 1
    return counter, wynik

file = open('liczby.txt', 'r')
file2 = open('przyklad.txt', 'r')

print(zad4_1(file))

file.close()
file2.close()