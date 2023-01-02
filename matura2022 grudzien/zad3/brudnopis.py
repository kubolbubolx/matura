# file = open('liczby.txt', 'r')
# list = []
#
# for i in file:
#     list.append(i)
#
# print(max(list))
#
# def isprime(n):
#     if n == 2:
#         return True
#     if n % 2 == 0 or n <= 1:
#         return False
#     prime = int(n ** 0.5) + 1
#     for dzielniki in range(3, prime, 2):
#         if n % dzielniki == 0:
#             return False
#     return True
#
# z = int(max(list)) / 2
#
#
# list1 = []
#
# for i in range(int(z)):
#     if isprime(i):
#         list1.append(i)
#
# print(list1)







file2 = open('liczby_przyklad.txt', 'r')

dict = {}



for i in range(10):
    dict[i] = 0

print(dict)

for line in file2:
    line = line.strip()
    for i in line:
        dict[i] += 1
print(dict)












