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

minimalna_s1 = s1_int[0][1]
minimalna_s2 = s2_int[0][1]
minimalna_s3 = s3_int[0][1]
for i in s1_int:
    if i[1]<minimalna_s1:
        minimalna_s1 = i[1]

minimalna = s2_int[0][1]
for i in s2_int:
    if i[1]<minimalna_s2:
        minimalna_s2 = i[1]

minimalna = s3_int[0][1]
for i in s3_int:
    if i[1]<minimalna_s3:
        minimalna_s3 = i[1]
minimalna_s1 = bin(minimalna_s1)
minimalna_s1 = minimalna_s1.replace('0b','')
minimalna_s2 = bin(minimalna_s2)
minimalna_s2 = minimalna_s2.replace('0b','')
minimalna_s3 = bin(minimalna_s3)
minimalna_s3 = minimalna_s3.replace('0b','')

print(minimalna_s1,minimalna_s2,minimalna_s3)