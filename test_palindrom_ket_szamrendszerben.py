from palindrom_ket_szamrendszerben import osszeg


def test_osszeg() -> None:
    assert osszeg(1_000_000) == 872187
