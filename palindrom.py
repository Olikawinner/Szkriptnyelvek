#1. Triviális módszer

def palindrom_trivialis(s):
    return s == s[::-1]

#2. Iteratív módszer

def palindrom_iterativ(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

#3. Rekurzív

def palindrom_rekurziv(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrom_rekurziv(s[1:-1])

def main():
    print(palindrom_trivialis("kutyus"))
    print(palindrom_iterativ("maoam"))
    print(palindrom_rekurziv("cica"))

if __name__ == "__main__":
    main()