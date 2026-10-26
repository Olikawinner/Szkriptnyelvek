#!/usr/bin/env python3

from pathlib import Path


def main():
    """Megszámolja az ismétlődő szavakat nem tartalmazó jelmondatokat."""
    ervenyesek = 0
    bemenet = Path(__file__).with_name("aoc_bemenet.txt")

    with bemenet.open(encoding="utf-8-sig") as fajl:
        for sor in fajl:
            szavak = sor.split()

            if len(szavak) == len(set(szavak)):
                ervenyesek += 1

    print(ervenyesek)


if __name__ == "__main__":
    main()
