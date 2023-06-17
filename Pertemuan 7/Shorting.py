import timeit
print("----------ASCENDING----------")
print(" ")

#Insertion Sort
def insertion_sort(array):
    start = timeit.default_timer()
    for i in range(1, len(array)):
        item = array[i]
        j = i - 1

        while j >= 0 and array[j] > item:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = item

    stop = timeit.default_timer()
    print(f"Insertion Sort successful! Elapsed time: {stop - start}")

    return array

#Bubble Sort
def bubble_sort(array):
    start = timeit.default_timer()

    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    stop = timeit.default_timer()
    print(f"Bubble Sort successful! Elapsed time {stop - start}")

    return array

#Selection Sort
def selection_sort(array):
    start = timeit.default_timer()

    for i in range(len(array)):
        min_index = i

        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

    stop = timeit.default_timer()
    print(f"Selection Sort successful! Elapsed time: {stop - start}")

    return array


# Uji Coba
list_a = [7, 14, 84, 93, 74, 100]
list_b = [7, 14, 84, 93, 74, 100]
list_c = [7, 14, 84, 93, 74, 100]

print(f"Before: {list_a}")
insertion_sort(list_a)
print(f"After: {list_a}")
print(" ")


print(f"Before: {list_b}")
bubble_sort(list_b)
print(f"After: {list_b}")
print(" ")


print(f"Before: {list_c}")
selection_sort(list_c)
print(f"After: {list_b}")
print(" ")


print("----------DESCENDING----------")
print(" ")

#Insertion sort
def insertion_sort(array):
    start = timeit.default_timer()
    for i in range(1, len(array)):
        item = array[i]
        j = i - 1

        while j >= 0 and array[j] < item:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = item

    stop = timeit.default_timer()
    print(f"Insertion Sort successful! Elapsed time: {stop - start}")

    return array

#Bubble sort
def bubble_sort(array):
    start = timeit.default_timer()

    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    stop = timeit.default_timer()
    print(f"Bubble Sort successful! Elapsed time {stop - start}")

    return array

#Selection sort
def selection_sort(array):
    start = timeit.default_timer()

    for i in range(len(array)):
        min_index = i

        for j in range(i + 1, len(array)):
            if array[min_index] < array[j]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

    stop = timeit.default_timer()
    print(f"Selection Sort successful! Elapsed time: {stop - start}")

    return array


# Uji Coba
list_a = [10, 28, 84, 93, 74, 100]
list_b = [10, 28, 84, 93, 74, 100]
list_c = [10, 28, 84, 93, 74, 100]

print(f"Before: {list_a}")
insertion_sort(list_a)
print(f"After: {list_a}")
print(" ")


print(f"Before: {list_b}")
bubble_sort(list_b)
print(f"After: {list_b}")
print(" ")


print(f"Before: {list_c}")
selection_sort(list_c)
print(f"After: {list_b}")
print(" ")