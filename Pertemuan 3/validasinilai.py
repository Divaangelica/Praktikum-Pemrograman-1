bilangan = int(input("Masukkan bilangan yang akan dibagi: "))
pembagi = int(input("Masukkan bilangan pembagi: "))

if pembagi == 0:
    print ("Pembagi tidak boleh 0")

else:
    print(f"Hasil bagi dari dari {bilangan} dan {pembagi} adalah {bilangan/pembagi}")