from fractions import Fraction

def klasik_olasilik(omega, olay):
    """
    omega: örnek uzay (list/set/tuple)
    olay: olay kümesi (list/set/tuple) veya omega üzerinde filtre fonksiyonu (callable)

    Dönüş: Fraction (tam kesir)
    """
    omega = list(omega)
    if len(omega) == 0:
        raise ValueError("Örnek uzay (omega) boş olamaz.")

    if callable(olay):
        A = [w for w in omega if olay(w)]
    else:
        A = set(olay)
        # omega dışındaki elemanları otomatik dışarıda bırak
        A = [w for w in omega if w in A]

    return Fraction(len(A), len(omega))


# ÖRNEK: Adil zar -> A = {4,5,6}
omega_zar = [1, 2, 3, 4, 5, 6]
print("P(A) =", klasik_olasilik(omega_zar, {4, 5, 6}))  # 1/2

