def isprime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    prime = int(n ** 0.5) + 1
    for dzielniki in range(3, prime, 2):
        if n % dzielniki == 0:
            return False
    return True


def zad1(file):
    counter = 0
    for line in file:
        line = line.strip()
        sum = 0
        for i in line:
            sum += ord(i)
        if isprime(sum) == True:
            counter += 1
    return counter


def zad2(file):
    wynik = []
    for line in file:
        line = line.strip()
        list = []
        counter = 0
        for i in line:
            list.append(ord(i))
        for i in range(len(list) - 1):
            if list[i] < list[i+1]:
                counter += 1
        if len(list) - 1 == counter:
            wynik.append(line)
    for i in wynik:
        print(i)
    return wynik


def zad3(file):
    dict = {}
    list = []
    for line in file:
        line = line.strip()
        list.append(line)
    for line in list:
        dict[line] = 0
    for line in list:
        dict[line] += 1
    for i in dict:
        if dict[i] == 2:
            print(i)


file = open('NAPIS.TXT', 'r')

print(zad3(file))

file.close()