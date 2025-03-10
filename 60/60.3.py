plik = open('../dane/60/liczby.txt', 'r')
wiersze = plik.readlines()

# ZADANIE 60.1.
liczby_mniejsze_od_1000 = []
for wiersz in wiersze:
    liczba = int(wiersz.strip())
    if liczba < 1000:
        liczby_mniejsze_od_1000.append(liczba)

ile_mniejszych = len(liczby_mniejsze_od_1000)
print('ZADANIE 60.1.')
print(f'MNIEJSZYCH OD 1000: {ile_mniejszych}')
print(f'OSTATNIE DWIE LICZBY: {liczby_mniejsze_od_1000[ile_mniejszych - 2]}, {liczby_mniejsze_od_1000[ile_mniejszych - 1]}')

# ZADANIE 60.2.
def znajdź_dzielniki(liczba):
    dzielniki = []
    for n in range(1, liczba + 1):
        if liczba % n == 0:
            dzielniki.append(n)

    return dzielniki
""""
print('\nZADANIE 60.2.')
for wiersz in wiersze:
    liczba = int(wiersz.strip())
    dzielniki = znajdź_dzielniki((liczba))

    if len(dzielniki) == 18:
        print(f'LICZBA: {liczba}, DZIELNIKI: {dzielniki}')
"""
# ZADANIE 60.3.
import math
max_względnie_pierwsza = int(wiersze[0])
dzielniki = []

for i in range(0, len(wiersze)):
    liczba = int(wiersze[i])
    dzielniki_lokalne = znajdź_dzielniki(liczba)
    dzielniki.append(dzielniki_lokalne)

for i in range(0, len(wiersze)):
    czy_względnie_pierwsza = True
    for j in range(0, len(wiersze)):
        if wiersze[i] == wiersze[j]:
            continue
        liczba_1 = int(wiersze[i])
        liczba_2 = int(wiersze[j])
        if math.gcd(liczba_1, liczba_2) > 1:
            czy_względnie_pierwsza = False

    if czy_względnie_pierwsza:
        if max_względnie_pierwsza < int(wiersze[i]):
            max_względnie_pierwsza = int(wiersze[i])

print('\nZADANIE 60.3.')
print(max_względnie_pierwsza)