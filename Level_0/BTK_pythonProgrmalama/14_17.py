import random
import sorting_algorithms
import search_algorithms

numbers = [random.randint(1,100) for _ in range(10)]
print("liste: ",numbers)

numbers = sorting_algorithms.merge_sort(numbers)
print("sıralı liste: ",numbers)

target = int(input("hedef değeri giriniz(1-100): "))

index = search_algorithms.binary_search(numbers, target, 0, len(numbers)-1)

if index != -1:
    print("hedef bulundu! indeks: ", index)
else:
    print("hedef bulunamadı.")