def zad1(file):
    max = 0
    min = 999
    for line in file:
        line = line.strip()
        line = line.split()
        for i in line:
            i = int(i)
            if i > max:
                max = i
            if i < min:
                min = i
    return max, min


def zad2(file):
    counter = 0
    for line in file:
        line = line.strip()
        line = line.split()
        for i in range(160):
            if line[i] == line[319 - i]:
                pass
            else:
                counter += 1
                break
    return counter


def zad3(file):
    main_list = []
    counter = 0
    for line in file:
        line = line.strip()
        line = line.split()
        main_list.append(line)
    for list in range(1, len(main_list) - 1):
        for pix in range(1, len(main_list[list]) - 1):
            if abs(int(main_list[list][pix]) - int(main_list[list][pix + 1])) > 128 or\
                    abs(int(main_list[list][pix]) - int(main_list[list][pix - 1])) > 128 or\
                    abs(int(main_list[list][pix]) - int(main_list[list + 1][pix])) > 128 or\
                    abs(int(main_list[list][pix]) - int(main_list[list - 1][pix])) > 128:
                counter += 1

    # pierwsza poziom
    for pix in range(len(main_list[0])):
        try:
            if abs(int(main_list[0][pix]) - int(main_list[0][pix + 1])) > 128 or\
                    abs(int(main_list[0][pix]) - int(main_list[0][pix - 1])) > 128:
                counter += 1
        except IndexError:
            if abs(int(main_list[0][pix]) - int(main_list[0][pix - 1])) > 128:
                counter += 1

    # ostatnia poziom
    for pix in range(len(main_list[199])):
        try:
            if abs(int(main_list[199][pix]) - int(main_list[199][pix + 1])) > 128 or\
                    abs(int(main_list[199][pix]) - int(main_list[199][pix - 1])) > 128:
                counter += 1
        except IndexError:
            if abs(int(main_list[199][pix]) - int(main_list[199][pix - 1])) > 128:
                counter += 1

    # pierwsza pion
    for list in range(len(main_list)):
        try:
            if abs(int(main_list[list][0]) - int(main_list[list + 1][0])) > 128 or\
                    abs(int(main_list[list][0]) - int(main_list[list - 1][0])) > 128:
                counter += 1
        except IndexError:
            if abs(int(main_list[list][0]) - int(main_list[list - 1][0])) > 128:
                counter += 1

    # ostatnia pion
    for list in range(len(main_list)):
        try:
            if abs(int(main_list[list][319]) - int(main_list[list + 1][319])) > 128 or\
                    abs(int(main_list[list][319]) - int(main_list[list - 1][319])) > 128:
                counter += 1
        except IndexError:
            if abs(int(main_list[list][319]) - int(main_list[list - 1][319])) > 128:
                counter += 1

    return counter


def zad4(file):
    main_list = []
    for line in file:
        line = line.strip()
        line = line.split()
        main_list.append(line)

    last = int(main_list[0][0])
    counter = 1
    max_counter = 1
    for i in range(320):
        for list in range(200):
            if int(main_list[list][i]) == last:
                counter += 1
            else:
                if counter > max_counter:
                    max_counter = counter
                counter = 1
                last = int(main_list[list][i])

    return max_counter


file = open('dane.txt', 'r')
file2 = open('przyklad.txt', 'r')
filew = open('wyniki', 'w')

print(zad4(file))

file.close()
file2.close()
filew.close()