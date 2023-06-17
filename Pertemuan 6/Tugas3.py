# Fungsi membuat kalkulator sederhana untuk dua bilangan

# Fungsi penjumlahan
def jumlah(x, y):
    hasil = x + y
    return hasil

# Fungsi perkalian


def kali(x, y):
    hasil = x * y
    return hasil

# Fungsi pembagian


def bagi(x, y):
    hasil = x / y
    return hasil


# Fungsi pengurangan
def kurang(x, y):
    hasil = x - y
    return hasil

# Fungsi pangkat


def pangkat(x, y):
    hasil = x ** y
    return hasil


# Menu operasi
print("         KALKULATOR           ")
print("1. Penjumlahan")
print("2. Perkalian")
print("3. Pembagian")
print("4. Pengurangan")
print("5. Pangkat")
pilihan = (input("Masukkan pilihan : "))


bil1 = int(input("Bilangan pertama  : "))
bil2 = int(input("Bilangan kedua    : "))


if pilihan == '1':
    print(f"Hasil penjumlahan : {jumlah(bil1, bil2)}")

elif pilihan == "2":
    print(f"Hasil perkalian : {kali(bil1, bil2)}")

elif pilihan == "3":
    print(f"Hasil pembagian : {bagi(bil1, bil2)}")

elif pilihan == "4":
    print(f"Hasil pengurangan : {kurang(bil1, bil2)}")

elif pilihan == "5":
    print(f"Hasil pangkat : {pangkat(bil1, bil2)}")

else:
    print("TIDAK VALID")
