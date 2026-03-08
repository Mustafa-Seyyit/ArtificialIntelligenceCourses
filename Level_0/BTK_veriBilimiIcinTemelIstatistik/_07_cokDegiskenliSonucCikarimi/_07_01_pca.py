import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Örnek veri
# [çalışma saati, uyku saati, ders devamı]
X = np.array([
    [5,7,80],
    [6,6,85],
    [7,8,90],
    [4,5,70],
    [8,7,95],
    [3,6,65]
])

# Veriyi ölçekleme
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# PCA uygulama (3 boyutu 2 boyuta indiriyoruz)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print("Yeni veri (PCA sonrası):")
print(X_pca)

# Açıklanan varyans oranı
print("Explained Variance Ratio:")
print(pca.explained_variance_ratio_)