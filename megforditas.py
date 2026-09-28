def fordit_aritmetikai(n):
    uj = 0
    while n > 0:
        uj = uj * 10 + n % 10
        n = n // 10
    return uj


def fordit_sztringes(n):
    return int(str(n)[::-1])


def main():
    print(fordit_aritmetikai(1977))   # 7791
    print(fordit_aritmetikai(12568))  # 86521
    print(fordit_sztringes(1977))     # 7791
    print(fordit_sztringes(12568))    # 86521


if __name__ == '__main__':
    main()