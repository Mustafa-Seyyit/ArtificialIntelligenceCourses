def bayes(P_B_given_A, P_A, P_B):
    """
    P_B_given_A : P(B|A)
    P_A         : P(A)
    P_B         : P(B)

    dönüş: P(A|B)
    """

    if P_B == 0:
        raise ValueError("P(B)=0 olduğu için Bayes tanımsız.")

    return (P_B_given_A * P_A) / P_B


# ÖRNEK:
# Hastalık testi örneği
P_H = 0.01          # Hastalık oranı
P_Poz_H = 0.99      # Hasta iken test pozitif
P_Poz = 0.05        # Toplam pozitif oranı (örnek değer)

print("P(H|Poz) =", bayes(P_Poz_H, P_H, P_Poz))