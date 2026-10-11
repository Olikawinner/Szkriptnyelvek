def main():
    """ lefutattja es kiirja a 15 feladat megoldasat"""
    # 1. feladat
    jarmuvek = ['auto', 'villamos', 'metro']
    print([szo.upper() + '!' for szo in jarmuvek])

    # 2. feladat
    nevek = ['aladar', 'bela', 'cecil']
    print([nev.capitalize() for nev in nevek])

    # 3. feladat
    print([0 for _ in range(10)])

    # 4. feladat
    szamok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print([n * 2 for n in szamok])

    # 5. feladat
    sztring_szamok = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    print([int(s) for s in sztring_szamok])

    # 6. feladat
    szam_sztring = "1234567"
    print([int(jegy) for jegy in szam_sztring])

    # 7. feladat
    mondat = 'The quick brown fox jumps over the lazy dog'
    print([len(szo) for szo in mondat.split()])

    # 8. feladat
    mondat2 = "python is an awesome language"
    print([szo[0] for szo in mondat2.split()])

    # 9. feladat
    print([(szo, len(szo)) for szo in mondat.split()])

    # 10. feladat
    print([n for n in range(10) if n % 2 == 0])

    # 11. feladat
    print([n * n for n in range(20) if (n * n) % 2 == 0])

    # 12. feladat
    print([n * n for n in range(20) if str(n * n)[-1] == '4'])

    # 13. feladat
    betuk = [chr(k) for k in range(ord('A'), ord('Z') + 1)]
    print(''.join(betuk))

    # 14. feladat
    gyumolcsok = [' apple ', ' banana ', ' kiwi']
    print([gy.strip() for gy in gyumolcsok])

    # 15. feladat
    bitek = [1, 0, 1, 1, 0, 1, 0, 0]
    print(''.join([str(b) for b in bitek]))


if __name__ == "__main__":
    main()