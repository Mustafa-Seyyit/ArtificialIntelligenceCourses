
"""
PROBLEM:Bir makinenin doğru tahmin yapma olasılığı %80.
    1 denemede:
        doğru tahmin olasılığı
        yanlış tahmin olasılığı
    hesaplayan fonksiyonu yaz.  
"""

def bernoulli(p, x):
    if x not in (0,1):
        raise ValueError("x 0 ile 1 arasında olmalıdır")
    if not 0 <= p <= 1:
        raise ValueError("p 0 ile 1 arasında olmalıdır")
    
    sonuc = (p ** x) * ((1-p) ** (1-x))
    return sonuc

p = 0.8
x = 1

print("olasılık: ", bernoulli(p, x))