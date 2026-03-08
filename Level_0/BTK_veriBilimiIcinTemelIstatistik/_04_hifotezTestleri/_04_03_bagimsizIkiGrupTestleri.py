import numpy as np
from scipy import stats

def iki_grup_karsilastir(
    grup1,
    grup2,
    mu_fark0: float = 0.0,
    sigma1: float | None = None,
    sigma2: float | None = None,
    alpha: float = 0.05,
    alternative: str = "two-sided",   # "two-sided", "greater", "less"
    levene_center: str = "median"     # "mean" (Levene), "median" (Brown-Forsythe, daha sağlam), "trimmed"
):
    """
    Bağımsız iki grup için otomatik test seçimi:
      - Levene ile varyans eşitliği kontrolü
      - sigma1 ve sigma2 (anakütle std) ikisi de verilirse: Z testi
      - Aksi halde: t testi (Levene'e göre pooled veya Welch)

    H0: (mu1 - mu2) = mu_fark0
    """

    x1 = np.asarray(grup1, dtype=float)
    x2 = np.asarray(grup2, dtype=float)

    if x1.size < 2 or x2.size < 2:
        raise ValueError("Her iki grupta da en az 2 gözlem olmalı.")

    if alternative not in {"two-sided", "greater", "less"}:
        raise ValueError("alternative 'two-sided', 'greater' veya 'less' olmalı.")

    # --- Özet istatistikler ---
    n1, n2 = x1.size, x2.size
    mean1, mean2 = float(np.mean(x1)), float(np.mean(x2))
    s1 = float(np.std(x1, ddof=1))
    s2 = float(np.std(x2, ddof=1))

    # --- Levene testi (varyans homojenliği) ---
    lev_stat, lev_p = stats.levene(x1, x2, center=levene_center)
    varyans_esit = lev_p > alpha  # H0: varyanslar eşit

    # Yardımcı: p-değeri hesaplama (tek/çift kuyruk)
    def p_value_from_stat(stat_value: float, dist: str, df: float | None = None) -> float:
        if dist == "z":
            cdf = stats.norm.cdf(stat_value)
        elif dist == "t":
            if df is None:
                raise ValueError("t dağılımı için df gerekli.")
            cdf = stats.t.cdf(stat_value, df)
        else:
            raise ValueError("dist 'z' veya 't' olmalı.")

        if alternative == "two-sided":
            # iki kuyruk: |stat| kadar uç olma olasılığı
            if dist == "z":
                return 2 * (1 - stats.norm.cdf(abs(stat_value)))
            return 2 * (1 - stats.t.cdf(abs(stat_value), df))
        elif alternative == "greater":
            # H1: mu1 - mu2 > mu_fark0
            return 1 - cdf
        else:  # "less"
            # H1: mu1 - mu2 < mu_fark0
            return cdf

    # --- Test seçimi ---
    sonuc = {
        "n1": n1, "n2": n2,
        "mean1": mean1, "mean2": mean2,
        "s1_sample": s1, "s2_sample": s2,
        "levene_stat": float(lev_stat),
        "levene_p": float(lev_p),
        "varyans_esit_mi_(Levene)": bool(varyans_esit),
        "alpha": alpha,
        "alternative": alternative,
        "H0": f"(mu1 - mu2) = {mu_fark0}"
    }

    # --- 1) Z testi (ikisinin de sigma'sı biliniyorsa) ---
    if sigma1 is not None and sigma2 is not None:
        if sigma1 <= 0 or sigma2 <= 0:
            raise ValueError("sigma1 ve sigma2 pozitif olmalı (standart sapma).")

        se = np.sqrt((sigma1**2) / n1 + (sigma2**2) / n2)
        z = ((mean1 - mean2) - mu_fark0) / se
        p = p_value_from_stat(z, dist="z")

        sonuc.update({
            "test": "Z testi (iki örneklem, sigma biliniyor)",
            "stat": float(z),
            "df": None,
            "std_error": float(se),
            "p_value": float(p),
            "karar": "H0 reddedilir" if p <= alpha else "H0 reddedilemez"
        })
        return sonuc

    # --- 2) t testi (en az bir sigma bilinmiyorsa) ---
    # Levene'e göre: eşit varyans -> pooled, değilse -> Welch
    if varyans_esit:
        # pooled t-test
        df = n1 + n2 - 2
        sp2 = (((n1 - 1) * s1**2) + ((n2 - 1) * s2**2)) / df
        se = np.sqrt(sp2 * (1 / n1 + 1 / n2))
        t_stat = ((mean1 - mean2) - mu_fark0) / se
        p = p_value_from_stat(t_stat, dist="t", df=df)

        sonuc.update({
            "test": "t testi (pooled, equal_var=True) [Levene: eşit varyans]",
            "stat": float(t_stat),
            "df": float(df),
            "std_error": float(se),
            "p_value": float(p),
            "karar": "H0 reddedilir" if p <= alpha else "H0 reddedilemez"
        })
        return sonuc
    else:
        # Welch t-test
        se2 = (s1**2) / n1 + (s2**2) / n2
        se = np.sqrt(se2)
        t_stat = ((mean1 - mean2) - mu_fark0) / se

        # Welch-Satterthwaite df
        num = se2**2
        den = ((s1**2 / n1)**2) / (n1 - 1) + ((s2**2 / n2)**2) / (n2 - 1)
        df = num / den

        p = p_value_from_stat(t_stat, dist="t", df=df)

        sonuc.update({
            "test": "Welch t testi (equal_var=False) [Levene: eşit değil]",
            "stat": float(t_stat),
            "df": float(df),
            "std_error": float(se),
            "p_value": float(p),
            "karar": "H0 reddedilir" if p <= alpha else "H0 reddedilemez"
        })
        return sonuc


# ------------------ ÖRNEK KULLANIM ------------------
if __name__ == "__main__":
    np.random.seed(0)
    g1 = np.random.normal(50, 5, 30)
    g2 = np.random.normal(52, 8, 35)

    # 1) Sigma bilinmiyor -> t testi (Levene'e göre pooled veya Welch)
    print(iki_grup_karsilastir(g1, g2, mu_fark0=0, alpha=0.05, alternative="two-sided"))

    # 2) Sigma biliniyor -> Z testi
    print(iki_grup_karsilastir(g1, g2, mu_fark0=0, sigma1=5, sigma2=8, alpha=0.05))