"""
PROBLEM: Bir sınıftaki öğrencilerin notları:
    veri = [45, 50, 67, 70, 72, 85, 90, 95]
    Bu veri setinin ranjını (range) hesaplayan bir Python fonksiyonu yazınız.
"""

veri = [45, 50, 67, 70, 72, 85, 90, 95]

def ranj_hesapla(veri):
    minimum = min(veri)
    maximum = max(veri)
    return maximum - minimum

print("ranj: ", ranj_hesapla(veri))
