import numpy as np
import scipy.stats as stats

def paired_t_test(grup1, grup2, alpha=0.05, alternative="two-sided"):
    """
    Bağımlı iki grup için paired sample t-test.
    
    alternative:
        "two-sided"
        "greater"  -> grup1 > grup2
        "less"     -> grup1 < grup2
    """
    
    x1 = np.array(grup1)
    x2 = np.array(grup2)
    
    if len(x1) != len(x2):
        raise ValueError("Bağımlı test için iki grubun gözlem sayıları eşit olmalıdır.")
    
    # Farklar
    fark = x1 - x2
    
    n = len(fark)
    ort_fark = np.mean(fark)
    sd_fark = np.std(fark, ddof=1)
    
    standart_hata = sd_fark / np.sqrt(n)
    
    t_istatistik = ort_fark / standart_hata
    df = n - 1
    
    # p-değeri hesaplama
    if alternative == "two-sided":
        p_degeri = 2 * (1 - stats.t.cdf(abs(t_istatistik), df))
    elif alternative == "greater":
        p_degeri = 1 - stats.t.cdf(t_istatistik, df)
    elif alternative == "less":
        p_degeri = stats.t.cdf(t_istatistik, df)
    else:
        raise ValueError("alternative geçersiz.")
    
    print("Paired Sample t-Test Sonuçları")
    print("-------------------------------")
    print("Ortalama fark:", ort_fark)
    print("t istatistiği:", t_istatistik)
    print("Serbestlik derecesi:", df)
    print("p-değeri:", p_degeri)
    
    if p_degeri > alpha:
        print("Sonuç: H0 reddedilemez (anlamlı fark yok).")
    else:
        print("Sonuç: H0 reddedilir (anlamlı fark var).")
    
    return t_istatistik, p_degeri


np.random.seed(42)

# Ön test
oncesi = np.random.normal(50, 5, 30)

# Son test 
sonrasi = oncesi + np.random.normal(2, 2, 30)

paired_t_test(oncesi, sonrasi)