import math
plik = open("../dane/59/liczby.txt")
tekst = plik.readlines()
plik.close()
dzielniki = set()
def czy_spelnia_warunek(n):
    if n % 2 == 0:
        return False

    k = 3

    dzielniki.clear()
    while(n>1 and k <= math.sqrt(n)):
        if len(dzielniki) > 3:
            return False
        while(n%k == 0):
            dzielniki.add(k)
            n = n/k
        k+=1
    if n>1:
        dzielniki.add(int(n))


    if len(dzielniki) == 3:
        return True
    return False

iterator = 0

for linia in tekst:
    if czy_spelnia_warunek(int(linia)):
        iterator +=1

print(iterator)

