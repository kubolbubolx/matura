# def zad4_3(file):
#     lista_par = []
#     for line in file:
#         line = line.split()
#         if int(line[0]) == len(line[1]):
#             lista_par.append(line)
#     najmniejsza = ['99', 'aaaaaaaaaaaaaa']
#     for i in lista_par:
#         print(i)
#
# file = open('pary.txt', 'r')
# file2 = open('przyklad.txt', 'r')
#
# print(zad4_3(file))
#
# file.close()
# file2.close()

word = 'abc'
word2 = 'def'
suma = 0
suma2 = 0
for i in word:
    suma = suma + ord(i)
for i in word2:
    suma2 = suma2 + ord(i)

print(suma, suma2)

