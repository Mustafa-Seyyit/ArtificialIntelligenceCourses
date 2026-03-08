import numpy as np
from sklearn.cluster import KMeans

# Örnek veri
X = np.array([
    [1, 2],
    [1, 3],
    [2, 2],
    [8, 8],
    [8, 9],
    [9, 8]
])

# KMeans modeli
model = KMeans(n_clusters=2, random_state=42, n_init=10)
model.fit(X)

# Küme etiketleri
etiketler = model.labels_

print("Küme etiketleri:")
print(etiketler)

# Küme merkezleri
print("Küme merkezleri:")
print(model.cluster_centers_)