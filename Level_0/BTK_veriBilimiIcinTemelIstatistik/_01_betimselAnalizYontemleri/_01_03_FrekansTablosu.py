import math

notlar = [45, 67, 89, 45, 72, 67, 90, 45, 72, 85, 90, 67, 72, 85, 45]


def frekans_tablosu(veri, sinif_sayisi):
    if not veri:
        print("Veri boş.")
        return

    sirali = sorted(veri)
    min_deger = sirali[0]
    max_deger = sirali[-1]

    ranj = max_deger - min_deger
    genislik = math.ceil(ranj / sinif_sayisi) if ranj != 0 else 1

    print("Veri:", veri)
    print("Sıralı:", sirali)
    print(f"Min: {min_deger}, Max: {max_deger}")
    print(f"Sınıf genişliği: {genislik}\n")

    alt = min_deger
    idx = 0
    n = len(sirali)

    for i in range(sinif_sayisi):
        ust = alt + genislik - 1
        if ust >= max_deger:
            ust = max_deger - 1

        sayac = 0
        while idx < n and alt <= sirali[idx] <= ust:
            sayac += 1
            idx += 1

        print(f"{i+1}. sınıf: {alt} - {ust} ---------> {sayac}")
        alt = ust + 1

        if alt >= max_deger:
            break

    print(f"{i+2}. sınıf: {max_deger} ve üzeri ---------> {veri.count(max_deger)}")


sinif_sayisi = int(input("Sınıf sayısını giriniz: "))
frekans_tablosu(notlar, sinif_sayisi)