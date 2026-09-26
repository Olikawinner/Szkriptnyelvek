#Írjunk függvényt, mely kap egy egészeket tartalmazó listát és visszaadja a listában lévő elemek szorzatát.

def szorzat(lista):
    eredmeny = 1
    for elem in lista:
        eredmeny = eredmeny * elem
    return eredmeny


def main():
    print(szorzat([2, 3, 4])) # varhato: 24
    print(szorzat([5, 4, 3, 2, 1])) # varhato :5! = 120


if __name__ == "__main__":
    main()