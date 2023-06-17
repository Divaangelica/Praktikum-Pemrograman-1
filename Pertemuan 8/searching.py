# 2 style penulisan fungsi
# Linear Search ()
l = [104, 100, 67, 102, 55, 70, 85, 80, 103,
     99, 100, 76, 98, 75, 77, 55, 81, 12, 111]
x = int(input('Masukan angka yang mau dicari: '))
idx = -1
for i in range(len(l)):
    if l[i] == x:
        idx = i
    break

if idx == -1:
    print('Nilai', x, 'ditemukan')
else:
    print('Nilai tidak ditemukan')

# # Linear_Search ()
# def linear_search(keyword, data):
#     cursor = -1

#     for i in range(len(data)):
#         if str(data[i]).lower() == keyword.lower():
#             print(f"{keyword} is found at index {i}")
#             return i

#     print(f"error: keyword {keyword} not found")
#     return -1


# # Binary Search ()
# # Binary_Search ()

# def insertion_sort(Variab):

#     for i in range(1, len(Variab)):
#         key = Variab[i]
#         j = i - 1

#         while j >= 0 and Variab[j] > key:
#             Variab[j + 1] = Variab[j]
#             j -= 1

#         Variab[j + 1] = key

#     return Variab


# def binary_search(keyword, data):

#     sorted_data = insertion_sort(data)
#     found = False
#     left = 0
#     right = len(data) - 1

#     while not found and left <= right:
#         mid = (left + right) // 2

#         if sorted_data[mid] == keyword:
#             found = True
#             break

#         elif sorted_data[mid] < keyword:
#             left = mid - 1

#         else:
#             right = mid + 1

#     print(f"error: keyword {keyword} not found")
#     return -1


# data = ['Namjoon', 'Seokjin', 'Yoongi', 'Hoseok', 'Jimin',
#         'Taehyung', 'Jungkook', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# keyword = input("Enter keyword: ")
# insertion_sort(keyword, data)
