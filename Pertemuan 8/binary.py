#2 style penulisan fungsi
#linear_search()
#linearsearch()

#----------------------------------------------------------------
#function: lienar search
#melakukan pencarian satu perastu dari index pertama hingga terakhir
def linear_search(keyword,data):
    print (f"Data : {data}")

    for i in range(len(data)):
        if str(data[i]).lower() == keyword.lower():
            print(f"{keyword} is found at index {i}")
            return i

    print(f"error: keyword {keyword} not found")
    return -1
#----------------------------------------------------------------
#function: insertion sort(ascending)
#melakukan pengurutan data dengan menempatkan satu persatu data berdasarkan besarnya nilai data tersebut hingga urut. 
#Jenis pengurutan adalah dari nilai terkecil hingga nilai terbesar
def insertion_sort(data):

        for i in range(1, len(data)):
            key = data[i]
            j = i - 1

            while j>= 0 and  data[j] > key :
                data[j + 1] = data[j]
                j -= 1

            data[j + 1] = key
        return convert_data_to_string(data)
#function: convert data to string
#Melakukan konversi semua data di list menjadi string dan huruf kecil
def convert_data_to_string(data):
    converted_data = []
    
    for i in data:
        converted_data.append(str(i).lower())

    return converted_data

#function: binary search
#Melakukan pencarian dengan membelah lits menjadi 2. Data WAJIB urut!
def binary_search(data, keyword):
    converted_data = convert_data_to_string(data)
    sorted_data = insertion_sort(converted_data)
    print (f"Data Sorted: {sorted_data}")
    low = 0
    high = len(sorted_data) - 1

    while low <= high:
        mid = (low + high) // 2
        
        if sorted_data[mid] == keyword:
            print(f"{keyword} is found at index {mid}")
            return mid

        elif str(sorted_data[mid]) < str(keyword):
            low = mid + 1

        else :
            high = mid - 1

    print(f"{keyword} is not found")
    return -1

#--------Main--------
data = [5,2,1,3,4,6,7,8,9]
keyword = input("Enter keyword: ")
binary_search(data, keyword)