import math

"""
PROBLEM:Bir modelin doğru tahmin yapma olasılığı %70.
    10 tahminden tam 8’ini doğru yapma olasılığını hesaplayan kodu yaz.
"""

def binom(n, k, p):
    if not (0 <= p <= 1):
        raise ValueError("p 0 ile 1 arasında olmalı")
    if not (0 <= k <= n):
        raise ValueError("k, 0 ile n arasında olmalı")
    sonuc = math.comb(n,k)* p **k * ((1-p) ** (n-k))
    return sonuc

p = 0.7
n = 10
k = 8

print("Olasılık:", binom(n, k, p))