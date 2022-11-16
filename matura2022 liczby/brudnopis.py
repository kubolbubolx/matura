# rozkład na czynniki pierwsze
def rozkład(liczba):
    czynniki = []
    dzielnik = 2
    while liczba != 1:
        while liczba % dzielnik == 0:
            liczba = liczba // dzielnik
            czynniki.append(dzielnik)
        dzielnik += 1
    return czynniki
print(rozkład(1187))
