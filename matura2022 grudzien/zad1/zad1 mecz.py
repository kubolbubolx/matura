def zad1(file):
    for line in file:
        list = []
        line = line.strip()
        for i in line:
            list.append(i)
    counter = 0
    for i in range(len(list) - 1):
        if list[i] != list[i + 1]:
            counter += 1
    return counter


def zad2(file):
    for line in file:
        line = line.strip()
        a_counter = 0
        b_counter = 0
        last_win = ''
        for i in line:
            if a_counter >= 1000 and abs(a_counter - b_counter) >= 3 \
                    or b_counter >= 1000 and abs(a_counter - b_counter) >= 3:
                return last_win, a_counter, b_counter
            else:
                if i == 'A':
                    a_counter += 1
                    last_win = 'A'
                if i == 'B':
                    b_counter += 1
                    last_win = 'B'


def zad3(file):
    for line in file:
        line = line.strip()
        counter = 1
        passa_a = 0
        passa_b = 0
        longest = 0
        longest_for = ''
        last = 'A'
        for i in line:
            if i == last:
                counter += 1
            else:
                if counter > longest:
                    longest = counter
                    longest_for = last
                if counter >= 10:
                    if last == 'A':
                        passa_a += 1
                    else:
                        passa_b += 1
                last = i
                counter = 1

    return passa_a + passa_b, longest, longest_for







file = open('mecz.txt', 'r')
file2 = open('mecz_przyklad.txt', 'r')
filew = open(' wyniki', 'w')

print(zad3(file))

file.close()
file2.close()
filew.close()
