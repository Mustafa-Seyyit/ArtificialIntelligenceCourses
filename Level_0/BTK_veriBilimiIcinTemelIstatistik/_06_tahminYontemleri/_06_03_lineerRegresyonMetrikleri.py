import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Örnek veri
X = np.array([1,2,3,4,5,6,7,8]).reshape(-1,1)
y = np.array([45,50,55,65,70,75,85,90])

# Model oluşturma
model = LinearRegression()
model.fit(X, y)

# Tahmin
y_tahmin = model.predict(X)

# Metrikler
mae = mean_absolute_error(y, y_tahmin)
mse = mean_squared_error(y, y_tahmin)
rmse = np.sqrt(mse)
r2 = r2_score(y, y_tahmin)

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2:", r2)