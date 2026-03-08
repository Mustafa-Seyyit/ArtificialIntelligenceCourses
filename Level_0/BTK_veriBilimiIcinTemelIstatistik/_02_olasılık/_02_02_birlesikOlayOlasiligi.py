from fractions import Fraction

def olasilik_kume(omega, A):
    omega = set(omega)
    A = set(A) & omega
    if not omega:
        raise ValueError("Örnek uzay boş olamaz.")
    return Fraction(len(A), len(omega))

def birlesim_olasiligi(omega, A, B):
    omega = set(omega)
    A = set(A) & omega
    B = set(B) & omega

    AuB = A | B
    AintB = A & B

    P_A = olasilik_kume(omega, A)
    P_B = olasilik_kume(omega, B)
    P_AintB = olasilik_kume(omega, AintB)

    P_AuB = P_A + P_B - P_AintB
    return AuB, P_AuB


# ÖRNEK: Zar
omega = {1,2,3,4,5,6}
A = {2,4,6}        # çift
B = {4,5,6}        # 4-6 arası
AuB, P = birlesim_olasiligi(omega, A, B)
print("A∪B =", AuB, "P(A∪B) =", P)  # {2,4,5,6}, 2/3