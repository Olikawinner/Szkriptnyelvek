def osszeg_3_vagy_5_tobbszorosei(hatar):
    """
    kiszamolja azon szamok osszeget melyek kisebbek
    a megadott hatarnal es 3-al vagy 5-el maradek nelkul oszthato.

    parameter: egy int ameddig a 3 es 5-el oszthato szamokat osszeadja

    Visszateresi ertek:
        az az int ami a szamok osszege lesz
    """
    return sum(n for n in range(hatar) if n % 3 == 0 or n % 5 == 0)