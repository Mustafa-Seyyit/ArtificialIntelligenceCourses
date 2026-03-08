from fractions import Fraction

def ayrik_mi(A, B):
    A, B = set(A), set(B)
    return (A & B) == set()

def ayrik_birlesim_olasiligi(omega, A, B):
    omega = set(omega)
    A = set(A) & omega
    B = set(B) & omega

    if not ayrik_mi(A, B):
        raise ValueError("A ve B ayrık değil (kesişim boş değil).")

    P_A = Fraction(len(A), len(omega))
    P_B = Fraction(len(B), len(omega))
    return (A | B), (P_A + P_B)


# ÖRNEK: Zar -> A={1,2}, B={5,6} ayrık
omega = {1,2,3,4,5,6}
A = {1,2}
B = {5,6}
AuB, P = ayrik_birlesim_olasiligi(omega, A, B)
print("A ayrık mı B?", ayrik_mi(A, B))
print("P(A∪B) =", P)  # 2/3? hayır: 4/6 = 2/3 doğru