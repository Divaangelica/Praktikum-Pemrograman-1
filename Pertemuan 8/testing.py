def bubble_sort(keyword,data):
    
    for i in  range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j] > data[j+1] :
                data[j], data[j+1] = data[j+1], data[j]
    return binary_search(keyword,data)

def binary_search(keyword,data):
    left = 0
    right = len(data) - 1
    
    while left <= right : 
        mid = (left+right)//2
        if str(data[mid]).lower() > keyword.lower() :
            right = mid - 1
        elif str(data[mid]).lower() < keyword.lower() :
            left = mid + 1
        else :
            print(data)
            print(f"Keyword {keyword} has found at indeks {mid}")
            return mid
    
    print(f"Keyword {keyword} not found")
    return -1


data = [21, 61, 28, 72, 44, 68, 37, 52, 75, 71]
keyword = '71'
bubble_sort(keyword,data)