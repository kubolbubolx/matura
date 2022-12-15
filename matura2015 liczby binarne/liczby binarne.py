def zad1(file):
    counter = 0
    for line in file:
        line = line.strip()
        zero_counter = 0
        one_counter = 0
        for i in line:
            if i == '0':
                zero_counter += 1
            else:
                one_counter += 1
        if zero_counter > one_counter:
            counter += 1
    return counter


def zad2(file):
    can_by_2 = 0
    can_by_8 = 0
    for line in file:
        line = line.strip()
        num = int(line, 2)
        if num % 2 == 0:
            can_by_2 += 1
        if num % 8 == 0:
            can_by_8 += 1
    return can_by_2, can_by_8


def zad3(file):
    min = 999999999999999999999999999999999999999999999999999999999999
    max = 0
    line_counter_for_min = 0
    line_counter_for_max = 0
    counter = 0
    for line in file:
        counter += 1
        line = line.strip()
        num = int(line, 2)
        print(num)
        if num > max:
            max = num
            line_counter_for_max = counter
        if num < min:
            min = num
            line_counter_for_min = counter

    return line_counter_for_min, line_counter_for_max


file = open('liczby.txt', 'r')
filew = open('wyniki', 'w')

print(zad3(file))

file.close()
filew.close()
