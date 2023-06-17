# Program untuk mengurutkan IPS mahasiswa

def bubble_sort(ips):
    for i in range(len(ips)):
        for j in range(len(ips) - i - 1):
            if ips[j] < ips[j + 1]:
                ips[j], ips[j + 1] = ips[j + 1], ips[j]

    return ips

ips_mhs = [3.8, 2.9, 3.3, 4.0, 2.7]

print(f"Indeks Prestasi Semester (IPS) ")
print(f"List sebelum diurutkan : {ips_mhs}")
bubble_sort(ips_mhs)
print(f"List setelah diurutkan : {ips_mhs}")
print(" ")
