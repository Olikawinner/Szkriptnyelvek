def diamond(magassag):
    if magassag % 2 == 0:
        print("Hiba: a magasságnak páratlan számnak kell lennie!")
        return

    for csillagok in range(1, magassag +1, 2):
        sor = "*" * csillagok
        print(sor.center(magassag))

    for csillagok in range(magassag -2, 0, -2):
        sor = "*" * csillagok
        print(sor.center(magassag))


def main():
    diamond(3)
    print()
    diamond(7)


if __name__ == "__main__":
    main()