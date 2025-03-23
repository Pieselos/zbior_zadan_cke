plik = open('../dane/61/ciagi.txt')
tekst = plik.readlines()
plik.close()
liczba_arytmetycznych = 0
najwieksza_roznica = -1
for linia in tekst[1::2]:

    tablica = linia.strip().split(' ')
    roznica = int(tablica[1]) - int(tablica[0])
    if roznica > najwieksza_roznica:
        najwieksza_roznica = roznica
    for i in range(0,len(tablica)-1):
        if int(tablica[i+1]) - int(tablica[i]) != roznica:
            break
    else:
        liczba_arytmetycznych+=1

print(liczba_arytmetycznych,najwieksza_roznica)




