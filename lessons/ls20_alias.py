#An alias allows you to use a contextually menaingful name for a broader type
# EX:
Percent = float
# cointoss_odds: Percent = 0.5

def main() -> None:
    print(ratio(1,2))

def ratio(numer: int, denom: int) -> Percent:
    """Calculate a simple percentage."""
    return numer / denom







if __name__ == "__main__":
    main()