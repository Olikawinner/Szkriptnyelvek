import sys


def main():
    if len(sys.argv) != 3:
        print("Hiba: két egész számot kell megadni parancssori argumentumként!")
        print("Használat: python3 ketszamosszeg.py <szám1> <szám2>")
        return
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    except ValueError:
        print("Hiba: mindkét argumentumnak egész számnak kell lennie!")
        return
    print(a + b)


if __name__ == '__main__':
    main()