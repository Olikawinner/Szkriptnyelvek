class Verem:
    def __init__(self):
        self.adatok = []

    def betesz(self, x):
        self.adatok.append(x)

    def kivesz(self):
        if self.ures():
            return None

        return self.adatok.pop()

    def ures(self):
        return len(self.adatok) == 0

    def meret(self):
        return len(self.adatok)

    def __str__(self):
        return "[" + " ".join(str(x) for x in self.adatok)


class Sor:
    def __init__(self):
        self.adatok = []

    def betesz(self, x):
        self.adatok.append(x)

    def kivesz(self):
        if self.ures():
            return None

        return self.adatok.pop(0)

    def ures(self):
        return len(self.adatok) == 0

    def meret(self):
        return len(self.adatok)


def main():
    # Verem tesztelése
    v = Verem()

    print(v)
    print(v.ures())

    v.betesz(1)
    v.betesz(4)
    v.betesz(5)

    print(v)
    print(v.meret())
    print(v.ures())

    x = v.kivesz()
    print(x)
    print(v)

    v.kivesz()
    v.kivesz()

    print(v.kivesz())  # None

    # Sor tesztelése
    s = Sor()

    s.betesz(1)
    s.betesz(4)
    s.betesz(5)

    print(s.meret())  # 3
    print(s.ures())   # False

    print(s.kivesz()) # 1
    print(s.kivesz()) # 4

    print(s.meret())  # 1

    print(s.kivesz()) # 5
    print(s.kivesz()) # None


if __name__ == "__main__":
    main()