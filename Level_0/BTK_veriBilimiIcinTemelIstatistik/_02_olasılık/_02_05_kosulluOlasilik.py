from fractions import Fraction

def kosullu_olasilik(omega, A, B):
    omega = set(omega)
    A = set(A) & omega
    B = set(B) & omega

    if not omega:
        raise ValueError("Örnek uzay boş olamaz.")

    PB = Fraction(len(B), len(omega))
    if PB == 0:
        raise ValueError("P(B)=0 olduğu için koşullu olasılık tanımsızdır.")

    AintB = A & B
    PAintB = Fraction(len(AintB), len(omega))
    return Fraction(PAintB, PB)  # (PA∩B) / PB


# ÖRNEK: Zar
omega = {1,2,3,4,5,6}
A = {4,5,6}     # >=4
B = {2,4,6}     # çift
print("P(A|B) =", kosullu_olasilik(omega, A, B))  # 2/3