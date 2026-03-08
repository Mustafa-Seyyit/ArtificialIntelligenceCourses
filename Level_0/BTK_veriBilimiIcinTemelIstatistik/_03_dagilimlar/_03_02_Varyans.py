"""
PROBLEM: Aşağıdaki veri setinin örnek varyansını (sample variance) hesaplayan kodu yazınız:
    veri = [4, 8, 6, 5, 3, 7]
"""
import statistics

def varyans_hesapla(veri):
    ortalama = statistics.mean(veri)
    yeni_veri = [x - ortalama for x in veri]
    kare_veri = [y**2 for y in yeni_veri]
    varyans = sum(kare_veri) / (len(kare_veri)-1)
    return varyans

if __name__ == "__main__":
    data = [4, 8, 6, 5, 3, 7]
    print("varyans:", varyans_hesapla(data))