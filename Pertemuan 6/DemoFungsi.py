#Penamaan fungsi:
#hitungKelilingPersegi
#hitung_keliling_persegi

#Fungsi menghitung keliling persegi
def hitung_keliling_persegi(sisi):
    hasil = 4 * sisi
    return hasil

#Fungsi menghitung luas persegi
def hitung_luas_persegi(sisi):
    hasil = sisi * sisi
    return hasil

user_input = int(input("Masukkan sisi persegi : "))
print(f"Keliling Persegi : {hitung_keliling_persegi(user_input)}")
print(f"Luas Persegi : {hitung_luas_persegi(user_input)}")
