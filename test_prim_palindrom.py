import pytest

from prim_palindrom import prim_palindrom


@pytest.mark.parametrize("n, expected", [
    (31, 101), (130, 131), (131, 131), (1977, 10301),
])
def test_prim_palindrom(n: int, expected: int) -> None:
    assert prim_palindrom(n) == expected
