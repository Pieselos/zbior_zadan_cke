plik = open("../dane/58/dane_systemy1.txt")
s1 = plik.readlines()
plik.close()
plik = open("../dane/58/dane_systemy2.txt")
s2 = plik.readlines()
plik.close()
plik = open("../dane/58/dane_systemy3.txt")
s3 = plik.readlines()
plik.close()

s1_int = []
for linia in s1:
    tab = linia.strip().split(' ')
    s1_int.append([int(tab[0],2) , int(tab[1],2)])
s2_int = []
for linia in s2:
    tab = linia.strip().split(' ')
    s2_int.append([int(tab[0],4) , int(tab[1],4)])
s3_int = []
for linia in s3:
    tab = linia.strip().split(' ')
    s3_int.append([int(tab[0],8) , int(tab[1],8)])

aktualny_rekord_s1 = s1_int[0][1]
aktualny_rekord_s2 = s2_int[0][1]
aktualny_rekord_s3 = s3_int[0][1]
liczba_dni_rekordowych = 1

for i in range(1,len(s3_int)):
    if(aktualny_rekord_s1<s1_int[i][1] or aktualny_rekord_s2<s2_int[i][1] or aktualny_rekord_s3<s3_int[i][1]):
        liczba_dni_rekordowych+=1
    if aktualny_rekord_s1<s1_int[i][1]:
        aktualny_rekord_s1 = s1_int[i][1]
    if aktualny_rekord_s2<s2_int[i][1]:
        aktualny_rekord_s2 = s2_int[i][1]
    if aktualny_rekord_s3<s3_int[i][1]:
        aktualny_rekord_s3 = s3_int[i][1]

print(liczba_dni_rekordowych)
