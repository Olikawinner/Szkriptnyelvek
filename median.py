#!/usr/bin/env python3


def main():
    def test(szamok):
        if not szamok:
            raise ValueError("Üres listának nincs mediánja.")

        rendezett = sorted(szamok)
        n = len(rendezett)
        kozep = n // 2

        if n % 2 == 1:
            return rendezett[kozep]

        return (rendezett[kozep - 1] + rendezett[kozep]) / 2

    print(test([1, 2, 3, 4, 5]))
    print(test([3, 1, 2, 5, 3]))
    print(test([1, 300, 2, 200, 1]))
    print(test([3, 6, 20, 99, 10, 15]))


if __name__ == "__main__":
    main()
