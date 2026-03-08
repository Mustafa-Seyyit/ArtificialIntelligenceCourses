import numpy as np
import scipy.stats as stats

def tek_orneklem_testi(veri, mu0, sigma=None, alpha=0.05):
    """
    Tek örneklem için:
    - sigma verilirse Z testi
    - sigma None ise t testi yapar.
    """
    
    veri = np.array(veri)
    n = len(veri)
    ortalama = np.mean(veri)
    
    print("Örneklem Ortalaması:", ortalama)
    print("Hipotez Ortalaması:", mu0)
    
  
    # Z TESTİ (Varyans biliniyor)
   
    if sigma is not None:
        standart_hata = sigma / np.sqrt(n)
        z = (ortalama - mu0) / standart_hata
        
        p_degeri = 2 * (1 - stats.norm.cdf(abs(z)))
        
        print("\n--- Z Testi Uygulandı ---")
        print("Z istatistiği:", z)
        print("p-değeri:", p_degeri)
        
        if p_degeri > alpha:
            print("Sonuç: H0 reddedilemez.")
        else:
            print("Sonuç: H0 reddedilir.")
        
        return z, p_degeri
    

    # t TESTİ (Varyans bilinmiyor)

    else:
        s = np.std(veri, ddof=1)
        standart_hata = s / np.sqrt(n)
        t = (ortalama - mu0) / standart_hata
        
        df = n - 1
        p_degeri = 2 * (1 - stats.t.cdf(abs(t), df))
        
        print("\n--- t Testi Uygulandı ---")
        print("t istatistiği:", t)
        print("Serbestlik derecesi:", df)
        print("p-değeri:", p_degeri)
        
        if p_degeri > alpha:
            print("Sonuç: H0 reddedilemez.")
        else:
            print("Sonuç: H0 reddedilir.")
        
        return t, p_degeri
    
np.random.seed(42)
veri = np.random.normal(100, 15, 50)

tek_orneklem_testi(veri, mu0=105, sigma=15)

print("------------------------------------------------------")

tek_orneklem_testi(veri, mu0=105)