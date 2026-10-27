"""Règles de calcul de FactureCloud : tout en entiers (FCFA), jamais de flottants."""

TAUX_TVA_BP = 1925  # 19,25 % en points de base (paramétrable)


def tva(montant_ht):
    """TVA arrondie au franc le plus proche (0,5 arrondi vers le haut)."""
    if montant_ht < 0:
        raise ValueError("MONTANT_INVALIDE")
    return (montant_ht * TAUX_TVA_BP + 5000) // 10000