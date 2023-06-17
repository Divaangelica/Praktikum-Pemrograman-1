print("===== PROGRAM SEDERHANA MENCARI KPK =====") 
def fpb(x,y):
    if x > y:
        terkecil = y
    else :
        terkecil = x
    for i in range (1, terkecil +1):
        if((x % i == 0) and (y % i == 0)):
            fpb = i
    return fpb

def kpk(x,y):
    kpk = int(x * y / fpb(x,y))
    return kpk

bil1 = int(input('Masukkan bilangan pertama = '))
bil2 = int(input('Masukkan bilangan kedua = '))

print("KPK = ", kpk(bil1, bil2))

