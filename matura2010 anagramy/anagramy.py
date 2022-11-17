def zada(file):
    for line in file:
        list = []
        line = line.strip()
        line2 = line
        line = line.split()
        for i in line:
            list.append(len(i))
        if list[0] == list[1] == list[2] == list[3] == list[4]:
            filew.write(line2 + '\n')

def zadb(file):
    for line in file:
        list = []
        line = line.strip()
        line2 = line
        line = line.split()
        for i in line:
            a = ''.join(sorted(i))
            list.append(a)
        if list[0] == list[1] == list[2] == list[3] == list[4]:
            filew.write(line2 + '\n')



file = open('anagram.txt', 'r')
filew = open('odp_4b.txt', 'w')

print(zadb(file))

file.close()
filew.close()