import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import accuracy_score

# Örnek veri
# [çalışma saati, ders devamı]
X = np.array([
    [2,60],
    [3,65],
    [4,70],
    [5,75],
    [6,80],
    [7,85],
    [8,90],
    [9,95]
])

# 0 = kaldı, 1 = geçti
y = np.array([0,0,0,0,1,1,1,1])

# Model oluşturma
lda = LinearDiscriminantAnalysis()
lda.fit(X, y)

# Tahmin
tahmin = lda.predict(X)

# Doğruluk
accuracy = accuracy_score(y, tahmin)

print("Tahminler:", tahmin)
print("Accuracy:", accuracy)

# Yeni veri tahmini
yeni_veri = np.array([[6,85]])
sonuc = lda.predict(yeni_veri)

print("6 saat çalışma ve %85 devam için sonuç:", sonuc[0])