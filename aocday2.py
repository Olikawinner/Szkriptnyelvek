def main():
    osszeg = 0

    with open("day02.txt", "r") as f:
        for sor in f:
            szamok = [int(x) for x in sor.split()]

            kulonbseg = max(szamok) - min(szamok)

            osszeg += kulonbseg

    print(osszeg)


if __name__ == "__main__":
    main()