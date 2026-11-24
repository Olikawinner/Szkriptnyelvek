def oldalak(megadas: str) -> list[int]:
    """'1-4,7,9,11-15' formatumu megadasbol a nyomtatando oldalak listaja"""
    result: list[int] = []
    for resz in megadas.split(","):
        eleje, _, vege = resz.strip().partition("-")
        result.extend(range(int(eleje), int(vege or eleje) + 1))
    return result


def main() -> None:
    print(oldalak(input("Oldalak (pl. 1-4,7,9,11-15): ")))


if __name__ == "__main__":
    main()
