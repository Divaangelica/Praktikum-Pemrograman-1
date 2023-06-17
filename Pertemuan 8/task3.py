def insertion_sort(data):

    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key
    return convert_data_to_string(data)


def convert_data_to_string(data):
    converted_data = []

    for i in data:
        converted_data.append(str(i).lower())

    return converted_data


def binary_search(data, keyword):
    converted_data = convert_data_to_string(data)
    sorted_data = insertion_sort(converted_data)
    print(f"Data Sorted: {sorted_data}")
    low = 0
    high = len(sorted_data) - 1

    while low <= high:
        mid = (low + high) // 2

        if sorted_data[mid] == keyword:
            print(f"{keyword} is found at index {mid}")
            return mid

        elif str(sorted_data[mid]) < str(keyword):
            low = mid + 1

        else:
            high = mid - 1

    print(f"{keyword} is not found")
    return -1


data = [21, 61, 28, 72, 44, 68, 37, 52, 75, 71]
keyword = '71'
binary_search(data, keyword)
