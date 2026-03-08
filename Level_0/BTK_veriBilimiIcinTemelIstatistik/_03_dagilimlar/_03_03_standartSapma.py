from _03_02_Varyans import varyans_hesapla
import math
"""
PROBLEM: Aşağıdaki veri setinin örnek standart sapmasını hesaplayan kodu yazınız:
    veri = [10, 12, 23, 23, 16, 23, 21, 16]
"""



def standart_sapma_hesapla(veri):
    varyans = varyans_hesapla(veri)
    standart_sapma = math.sqrt(varyans)
    return standart_sapma


if __name__ == "__main__":
    veri = [10, 12, 23, 23, 16, 23, 21, 16]    
    print("standart sapma: ", standart_sapma_hesapla(veri))
