def negyzet(n):
    osszeg = 0
    i = 0
    while i <= n:
        osszeg += i*i
        i += 1
    return osszeg

def sum(n):
    osszeg = 0
    i = 0
    while i <= n:
        osszeg += i
        i += 1
    return osszeg

def main():
    print("Első tíz négyzetszám: ", negyzet(10)) #385
    print("Első ötvenöt: ", negyzet(55)) #56980
    print("Első száz: ", negyzet(100)) #338350
    print("Az első száz természetes szám összegének a négyzete és az első száz természetes szám négyzetösszege közti különbség: ", (sum(100)*sum(100)-negyzet(100)))

if __name__ == "__main__":
    main()