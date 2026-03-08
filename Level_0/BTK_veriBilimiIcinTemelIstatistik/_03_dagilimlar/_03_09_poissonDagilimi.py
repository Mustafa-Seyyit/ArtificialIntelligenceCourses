import math
"""
PROBLEM: Bir web sitesine dakikada ortalama 4 ziyaret geliyor.
    Bir dakikada tam 6 ziyaret gelme olasılığını hesaplayan kodu yaz.
"""

e = math.e

def poisson(lam, k):
    if lam < 0:
        raise ValueError("lambda (lam) negatif olamaz.")
    if k < 0:
        raise ValueError("k negatif olamaz.")

    return (lam ** k) * math.exp(-lam) / math.factorial(k) # math.exp(-lam) = e ** -lam

lam = 4   
k = 6     
print(poisson(lam, k))
