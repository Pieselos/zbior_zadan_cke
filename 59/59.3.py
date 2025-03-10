def w(n):
    tab_n = list(str(n))
    moc = 0
    while len(tab_n)>1:
        iloczyn = 1
        for i in tab_n:
            iloczyn*=int(i)
        tab_n = list(str(iloczyn))
        moc+=1
    return moc
plik = open("../dane/59/liczby.txt")
tekst = plik.readlines()
plik.close()

tablica_mocy = dict()
for i in range(1,9):
    tablica_mocy[i] = 0

flaga = True
print(tekst[0])
for linia in tekst:
    liczba = int(linia.strip())
    moc = w(liczba)
    if moc>8:
        continue
    if moc == 1:
        if flaga:
            max_moc_1 = liczba
            min_moc_1 = liczba
            flaga = False
        if max_moc_1 < liczba:
            max_moc_1 = liczba
        if min_moc_1 > liczba:
            min_moc_1 = liczba
    tablica_mocy[moc]+=1

print(tablica_mocy)
print(min_moc_1,max_moc_1)


