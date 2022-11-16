def zad4_3(file):
    for line in file:
        line = line.strip()  # line to jest nasze x




file = open('liczby.txt', 'r')
file2 = open('przyklad.txt', 'r')

print(zad4_3(file2))

file.close()
file2.close()