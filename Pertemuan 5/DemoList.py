#Pembuatan list sekaligus diisi nilainya
#Index adalah urutan yang dimulai dari 0
kpop = ["Namjoon", "Seokjin", "Yoongi", "", "Jimin", "Taehyung", "Jungkook"]
Hoseok
#Cara melihat semua nilai menggunakan for
for i in kpop:
    print (i)

#Cara melihat semua nilai menggunakan print
print(kpop)

#Cara melihat nilai tertentu 
print(kpop[6])

#Cara memasukkan data ke list (urutan terakhir)
kpop.append("Jake")

#Cara memasukkan data ke list (urutan tertentu)
#index (index, data)
kpop.insert(1, "Sunghoon")

#Caraa mengosongkan seluruh data dilist
kpop.clear()

#Cara menghapus data dilist index tertentu
kpop.pop(7)

#Cara menghapus data di list dengan memasukkan data yang ingin dihapus
#Apabila ada data yang sama maka data yang terhapus adalah data yang pertama 
kpop.remove("Jake")

#Untuk mengganti sebuah nilai
kpop[1] = "Jay"

#Cara salah menggandakan data 
penyanyi = kpop #apabila kita ingin menghapus salah satu data di kpop maka data di penyanyi juga akan terhapus
#karena mereka memiliki objek yang sama hanya saja namanya beda

# Cara 1 menggandakan list (buat dari awal)
penyanyi = kpop.copy()

#Cara 2 menggandakan list (sekadar menambah nilai ke list yg ada)
penyanyi.extend(kpop)

# Cara mengurutkan 
kpop.sort()

# Cara membalik urutan
kpop.reverse()