#!/usr/bin/env python3

import string

TEXT = """
Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb
"""


def dekodol(szoveg, eltolas=2):
    """Caesar-kód visszafejtése: minden betűt 'eltolas' hellyel előrelépünk az ábécében."""
    kis = string.ascii_lowercase
    nagy = string.ascii_uppercase
    forras = kis + nagy
    cel = kis[eltolas:] + kis[:eltolas] + nagy[eltolas:] + nagy[:eltolas]
    return szoveg.translate(str.maketrans(forras, cel))


def main():
    print(dekodol(TEXT))


if __name__ == "__main__":
    main()