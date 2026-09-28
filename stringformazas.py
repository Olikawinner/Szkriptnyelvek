def main():
    nev = "Kenyér"
    ar = 1249.5
    db = 3

    print(f"{nev:<10}{db:>3} db{ar:>10.2f} Ft")

    print(f"Összesen: {db * ar * 1000:,.2f} Ft")

    print(f"ÁFA: {0.27:.0%}")


if __name__ == "__main__":
    main()