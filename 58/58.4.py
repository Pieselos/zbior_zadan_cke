import math

plik = open("../dane/58/dane_systemy1.txt")
s1 = plik.readlines()
plik.close()
plik = open("../dane/58/dane_systemy2.txt")

s1_int = []
for linia in s1:
    tab = linia.strip().split(' ')
    s1_int.append([int(tab[0],2) , int(tab[1],2)])
najwiekszy_skok = 0
for i in range(0,len(s1_int)-1):
    for j in range(i+1,len(s1_int)):
        r = (s1_int[i][1]-s1_int[j][1])**2
        roznica = math.ceil(j-i)
        skok = r/roznica
        if skok > najwiekszy_skok:
            najwiekszy_skok = math.ceil(skok)


print(najwiekszy_skok)

