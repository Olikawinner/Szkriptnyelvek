#!/usr/bin/env python3

def inverse_captcha(sorozat):
    """
    Osszeadja a szamsorozat azon szamjegyeit, amelyek megegyeznek a
    rakovetkezo szamjeggyel. A sorozat cirkularis, vagyis az utolso
    szamjegy rakovetkezoje az elso szamjegy.

    Parameter:
        sorozat (str): szamjegyekbol allo sztring

    Visszateresi ertek:
        int: a feltetelnek megfelelo szamjegyek osszege
    """
    kovetkezok = sorozat[1:] + sorozat[0]
    return sum(int(jegy) for jegy, kov in zip(sorozat, kovetkezok) if jegy == kov)


def main():
    """Leteszteli a fuggvenyt a pelda-bemenetekkel, majd megoldja a tenyleges feladatot."""
    print(inverse_captcha("1122"))
    print(inverse_captcha("1111"))
    print(inverse_captcha("1234"))
    print(inverse_captcha("91212129"))

    with open("day01_input.txt") as f:
        sorozat = f.read().strip()
    print("A feladat eredmenye:", inverse_captcha(sorozat))


if __name__ == "__main__":
    main()