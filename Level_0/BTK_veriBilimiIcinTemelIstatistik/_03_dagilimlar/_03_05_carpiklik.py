from _03_03_standartSapma import standart_sapma_hesapla
"""
PROBLEM:Aşağıdaki veri setinin örnek çarpıklığını hesaplayan kodu yazınız
    veri = [2, 4, 5, 6, 8, 12, 15]
"""

veri = [2, 4, 5, 6, 8, 12, 15]

def carpiklik_hesapla(data):
    ortalama = sum(data) / len(data)
    yeni_data = [x - ortalama for x in data]
    yeni_data = [y ** 3 for y in yeni_data]
    yeni_ortalama = sum(yeni_data) / len(yeni_data)
    standart_sapma = standart_sapma_hesapla(data)
    carpiklik = yeni_ortalama / (standart_sapma **3)
    return carpiklik

carpiklik = carpiklik_hesapla(veri)
if carpiklik < 0:
    print("sola çarpık dağılım")
elif carpiklik > 0:
    print("sağa çarpık dağılım")
else:
    print("simetrik dağılım")