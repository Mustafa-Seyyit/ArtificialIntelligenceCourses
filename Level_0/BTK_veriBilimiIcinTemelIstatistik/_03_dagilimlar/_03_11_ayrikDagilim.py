"""
PRLOBLEM: Bir sınıflandırma modelinin çıktısı:
[0.2, 0.3, 0.1, 0.4]
Toplamının 1 olup olmadığını kontrol eden
En yüksek olasılığı bulan
fonksiyonu yaz.
"""

def ayrik_dagilim(data, tol = 1e-9):
    toplam = sum(data)
    toplam_1_mi = abs(toplam -1) < tol
    return toplam_1_mi
   
cikti = [0.2, 0.3, 0.1, 0.4]

if ayrik_dagilim(cikti):
    print("geçerli normal dağılım")
else:
    print("geçerli normal dağılım değil")