from fractions import Fraction

def kesisim_olasiligi(omega, A, B):
    omega = set(omega)
    A = set(A) & omega
    B = set(B) & omega

    AintB = A & B
    if not omega:
        raise ValueError("Örnek uzay boş olamaz.")
    return AintB, Fraction(len(AintB), len(omega))


# ÖRNEK
omega = {1,2,3,4,5,6}
A = {2,4,6}
B = {4,5,6}
AintB, P = kesisim_olasiligi(omega, A, B)
print("A∩B =", AintB, "P(A∩B) =", P)  # {4,6}, 1/3