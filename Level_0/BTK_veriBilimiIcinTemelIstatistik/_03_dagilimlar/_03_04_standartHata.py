from _03_03_standartSapma import standart_sapma_hesapla
import math

"""
PROBLEM: Bir örneklem için standart hata hesaplayan kodu yazınız.
    veri = [5, 7, 8, 6, 9, 4, 10, 6]
"""

veri = [5, 7, 8, 6, 9, 4, 10, 6]

def standart_hata_hesapla(data):
    standart_sapma= standart_sapma_hesapla(data)
    gozlem_sayisi = len(data)
    standart_hata = standart_sapma / math.sqrt(gozlem_sayisi)
    return standart_hata

print("standart hata: ", standart_hata_hesapla(veri))