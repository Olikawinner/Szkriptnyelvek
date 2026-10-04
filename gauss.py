def sum(n):
    osszeg = 0
    i = 0
    while i <= n:
        osszeg += i
        i += 1
    return osszeg

def szamjegyek_ossz():
    ossz = 0
    for n in range(1, 101):
        for jegy in list(str(n)):
            ossz += int(jegy)
    return ossz

def main():
    #print("Gauss: ")
    print("A számok összege egytől százig: ", sum(100))
    #print("Variáció: ")
    print("A számjegyek összege: ", szamjegyek_ossz())

if __name__ == "__main__":
    main()

#Python shellben sum(range(1, 101)) kidobja az 5050 eredményt egyből 