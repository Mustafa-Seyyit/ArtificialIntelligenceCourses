"""
PROBLEM: Aşağıdaki veri setinin basıklığını (kurtosis) hesaplayan kodu yazınız:
    veri = [3, 5, 7, 8, 9, 10, 12]
"""

veri = [3, 5, 7, 8, 9, 10, 12]

def basiklik_hesapla(data):
    n = len(data)
    ortalama = sum(data)
    sapmalar = [x - ortalama for x in data]
    ikinci_moment = sum(s**2 for s in sapmalar) / n
    dorduncu_moment = sum(s**4 for s in sapmalar) / n
    
    basiklik = dorduncu_moment / (ikinci_moment ** 2)

    return basiklik

sonuc = basiklik_hesapla(veri)
print("basiklik:", sonuc)
