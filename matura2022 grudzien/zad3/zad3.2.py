from math import sqrt
import time

t1 = time.time()

def isprime(n):
    if n < 2:
        return False
    range_limit = int(sqrt(n)) + 1
    for dzielniki in range(2, range_limit):
        if n % dzielniki == 0:
            return False
    return True

def goldbach(n):
    wyniki = []
    for i in range(2, n // 2 + 1):
        roznica = n - i
        if isprime(i) and isprime(roznica):
            wyniki.append([i, roznica])
    return wyniki

with open('liczby_przyklad.txt', 'r') as file:
    nums = [int(n) for n in file.readlines()]

unique_nums = set(nums)
even_nums = filter(lambda x: x % 2 == 0, unique_nums)

goldbach_results = map(
    lambda num: {'number': num, 'total_sums': len(goldbach(num))}, even_nums)

sorted_goldbach_results = sorted(
    goldbach_results, key=lambda res: res['total_sums'])

print(f'lower goldbach result: {sorted_goldbach_results[0]}')
print(f'higher goldbach result: {sorted_goldbach_results[-1]}')
print(f'czas działania: {round(time.time() - t1)}')
