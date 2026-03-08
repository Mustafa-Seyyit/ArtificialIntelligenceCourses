import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Örnek veri
calisma_saati = np.array([1,2,3,4,5,6,7,8]).reshape(-1,1)
sinav_notu = np.array([45,50,55,65,70,75,85,90])

# Model oluşturma
model = LinearRegression()
model.fit(calisma_saati, sinav_notu)

# Tahmin
tahmin = model.predict(calisma_saati)

# Katsayılar
print("Sabit (intercept):", model.intercept_)
print("Katsayı:", model.coef_[0])

# R^2 değeri
r2 = r2_score(sinav_notu, tahmin)
print("R^2:", r2)

# Grafik
plt.scatter(calisma_saati, sinav_notu)
plt.plot(calisma_saati, tahmin)
plt.xlabel("Çalışma Saati")
plt.ylabel("Sınav Notu")
plt.title("Basit Doğrusal Regresyon")
plt.show()

# Yeni veri tahmini
yeni_saat = np.array([[6]])
yeni_tahmin = model.predict(yeni_saat)
print("6 saat çalışan bir öğrencinin tahmini notu:", yeni_tahmin[0])