#BY ROOTKURBANI // ROOTKURBANI TARAFINDAN.
#BEOC (BASIC ENCRYPTION OUTPUT CODE) // BŞÇK (BASİT ŞİFRELEME ÇIKIŞ KODU)



#m*n=f
#f(m+n)=b
#b*f=l
#l(b-f)=a
#a*n^m=o

#m = INP1
#n = INP2
#f = CAL1
#b = CAL2
#l = CAL3
#a = CAL5
#o = RES1

import sys

sys.set_int_max_str_digits(2**30) #INCREASING PYTHON OUTPUT LIMIT// PYTHON ÇIKIŞ KODU ARTTIRMAK İÇİN

m = int(input())
n = int(input())

f = m+n #CALCULATION 1 // HESAP 1
print("RESULT/SONUÇ:	",f) #DEBUGGING1 // AYIKLAMA1

b = f*(m+n) #CALCULATION 2 // HESAP 2
print("RESULT/SONUÇ:	",b) #DEBUGGING2 // AYIKLAMA2

l = b*f #CALCULATION 3 //HESAP 3
print("RESULT/SONUÇ:	",l) #DEBUGGING3 // AYIKLAMA3

a = l*(b-f) #CALCULATION 4 // HESAP 4
print("RESULT/SONUÇ:	",a) #DEBUGGING4 // AYIKLAMA4

o = a*n**m #CALCULATION 5 // HESAP 5
print("RESULT/SONUÇ:	",o) ##DEBUGGING5 //AYIKLAMA5

#TR: Sanırım bu tuhaf  kod kalacak. Hoş gözüken sayılar oluşturabiliyor, belki effektlerde kullanışılıdır. Python matematiğini öğrenmek için yazmıştım bir ara.
