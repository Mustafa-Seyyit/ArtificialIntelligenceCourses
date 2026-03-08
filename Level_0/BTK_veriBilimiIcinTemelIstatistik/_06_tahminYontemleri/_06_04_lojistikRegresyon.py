import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# Örnek veri
# çalışma saati
X = np.array([1,2,3,4,5,6,7,8]).reshape(-1,1)

# sonuç (0 = kaldı, 1 = geçti)
y = np.array([0,0,0,0,1,1,1,1])

# model oluşturma
model = LogisticRegression()
model.fit(X, y)

# tahmin
tahmin = model.predict(X)

# doğruluk
accuracy = accuracy_score(y, tahmin)

print("Tahminler:", tahmin)
print("Accuracy:", accuracy)

# karışıklık matrisi
cm = confusion_matrix(y, tahmin)
print("Confusion Matrix:")
print(cm)

# yeni veri tahmini
yeni_veri = np.array([[6]])
sonuc = model.predict(yeni_veri)

print("6 saat çalışan öğrenci geçer mi?:", sonuc[0])