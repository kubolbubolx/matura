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
        if isprime(int(line) - 1):
            counter += 1
    return counter


def zad2(file):
    list1 = []
    list2 = []
    for i in range(1000):
        if isprime(i):
            list1.append(i)
    list2 = list1
    max_counter = 0
    max_counter_line = ''
    min_counter = 99999999999
    min_counter_line = ''
    for line in file:
        list = []
        counter = 0
        line = line.strip()
        for i in list1:
            for j in list2:
                if (i + j) == int(line):
                    if (i, j) not in list:
                        if (j, i) not in list:
                            list.append((i, j))
                            counter += 1
        if counter > max_counter:
            max_counter = counter
            max_counter_line = line
        if counter < min_counter:
            min_counter = counter
            min_counter_line = line
    return max_counter_line, max_counter, min_counter_line, min_counter


def zad3(file):
    dict = {'0':0,
            '1':0,
            '2':0,
            '3':0,
            '4':0,
            '5':0,
            '6':0,
            '7':0,
            '8':0,
            '9':0,
            'A':0,
            'B':0,
            'C':0,
            'D':0,
            'E':0,
            'F':0}

    for line in file:
        line = line.strip()
        line = format(int(line), 'X')
        for i in line:
            dict[i] += 1

    for i in dict:
        print(i+':', dict[i])

    return dict




file = open('liczby.txt', 'r')
file2 = open('liczby_przyklad.txt', 'r')
filew = open('wyniki', 'w')

print(zad2(file2))

file.close()
file2.close()
filew.close()