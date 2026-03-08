import statistics

def veri_al():
    print("verileri giriniz çıkmak için 'a' giriniz.")
    veri = []
    while True:
        eleman = input("eleman: ")
        if eleman == 'a':
            break
        else:
            try:
                veri.append(float(eleman.strip()))
            except ValueError:
                print("lütfen nümerik bir değer giriniz")
    return veri

def mod_hesapla():
    veri = veri_al()

    while not veri:
        print("Veri seti boş olamaz, lütfen veri giriniz.\n")
        veri = veri_al()

    frekans = {}
    for eleman in veri:
        frekans[eleman] = frekans.get(eleman, 0) + 1

    mod = max(frekans, key=frekans.get)
    print(f"Mod değeri: {mod}")

def medyan_bul():
    veri = veri_al()

    while not veri:
        print("Veri seti boş olamaz, lütfen veri giriniz.\n")
        veri = veri_al()
    uzunluk = len(veri)
    orta = uzunluk //2

    veri.sort()
    if uzunluk % 2 == 0:
        medyan =  (veri[orta] + veri[orta-1]) / 2
    else:
        medyan = veri[orta]

    print("medyan değeri: ", medyan)


def ceyrekleri_hesapla():
    veri = veri_al()

    while not veri:
        print("Veri seti boş olamaz, lütfen veri giriniz.\n")
        veri = veri_al()

    veri.sort()
    n = len(veri)

    Q2 = statistics.median(veri)

    # Alt ve üst yarılar
    if n % 2 == 0:
        alt_yari = veri[:n//2]
        ust_yari = veri[n//2:]
    else:
        alt_yari = veri[:n//2]
        ust_yari = veri[n//2 + 1:]

    Q1 = statistics.median(alt_yari)
    Q3 = statistics.median(ust_yari)

    yari_ceyrek = (Q3 - Q1) / 2

    print(f"Alt çeyrek (Q1): {Q1}")
    print(f"Medyan (Q2): {Q2}")
    print(f"Üst çeyrek (Q3): {Q3}")
    print(f"Yarı çeyrek açıklığı: {yari_ceyrek}")

        
    
