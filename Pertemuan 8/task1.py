def Data_Nopol(InputNo,Plat):
    print (f"Database Nomor Kendaraan : {Plat}")

    for i in range(len(Plat)):
        if str(Plat[i]).lower() == InputNo.lower():
            print(f"{InputNo} ada di dalam database")
            return 

    print(f"Nomor Kendaraan {InputNo} Tidak ada di database")
    return -1

data = ['R 300 SR', 'R 1234 DJ', 'R 3218 RR', 'R 701 LP', 'R 007 TU', 'R 3 ST', 'R 999 RT', 'R 210 RO', 'R 1111 II', 'R 4987 LH']
keyword = input("Masukkan Plat Nomor: ")
Data_Nopol(keyword, data)