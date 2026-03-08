import numpy as np
from sklearn.linear_model import LinearRegression

# TEK DEĞİŞKENLİ REGRESYON

# Bağımsız değişken (çalışma saati)
X1 = np.array([1,2,3,4,5,6,7,8]).reshape(-1,1)

# Bağımlı değişken (sınav notu)
y1 = np.array([45,50,55,65,70,75,85,90])

model1 = LinearRegression()
model1.fit(X1, y1)

print("TEK DEĞİŞKENLİ REGRESYON")
print("Sabit:", model1.intercept_)
print("Katsayı:", model1.coef_[0])

# tahmin
tahmin1 = model1.predict([[6]])
print("6 saat çalışma için tahmin edilen not:", tahmin1[0])


# ÇOK DEĞİŞKENLİ REGRESYON

# Bağımsız değişkenler
# [çalışma saati, devamsızlık yüzdesi]
X2 = np.array([
    [1,60],
    [2,65],
    [3,70],
    [4,75],
    [5,80],
    [6,85],
    [7,90],
    [8,95]
])

# Bağımlı değişken
y2 = np.array([45,50,55,65,70,75,85,90])

model2 = LinearRegression()
model2.fit(X2, y2)

print("\nÇOK DEĞİŞKENLİ REGRESYON")
print("Sabit:", model2.intercept_)
print("Katsayılar:", model2.coef_)

# tahmin
tahmin2 = model2.predict([[6,85]])
print("6 saat çalışma ve %85 devam için tahmini not:", tahmin2[0])