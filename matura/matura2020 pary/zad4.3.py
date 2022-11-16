def zad4_3(file):
    lista_par = []
    for line in file:
        line = line.split()
        if int(line[0]) == len(line[1]):
            lista_par.append(line)
    najmniejsza = ['99', 'aaaaaaaaaaaaaa']
    for j in range(len(lista_par)):
        for i in lista_par:
            if int(i[0]) < int(najmniejsza[0]):
                najmniejsza = i
            elif int(i[0]) == int(najmniejsza[0]):
                word = str(i[1])
                word2 = str(najmniejsza[1])
                suma = 0
                suma2 = 0
                for t in word:
                    suma = suma + ord(t)
                for y in word2:
                    suma2 = suma2 + ord(y)
                if word < word2:
                    najmniejsza = i
    return najmniejsza



file = open('pary.txt', 'r')
file2 = open('przyklad.txt', 'r')

print(zad4_3(file))

file.close()
file2.close()