def main() -> None:
    print(g(10))
    

def g(x: int) -> int:
    if x > 0:
        x *= -1
    elif x < 0:
        x *= -1
    return x

if __name__ == "__main__":
    main()