import numpy as np
import scipy.stats as stats

def anova_testi(*gruplar, alpha=0.05):
    """
    İkiden fazla bağımsız grup için:
    - Levene testi (varyans homojenliği)
    - One-Way ANOVA (F testi)
    """
    
    gruplar = [np.array(g) for g in gruplar]
    k = len(gruplar)
    N = sum(len(g) for g in gruplar)
    
    print("----- LEVENE TESTİ -----")
    lev_stat, lev_p = stats.levene(*gruplar, center='median')
    print("Levene istatistiği:", lev_stat)
    print("Levene p-değeri:", lev_p)
    
    if lev_p > alpha:
        print("Varyanslar homojen.\n")
        equal_var = True
    else:
        print("Varyanslar homojen değil.\n")
        equal_var = False
    
    print("----- ANOVA (F TESTİ) -----")
    
    # Manuel ANOVA Hesabı
    genel_ortalama = np.mean(np.concatenate(gruplar))
    
    # SS_between
    ss_between = sum(len(g) * (np.mean(g) - genel_ortalama)**2 for g in gruplar)
    
    # SS_within
    ss_within = sum(sum((g - np.mean(g))**2) for g in gruplar)
    
    df_between = k - 1
    df_within = N - k
    
    ms_between = ss_between / df_between
    ms_within = ss_within / df_within
    
    F = ms_between / ms_within
    
    p_degeri = 1 - stats.f.cdf(F, df_between, df_within)
    
    print("F istatistiği:", F)
    print("df1 (between):", df_between)
    print("df2 (within):", df_within)
    print("p-değeri:", p_degeri)
    
    if p_degeri > alpha:
        print("Sonuç: H0 reddedilemez (ortalamalar eşit).")
    else:
        print("Sonuç: H0 reddedilir (en az bir grup farklı).")
    
    return {
        "Levene_p": lev_p,
        "F": F,
        "p_value": p_degeri
    }




np.random.seed(42)

grup1 = np.random.normal(50, 5, 30)
grup2 = np.random.normal(55, 5, 30)
grup3 = np.random.normal(60, 5, 30)

anova_testi(grup1, grup2, grup3)