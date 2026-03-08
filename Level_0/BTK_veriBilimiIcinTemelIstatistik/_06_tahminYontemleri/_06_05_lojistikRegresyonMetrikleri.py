import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# Örnek veri
X = np.array([1,2,3,4,5,6,7,8]).reshape(-1,1)

# 0 = kaldı, 1 = geçti
y = np.array([0,0,0,0,1,1,1,1])

# Model oluşturma
model = LogisticRegression()
model.fit(X, y)

# Tahmin
y_tahmin = model.predict(X)

# Metrikler
accuracy = accuracy_score(y, y_tahmin)
precision = precision_score(y, y_tahmin)
recall = recall_score(y, y_tahmin)
f1 = f1_score(y, y_tahmin)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)

# Confusion Matrix
cm = confusion_matrix(y, y_tahmin)
print("Confusion Matrix:")
print(cm)