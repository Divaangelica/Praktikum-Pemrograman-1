#Menggunakan prosedur

def perbedaan_bilangan(a,b):
    if a < b:
        print("Bilangan", a, "lebih kecil dari", b)
    elif a > b:
        print("Bilangan", a, "lebih besar dari", b)
    elif a == b:
        print("Nilainya sama")

a = int(input("Masukkan bilangan pertama : "))
b = int(input("Masukkan bilangan kedua : "))
perbedaan_bilangan(a,b)