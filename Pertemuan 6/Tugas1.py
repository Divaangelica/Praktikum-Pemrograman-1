# Fungsi menampilkan bilangan ganjil genap

def genap(x):
    if (x > 0):
        return genap(x-2)
    elif (x == 0):
        return genap
    elif (x == 1):
        return genap


bil = int(input("Masukkan bilangan: "))
if (genap(bil)):
    print(f"Bilangan yang anda masukkan adalah genap")
else:
    print(f"Bilangan yang anda masukkan adalah ganjil")


# prosedur

def genap_ganjil(x):
    if (x % 2 == 0):
        print(x, 'adalah bilangan genap')
    else:
        print(x, 'adalah bilangan ganjil')


x = int(input("Masukkan bilangan: "))
genap_ganjil(x)
