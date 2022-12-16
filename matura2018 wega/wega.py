def zad1(file):
    counter = 0
    wynik = ''
    for line in file:
        line = line.strip()
        counter += 1
        if counter % 40 == 0:
            wynik += line[9]
    filew.write(wynik)
    return wynik


def zad2(file):
    max = 0
    word = ''
    for line in file:
        line = line.strip()
        dict = {}
        for i in line:
            dict[i] = 0
        if len(dict) > max:
            max = len(dict)
            word = line
    filew.write(word + ' ' + str(max))


def zad3(file):
    for line in file:
        line = line.strip()
        list = []
        counter = 0
        dict = {}
        for i in line:
            list.append(ord(i))
        for i in list:
            dict[i] = 0
        for i in range(len(list) - 1):
            if list[i] < list[i + 1]:
                if list[i + 1] - list[i] >= 10:
                    pass
                else:
                    counter += 1
            if list[i] > list[i+1]:
                if list[i] - list[i + 1] >= 10:
                    pass
                else:
                    counter += 1
        if len(dict) - 1 == counter:
            filew.write(line + '\n')


file = open('sygnaly.txt', 'r')
file2 = open('przyklad.txt', 'r')
filew = open('wyniki', 'w')

print(zad3(file))

file.close()
file2.close()
filew.close()
def zad1(file):
    counter = 0
    wynik = ''
    for line in file:
        line = line.strip()
        counter += 1
        if counter % 40 == 0:
            wynik += line[9]
    filew.write(wynik)
    return wynik


def zad2(file):
    max = 0
    word = ''
    for line in file:
        line = line.strip()
        dict = {}
        for i in line:
            dict[i] = 0
        if len(dict) > max:
            max = len(dict)
            word = line
    filew.write(word + ' ' + str(max))


def pary(slowo):
    if len(slowo) == 2:
        if abs(ord(slowo[0]) - ord(slowo[1])) > 10:
            return False
        return True
    for i in range(len(slowo) - 1):
        for j in range(i + 1, len(slowo) - 1):
            if abs(ord(slowo[i]) - ord(slowo[j])) > 10:
                return False
    return True


def zad3(file):
    for line in file:
        line = line.strip()
        if pary(line):
            filew.write(line + '\n')









file = open('sygnaly.txt', 'r')
file2 = open('przyklad.txt', 'r')
filew = open('wyniki', 'w')

print(zad3(file))

file.close()
file2.close()
filew.close()
