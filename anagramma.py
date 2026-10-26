#!/usr/bin/env python3


def main():
    def normalize(szoveg):
        return "".join(szoveg.lower().split())

    def anagramma_rendezessel(elso, masodik):
        return sorted(normalize(elso)) == sorted(normalize(masodik))

    def betugyakorisag(szoveg):
        gyakorisag = {}
        for betu in normalize(szoveg):
            gyakorisag[betu] = gyakorisag.get(betu, 0) + 1
        return gyakorisag

    def anagramma_szotarral(elso, masodik):
        return betugyakorisag(elso) == betugyakorisag(masodik)

    peldak = [
        ("listen", "silent"),
        ("A gentleman", "Elegant man"),
        ("Clint Eastwood", "Old west action"),
        ("dormitory", "dirty room"),
        ("étel", "élet"),
        ("papi", "pipa"),
        ("kolostor", "rostokol"),
        ("aab", "abb"),
    ]

    for elso, masodik in peldak:
        print(elso, "/", masodik)
        print("  Rendezéssel:", anagramma_rendezessel(elso, masodik))
        print("  Szótárral:  ", anagramma_szotarral(elso, masodik))


if __name__ == "__main__":
    main()
