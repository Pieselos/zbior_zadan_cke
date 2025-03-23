plik = open("../dane/59/liczby.txt")
tekst = plik.readlines()
plik.close()
dict()
set()

def odwroc_tekst(linia):
    do_odwrocenia = list(linia)
    liczba_odrwocona = ''
    while do_odwrocenia:
        liczba_odrwocona = liczba_odrwocona + do_odwrocenia.pop()
    return liczba_odrwocona


iterator = 0

for linia in tekst:
    linia = linia.strip()
    liczba_odwrocona = odwroc_tekst(linia)
    suma = int(linia)+int(liczba_odwrocona)
    suma = str(suma)
    for x:
        break
    else:


    print(linia,liczba_odwrocona, suma)
    if suma == odwroc_tekst(suma):
        iterator+=1

print(iterator)

