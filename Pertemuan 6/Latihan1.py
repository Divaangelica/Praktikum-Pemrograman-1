#Menggunakan Fungsi 

def keliling_persegi(sisi):
    return 4 * sisi

def luas_persegi(sisi):
    return sisi * sisi

panjang = 8
print("Masukkan panjang sisi: %f" %panjang)
print("Kelilingnya adalah: %f" %keliling_persegi(panjang))
print("Luasnya adalah: %f" %luas_persegi(panjang))