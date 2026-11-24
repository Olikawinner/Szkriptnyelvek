from nyomtatando_oldalak import oldalak


def test_pelda() -> None:
    assert oldalak("1-4,7,9,11-15") == [1, 2, 3, 4, 7, 9, 11, 12, 13, 14, 15]


def test_egy_oldal() -> None:
    assert oldalak("5") == [5]


def test_szokozok() -> None:
    assert oldalak("1-2, 4") == [1, 2, 4]
