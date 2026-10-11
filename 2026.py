#!/usr/bin/env python

import string


def main():
    """Kiirja az evszamot a forraskodban hasznalt szamjegyek nelkul."""
    elso_resz = len("abcdefghijklmnopqrst")
    masodik_resz = len(string.ascii_lowercase)

    print(f"{elso_resz}{masodik_resz}")


if __name__ == "__main__":
    main()