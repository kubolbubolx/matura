def znajdz_spojny_fragment(file):
    for line in file:
        line = line.split()
        napis = line[1]
        dlugosc=1
        max=1
        litera=napis[0]
        for i in range(len(napis)-1):
            if napis[i]==napis[i+1]:
                dlugosc=dlugosc+1
                if dlugosc>max:
                    max=dlugosc
                    litera=napis[i]
            else:
                dlugosc=1
        print(litera * max, max)


file = open("pary.txt", 'r')

znajdz_spojny_fragment(file)

file.close()