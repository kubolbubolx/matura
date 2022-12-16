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
    words = ''
    for line in file:
        line = line.strip()
        b = True
        for i in line:
            if line == '\n':
                continue
            if b:
                for i2 in line[1:]:
                    if i2 == '\n':
                        continue
                    diff = abs(ord(i) - ord(i2))
                    if diff > 10:
                        b = False
            else:
                break
        if b:
            words = words + line + '\n'
    filew.write(words)


file = open('sygnaly.txt', 'r')
file2 = open('przyklad.txt', 'r')
filew = open('wyniki', 'w')

print(zad3(file))

file.close()
file2.close()
filew.close()
