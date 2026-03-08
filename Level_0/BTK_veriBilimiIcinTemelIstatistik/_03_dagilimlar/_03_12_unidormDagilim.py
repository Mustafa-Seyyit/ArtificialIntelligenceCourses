"""
PROBLEM: [2, 8] aralığında:
f(x) değerini hesaplayan
varyansını hesaplayan
kod yaz.
"""

def varyans_hesapla(alt, ust):
    sonuc = ((ust - alt) ** 2) / 12
    return sonuc

def uniform(x, alt, ust):
    if alt <= x <= ust:
        return 1 / (ust - alt)
    else:
        return 0
    
alt = 2
ust = 8

print("Varyans:", varyans_hesapla(alt, ust))
print("f(5):", uniform(5, alt, ust))