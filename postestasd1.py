import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)

list_kosong = []

#mengisi list kosong dengan 10 angka acak
for i in range(10):
    list_kosong.append(random.randint(1, 100))

#menampilkan list sebelum diurutkan
print("List sebelum diurutkan:")
print(list_kosong)

#mengurutkan list menggunakan Quick Sort
list_kosong = quick_sort(list_kosong)

#menampilkan list setelah diurutkan
print("List setelah diurutkan:")
print(list_kosong)
