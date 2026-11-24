def is_palindrome(s: str) -> bool:
    return s == s[::-1]


def osszeg(hatar: int) -> int:
    """A hatar alatti 10-es es 2-es szamrendszerben is palindrom szamok osszege"""
    return sum(n for n in range(1, hatar)
               if is_palindrome(str(n)) and is_palindrome(f"{n:b}"))


def main() -> None:
    print(osszeg(1_000_000))


if __name__ == "__main__":
    main()
