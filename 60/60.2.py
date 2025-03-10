plik = open('../dane/60/liczby.txt')
tekst = plik.readlines()
plik.close()

tab_int = []
for linia in tekst:
    tab_int.append(int(linia.strip()))


assoc = dict()

for i in tab_int:
    tab_dzielniki = []
    for j in range(1,i+1):
        if i%j==0:
            tab_dzielniki.append(j)



    if len(tab_dzielniki) == 18:
        assoc[i] = tab_dzielniki

print(assoc)