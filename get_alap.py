#!/usr/bin/env python3

import os

PY_TARTALOM = """#!/usr/bin/env python3


def main():
    print('Py3')

##############################################################################

if __name__ == "__main__":
    main()
"""

C_TARTALOM = """#include <stdio.h>

int main(void)
{
    printf("Hello, World!\\n");

    return 0;
}
"""

MENU = """---------------------------
Create an empty source file
---------------------------
1) Python [py]
2) C      [c]
q) quit
> """


def create_file(fajlnev, tartalom):
    if os.path.exists(fajlnev):
        print(f"Hiba: a(z) '{fajlnev}' fájl már létezik, nem írom felül!")
        return
    with open(fajlnev, 'w') as f:
        f.write(tartalom)
    print(f"Létrehozva: {fajlnev}")


def main():
    while True:
        valasz = input(MENU).strip().lower()
        if valasz in ('1', 'py'):
            create_file('alap.py', PY_TARTALOM)
        elif valasz in ('2', 'c'):
            create_file('alap.c', C_TARTALOM)
        elif valasz == 'q':
            break
        else:
            print("Érvénytelen választás, próbáld újra!")


if __name__ == "__main__":
    main()