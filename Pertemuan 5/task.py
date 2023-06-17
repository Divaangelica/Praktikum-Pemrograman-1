jum_matkul = int(input('Masukkan Jumlah Mata Kuliah : '))
matkul = [ ]
total = 0

for a in range(jum_matkul):
    nilai = int(input("Masukkan nilai mata kuliah ke-{}: ".format(a+1)))
    matkul.append(nilai)
    
nilai = sum (matkul)/a

if (100 > nilai >=90):
    print ("Hasil predikat A dengan nilai :")
    print (matkul)
            
elif (90 > nilai >= 70):
    print ("Hasil predikat B dengan nilai :")
    print (matkul)

elif (70 > nilai >= 50):
    print ("Hasil predikat C dengan nilai :")
    print (matkul)
            
elif (50 > nilai >= 30):
    print ("Hasil predikat D dengan nilai :")
    print (matkul)

elif (30 > nilai >= 0):
    print ("Hasil predikat E dengan nilai :")
    print (matkul)

else:
    print("Nilai tidak valid!")