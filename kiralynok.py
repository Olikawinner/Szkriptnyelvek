#!/usr/bin/env python3


def main():
    def sakktabla(allas):
        print("+-----------------+")

        for sor in range(7, -1, -1):
            print("|", end=" ")
            for oszlop in range(8):
                if allas[oszlop] == sor:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print("|")

        print("+-----------------+")

    sakktabla([7, 3, 0, 2, 5, 1, 6, 4])
    print()
    sakktabla([0, 4, 7, 5, 2, 6, 1, 3])


if __name__ == "__main__":
    main()
