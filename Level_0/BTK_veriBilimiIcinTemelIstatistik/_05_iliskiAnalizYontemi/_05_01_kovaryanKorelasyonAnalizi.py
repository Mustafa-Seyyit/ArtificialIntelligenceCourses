"""
KOVARYANS VE KORELASYON ANALİZİ
---------------------------------------------------
Bu script şu konuları gösterir:
1. Kovaryans hesaplama
2. Kovaryans matrisi oluşturma
3. Pearson korelasyon analizi
4. Spearman korelasyon analizi
5. Kendall korelasyon analizi
6. p-değeri ile anlamlılık kontrolü
7. Grafiksel gösterimler

Gereken kütüphaneler:
pip install numpy pandas matplotlib scipy
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, spearmanr, kendalltau


# 1) ÖRNEK VERİ SETİ
# Anlamlı ilişkiler içeren örnek veri oluşturuyoruz
np.random.seed(42)

n = 100

calisma_saati = np.random.randint(1, 10, size=n)
uyku_saati = np.random.randint(4, 10, size=n)
deneme_sinavi = np.random.normal(65, 10, size=n)

# Not değişkenini diğerlerinden etkilenmiş olacak şekilde üretelim
sinav_notu = (
    40
    + calisma_saati * 5
    + uyku_saati * 2
    + deneme_sinavi * 0.3
    + np.random.normal(0, 5, size=n)
)

df = pd.DataFrame({
    "CalismaSaati": calisma_saati,
    "UykuSaati": uyku_saati,
    "DenemeSinaviPuani": deneme_sinavi,
    "SinavNotu": sinav_notu
})

print("\nİlk 5 gözlem:")
print(df.head())


# 2) KOVARYANS HESABI (MANUEL)
def manual_covariance(x, y):
    """
    İki değişken arasındaki örnek kovaryansını manuel hesaplar.
    """
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)

    if len(x) != len(y):
        raise ValueError("x ve y aynı uzunlukta olmalıdır.")

    x_mean = np.mean(x)
    y_mean = np.mean(y)

    cov = np.sum((x - x_mean) * (y - y_mean)) / (len(x) - 1)
    return cov


cov_xy = manual_covariance(df["CalismaSaati"], df["SinavNotu"])
print("\n[MANUEL] CalismaSaati ile SinavNotu kovaryansı:", round(cov_xy, 4))


# 3) PANDAS İLE KOVARYANS MATRİSİ
cov_matrix = df.cov()

print("\nKovaryans Matrisi:")
print(cov_matrix)


# 4) KORELASYON HESAPLARI


# Pearson: doğrusal ilişki
pearson_corr_matrix = df.corr(method="pearson")

# Spearman: sıralama ilişkisi / monoton ilişki
spearman_corr_matrix = df.corr(method="spearman")

# Kendall: sıralama temelli başka bir korelasyon yaklaşımı
kendall_corr_matrix = df.corr(method="kendall")

print("\nPearson Korelasyon Matrisi:")
print(pearson_corr_matrix)

print("\nSpearman Korelasyon Matrisi:")
print(spearman_corr_matrix)

print("\nKendall Korelasyon Matrisi:")
print(kendall_corr_matrix)



# 5) İKİ DEĞİŞKEN ARASI DETAYLI KORELASYON ANALİZİ

x = df["CalismaSaati"]
y = df["SinavNotu"]

pearson_r, pearson_p = pearsonr(x, y)
spearman_r, spearman_p = spearmanr(x, y)
kendall_r, kendall_p = kendalltau(x, y)

print("\nDetaylı Korelasyon Analizi: CalismaSaati vs SinavNotu")
print("-" * 55)
print(f"Pearson korelasyon katsayısı : {pearson_r:.4f}")
print(f"Pearson p-değeri             : {pearson_p:.6f}")

print(f"Spearman korelasyon katsayısı: {spearman_r:.4f}")
print(f"Spearman p-değeri            : {spearman_p:.6f}")

print(f"Kendall korelasyon katsayısı : {kendall_r:.4f}")
print(f"Kendall p-değeri             : {kendall_p:.6f}")



# 6) YORUM FONKSİYONU

def interpret_correlation(r):
    """
    Korelasyon katsayısını sözel olarak yorumlar.
    """
    abs_r = abs(r)

    if abs_r < 0.20:
        return "Çok zayıf ilişki"
    elif abs_r < 0.40:
        return "Zayıf ilişki"
    elif abs_r < 0.60:
        return "Orta düzey ilişki"
    elif abs_r < 0.80:
        return "Güçlü ilişki"
    else:
        return "Çok güçlü ilişki"


def significance_comment(p, alpha=0.05):
    """
    p-değerine göre anlamlılık yorumu yapar.
    """
    if p < alpha:
        return f"İlişki istatistiksel olarak anlamlıdır (p < {alpha})."
    return f"İlişki istatistiksel olarak anlamlı değildir (p >= {alpha})."


print("\nYorumlar:")
print("Pearson yorumu :", interpret_correlation(pearson_r))
print("Anlamlılık     :", significance_comment(pearson_p))



# 7) GRAFİKLER

# 7.1 Scatter Plot
plt.figure(figsize=(8, 5))
plt.scatter(df["CalismaSaati"], df["SinavNotu"], alpha=0.7)
plt.title("Çalışma Saati ile Sınav Notu Arasındaki İlişki")
plt.xlabel("Çalışma Saati")
plt.ylabel("Sınav Notu")
plt.grid(True)
plt.tight_layout()
plt.show()


# 7.2 Korelasyon Isı Haritası (matplotlib ile)
corr_matrix = df.corr(method="pearson")

plt.figure(figsize=(8, 6))
im = plt.imshow(corr_matrix, interpolation="nearest", aspect="auto")
plt.colorbar(im)

plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns, rotation=45)
plt.yticks(range(len(corr_matrix.index)), corr_matrix.index)

plt.title("Pearson Korelasyon Isı Haritası")

# Hücrelerin içine korelasyon değerlerini yaz
for i in range(len(corr_matrix.index)):
    for j in range(len(corr_matrix.columns)):
        plt.text(j, i, f"{corr_matrix.iloc[i, j]:.2f}",
                 ha="center", va="center")

plt.tight_layout()
plt.show()



# 8) SONUÇ RAPORU
print("\nSONUÇ RAPORU")
print("-" * 55)
print(f"Çalışma saati ile sınav notu arasındaki kovaryans: {cov_xy:.4f}")
print(f"Pearson korelasyon katsayısı: {pearson_r:.4f}")
print(f"Spearman korelasyon katsayısı: {spearman_r:.4f}")
print(f"Kendall korelasyon katsayısı: {kendall_r:.4f}")
print(interpret_correlation(pearson_r))
print(significance_comment(pearson_p))