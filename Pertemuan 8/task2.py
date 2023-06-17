def Sorting_awal (inputdata,nim):

    for i in range(len(nim)):
        min_index = i
        for j in range(i+1, len(nim)):
            if nim[j] < nim[min_index]:
                min_index = j
        nim[i], nim[min_index] = nim[min_index], nim[i]
    return binary_search(inputdata,nim)

def binary_search(inputdata,nim):
    left = 0
    right = len(nim) - 1
    
    while left <= right : 
        mid = (left+right)//2
        if str(nim[mid]).lower() > inputdata.lower() :
            right = mid - 1
        elif str(nim[mid]).lower() < inputdata.lower() :
            left = mid + 1
        else :
            print(f"\nData Mahassiswa yang hadir: {nim}")
            print(f"Nim : {inputdata} ada dikelas")
            return mid
    
    print(f"\nMahasiswa yang hadir: {nim}")
    print(f"Nim {inputdata} tidak ditemukan")
    return -1


nim = [12102002, 121002004, 12102001, 12102003, 12102005, 12102008, 12102007,12102006, 12102009, 121020013, 12102010, 12102012, 12102011]
inputdata = input("Masukkan Nim : ")
Sorting_awal(inputdata,nim)

