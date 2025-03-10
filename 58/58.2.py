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

b = s1_int[0][0]
iterator = 0
for i in range(0, len(s1_int)):

    if(s1_int[i][0]-b) % 24 != 0 and (s2_int[i][0]-b) % 24 != 0 and (s3_int[i][0]-b) % 24 != 0:
        iterator+=1
print(iterator)