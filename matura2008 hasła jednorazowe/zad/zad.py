def zad1(file):
    max = 0
    maxslowo = ''
    min = 99999999
    minslowo = ''
    for line in file:
        line = line.strip()
        line = line[::-1]
        filew.write(line + '\n')
        if len(line) > max:
            max = len(line)
            maxslowo = line
        if len(line) < min:
            min = len(line)
            minslowo = line

    return max, maxslowo, min, minslowo


def palindrom(word):
    if word == word[::-1]:
        return True
    return False


def zad2(file):
    suma = 0
    najdluzsze = 0
    najdluzszestr = ''
    najkrotsze = 999999999
    najkrotszestr = ''
    for line in file:
        line = line.strip()
        if palindrom(line):
            filew.write(line + '\n')
            suma += len(line)
            if len(line) > najdluzsze:
                najdluzsze = len(line)
                najdluzszestr = line
            if len(line) < najkrotsze:
                najkrotsze = len(line)
                najkrotszestr = line
            if len(line) == 12:
                print(line)
        else:
            dlugosc = len(line)
            max = ''
            while dlugosc != 0:
                slowo = ''
                for i in range(dlugosc):
                    slowo += line[i]
                dlugosc -= 1
                if palindrom(slowo) and len(slowo) > len(max):
                    max = slowo
            haslo = line[len(max):][::-1] + line
            suma += len(haslo)
            if len(haslo) > najdluzsze:
                najdluzsze = len(haslo)
                najdluzszestr = haslo
            if len(haslo) < najkrotsze:
                najkrotsze = len(haslo)
                najkrotszestr = haslo
            if len(haslo) == 12:
                print(haslo)
            filew.write(haslo + '\n')
    return najdluzsze, najdluzszestr, najkrotsze, najkrotszestr, suma


file = open('slowa.txt', 'r')
filew = open('wyniki', 'w')

print(zad2(file))

file.close()