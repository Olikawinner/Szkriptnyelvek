#!/usr/bin/env python3

def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    """Visszaadja a text azon karaktereit, amelyek szerepelnek a chars-ban."""
    return ''.join(betu for betu in text if betu in chars)


def main():
    """Leteszteli a valid() fuggvenyt."""
    print(valid("Barking!"))
    print(valid("KL754", "0123456789"))
    print(valid("BEAN", "abcdefghijklmnopqrstuvwxyz"))


if __name__ == "__main__":
    main()