import pytest
from service_calcul.calcul import tva


def test_tva_arrondie_au_franc_le_plus_proche():
    assert tva(100000) == 19250
    assert tva(1) == 0
    assert tva(200) == 39  # 38,5 arrondi vers le haut


def test_tva_sur_20000():
    assert tva(20000) == 3850


def test_tva_sur_zero():
    assert tva(0) == 0


def test_tva_negative_leve_erreur():
    with pytest.raises(ValueError):
        tva(-1)