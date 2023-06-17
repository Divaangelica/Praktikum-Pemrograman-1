print("===== PROGRAM SEDERHANA MENGHITUNG JUMLAH TOTAL BILANGAN =====") 
      
total = 0
bilangan = int(input('Masukkan bilangan = '))

print ('Total Nilai =', end = ' ')

while bilangan >= 1:
    print(bilangan, end = ' ')
    if 1 == bilangan:
        print('=', end = ' ')
    else :
        print('+', end = ' ')
    total = total + bilangan
    bilangan = bilangan - 1

print (total)

