import search_algorithms

numbers = [1,40,42,4,6,23]

target = int(input("hedef değeri giriniz: "))

index = search_algorithms.linear_search(numbers, target)
if index != -1:
    print("hedef bulundu. index değeri: ", index)
else:
    print("hedef bulunamadı.")