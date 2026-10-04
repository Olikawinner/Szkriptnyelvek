from enum import Enum


class Hangrend(Enum):
    MELY = 1
    MAGAS = 2
    VEGYES = 3
    SEMMILYEN = 4


MELY_MGHK = 'aáoóuú'
MAGAS_MGHK = 'eéiíöőüű'


def hangrend(szo):
    van_mely = False
    van_magas = False
    for betu in szo.lower():
        if betu in MELY_MGHK:
            van_mely = True
        elif betu in MAGAS_MGHK:
            van_magas = True

    if van_mely and van_magas:
        return Hangrend.VEGYES
    elif van_mely:
        return Hangrend.MELY
    elif van_magas:
        return Hangrend.MAGAS
    else:
        return Hangrend.SEMMILYEN


def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "Pfffffff"]
    for szo in words:
        print(f"{szo:12} -> {hangrend(szo)}")


if __name__ == "__main__":
    main()