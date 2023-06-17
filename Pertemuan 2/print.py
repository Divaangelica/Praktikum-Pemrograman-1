#Basic
print("Belajar program Python")

#Basic with variable
belajar = "Pemrograman itu menyenangkan"
print(belajar)

#Print format (kekurangan tidak user friendly)
nama = "Melody"
print("Good moring, {}".format(nama))

item = "Blade"
cost = 4000
print("Item name: {}, cost {}".format(item, cost))

#Print plus (kekurangannya sensitif terhadap type datanya)
nama = "Diva"
print("Good night, " + nama)

item = "Shield"
cost = 5000
print("Item name: " + item + ", cost: " +  str(cost))

#Print F (user friendly dan tidak sensitif type data)
nama = "Jungkook"
print(f"Annyeong my name is, {nama}")

item = "01 September"
cost = "1997"
print(f"I was born on {item} {cost}")