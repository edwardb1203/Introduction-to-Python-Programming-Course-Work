"""A demonstration of classes/objects."""

class Pizza:
    """A simple model of a Pizza."""
    size: str = "medium"
    extra_cheese: bool = False
    toppings: int = 0


def price(one_pizza: Pizza) -> float:
    """Takes a pizza and gives price."""
    total_price: float = 0
    if Pizza.size == "small":
        base_price: float = 7.0
    if Pizza.size == "medium":
        base_price: float = 9.0
    if Pizza.size == "large":
        base_price: float = 11.0
    total_price += base_price
    if one_pizza.extra_cheese:
        total_price += 1.0
    total_price += one_pizza.toppings * .75
    return total_price

def main() -> None:
    """Entrypoint of program."""
    a_pizza: Pizza = Pizza()
    a_pizza.size = "Large"
    a_pizza.toppings = 3
    a_pizza.extra_cheese = True
    print("Size: " + a_pizza.size)
    print("Toppings: " + str(a_pizza.toppings))
    print("Your price is: " + str(price(a_pizza)))
    ...

if __name__ == "__main__":
    main()