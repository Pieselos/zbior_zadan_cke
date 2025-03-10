plik = open('../dane/60/liczby.txt')
tekst = plik.readlines()
plik.close()

tab_int = []
for linia in tekst:
    tab_int.append(int(linia.strip()))
tab_mn_1000 = []
for i in tab_int:
    if i < 1000:
        tab_mn_1000.append(i)

print(len(tab_mn_1000),tab_mn_1000[len(tab_mn_1000)-2],tab_mn_1000[len(tab_mn_1000)-1])