def giris_al(message, type):
    if type == 1: #int al
        return int(input(message))
    elif type == 2: #float al
        return float(input(message))
    else:
        return -float('inf')


def aritmetik_ortalama_hesapla():
    print("aritmatik ortalamasını almak istediğiniz değerleri giriniz: ")
    print("çıkmak için -1 giriniz\n")
    
    toplam = 0
    adet = 0
    sira = 1

    while True:
        try:
            eleman = giris_al(f"{sira}. eleman: ", 1)
            if eleman == -1:
                break
            adet += 1
            sira += 1
            toplam += eleman
        except ValueError:
            print("lütfen sadece tam sayı giriniz.")

    if adet == 0:
        print("hiçbir değer girilmedi, ortalama: 0")
    else:
        ortalama = toplam / adet
        print(f"aritmatik ortalama: {ortalama}")


def agirlikli_ortalama_hesapla():
    print("Ağırlıklı ortalama hesaplamak için her elemanın önce ağırlığını, sonra değerini giriniz.")
    print("Çıkmak için ağırlık olarak -1 giriniz.\n")

    toplam_agirlikli = 0
    toplam_agirlik = 0
    sira = 1

    while True:
        try:
            agirlik = giris_al(f"{sira}. elemanın ağırlığı: ", 1)
            if agirlik == -1:
                break

            if agirlik < 0:
                print("Ağırlık negatif olamaz. Çıkış için sadece -1 kullanınız.")
                continue

            deger = giris_al(f"{sira}. elemanın değeri: ", 1)

        except ValueError:
            print("Lütfen ağırlık ve değer için tam sayı giriniz.")
            continue

        toplam_agirlikli += agirlik * deger
        toplam_agirlik += agirlik
        sira += 1

    if sira == 1:
        print("Hiç değer çifti girilmedi. Ağırlıklı ortalama hesaplanamaz.")
    elif toplam_agirlik == 0:
        print("Toplam ağırlık 0 olduğu için ağırlıklı ortalama hesaplanamaz.")
    else:
        ortalama = toplam_agirlikli / toplam_agirlik
        print(f"Ağırlıklı ortalama: {ortalama}")

def geometrik_ortalama_hesapla():
    print("geometrik ortalamasını hesaplamak istediğiniz elemanları giriniz: ")
    print("çıkmak için -1 giriniz")
    
    carpim = 1
    adet = 0
    sira = 1

    while True:
        try:
            eleman = giris_al(f"{sira}. eleman: ", 1)
            if eleman == -1:
                break
            if eleman <= 0:
                print("lütfen pozitif tam sayi bir değer giriniz")
                continue
            carpim *= eleman
            adet += 1
            sira += 1
        except ValueError:
            print("lütfen tam sayi bir değer giriniz.")

    if adet == 0:
        print("eleman girilmedi geometrik ortalama hesaplanamaz.")
    else:
        try:
            ortalama = carpim ** (1 / adet)
        except OverflowError:
             print("Sayılar çok büyük olduğu için geometrik ortalama hesaplanamadı (taşma).")
        else:
            print(f"Geometrik ortalama: {ortalama}")

    

def harmonik_ortalama_hesapla():
    print("harmonik ortalamasını hesaplamak istediğiniz değerleri giriniz: ")
    print("çıkmak için -1 giriniz.")
    adet = 0
    tersler_toplami = 0

    while True:
        try:
            eleman = giris_al("eleman: ", 2)
            if eleman == 0:
                print("0 girilemez lütfen pozitif numerik bir değer giriniz")
                continue
            if eleman == -1:
                break
            if eleman <= 0:
                print("Harmonik ortalama için pozitif değer giriniz.")
                continue

            adet += 1
            tersler_toplami += 1/eleman
        except ValueError:
            print("lütfen bir numerik bir değer giriniz")

    if adet == 0:
        print("hiç eleman girilmedi ortalama hesaplanamaz")
    else:
        ortalama = adet / tersler_toplami
        print("girilen değerlerin harmonik ortalaması: ", ortalama)

