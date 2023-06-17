print("===== PROGRAM SEDERHANA MENGHITUNG PANGKAT =====") 

bil = int(input('Masukkan bilangan = '))
pangkat = int(input('Masukkan pencacah = '))

hasil = bil
for i in range(pangkat -1 ):
    hasil *= bil

print ('Hasil pangkat = ', hasil)
