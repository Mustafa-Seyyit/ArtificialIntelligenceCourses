import numpy as np
from sklearn.decomposition import FactorAnalysis
from sklearn.preprocessing import StandardScaler

# Örnek veri
# [matematik, fizik, kimya, biyoloji notları]
X = np.array([
    [70,65,60,75],
    [80,78,72,85],
    [60,55,58,65],
    [90,88,85,92],
    [75,70,68,80],
    [65,60,62,70]
])

# Veriyi standartlaştırma
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Faktör analizi (2 faktöre indiriyoruz)
fa = FactorAnalysis(n_components=2)
X_factors = fa.fit_transform(X_scaled)

print("Faktör skorları:")
print(X_factors)

print("Faktör yükleri:")
print(fa.components_)