def is_prime(n: int) -> bool:
    if n < 2:
        return False
    return all(n % i for i in range(2, int(n ** 0.5) + 1))


def is_palindrome(n: int) -> bool:
    s = str(n)
    return s == s[::-1]


def prim_palindrom(n: int) -> int:
    """A legkisebb M >= n szam, ami prim es palindrom"""
    while not (is_palindrome(n) and is_prime(n)):
        n += 1
    return n
