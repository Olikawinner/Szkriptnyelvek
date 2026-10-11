#!/usr/bin/env python3

# Segedtabla: minden szamjegyhez (0-9) elore kiszamoljuk a "sajat magara"
# emelt hatvanyat, hogy ne kelljen ujra es ujra pow()-ot hivni.
# A feladat kerese szerint 0^0 = 0.
HATVANY = [0] + [d ** d for d in range(1, 10)]


def digitosszeg_hatvany(n):
    """A szam szamjegyeinek sajat-magukra-emelt hatvanyainak osszeget adja vissza (0^0=0 szabaly szerint)."""
    osszeg = 0
    while n > 0:
        n, jegy = divmod(n, 10)
        osszeg += HATVANY[jegy]
    return osszeg


def is_munchausen(n):
    """Eldonti, hogy n Munchausen-szam-e."""
    if n == 0:
        return True  # 0^0 = 0, tehat 0 is Munchausen-szam
    return digitosszeg_hatvany(n) == n


def munchausen_szamok(hatar):
    """Megkeresi a hatarnal (kizarolag) kisebb osszes Munchausen-szamot, 0-tol indulva."""
    return [n for n in range(hatar) if is_munchausen(n)]


def main():
    """Lefuttatja a ket reszfeladatot: 10 000 alatt (debug), majd az osszeset 440 millio alatt."""
    print("1. feladat (10 000 alatt):")
    print(munchausen_szamok(10_000))

    print()
    print("2. feladat (440 millio alatt):")
    print(munchausen_szamok(440_000_000))


if __name__ == "__main__":
    main()