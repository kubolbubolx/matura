import string

def zad6_3(file):
    for line in file:
        line = line.split()
        list = []
        for letter in range(len(line[0])):
            a = alfabet.index(line[0][letter])
            b = alfabet.index(line[1][letter])
            przesun = (b - a) % len(alfabet)
            list.append(przesun)
        sett = set(list)
        if len(sett) > 1:
            filew.write(line[0] + '\n')

file = open('dane_6_3.txt', 'r')
filew = open('wyniki_6_1.txt', 'w')

alfabet = string.ascii_uppercase
zad6_3(file)

file.close()
filew.close()