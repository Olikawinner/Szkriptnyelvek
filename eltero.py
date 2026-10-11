#!/usr/bin/env python3

import os
import string
import sys


def main():
    """Kiirja az abc kisbetuit; a program neve (argv[0]) donti el az iranyt."""
    program_nev = os.path.basename(sys.argv[0])
    betuk = string.ascii_lowercase

    if program_nev == "z-a.py":
        print(betuk[::-1])
    else:
        print(betuk)


if __name__ == "__main__":
    main()