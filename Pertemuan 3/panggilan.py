gender = input("Laki-laki atau Perempuan? (L/P): ")
status = input("Anda sudah menikah atau belum? (Y/N): ")

if gender=="P" or "p" and status=="N" or "n":
    print("Hallo, Mbak!")

elif gender=="P" or "p" and status=="Y" or "y":
    print("Hallo, Ibu!")

elif gender=="L" or "l" and status=="N" or "n":
    print("Hallo, Mas!")

else:
    print("Hallo, Bapak!")