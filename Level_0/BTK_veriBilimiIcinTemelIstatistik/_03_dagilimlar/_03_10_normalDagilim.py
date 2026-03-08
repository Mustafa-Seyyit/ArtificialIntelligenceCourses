import math

"""
PROBLEM: Bir veri setinde:
    Ortalama = 50
    Standart sapma = 5
    x = 60 değerinin olasılık yoğunluğunu hesaplayan kodu yaz."""

def normal(x, ortalama, std):
    return (1 / (std * math.sqrt(2 * math.pi))) * \
           math.exp(-((x - ortalama) ** 2) / (2 * std ** 2))


# Problem değerleri
ortalama = 50
std = 5
x = 60

print(normal(x, ortalama, std))