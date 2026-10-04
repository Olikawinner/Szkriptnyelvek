def xor(a, b):
    return bool(a) != bool(b)


def main():
    str1 = "python"
    str2 = None

    str3 = "kutya"
    str4 = "cica"
    
    print(xor(str1, str2))
    print(xor(str3, str4))


if __name__ == "__main__":
    main()