"""Grocery Price Calculator!"""

print("What groceries would you like to buy today?")
number_eggs: str = input("Eggs are on special for $2.10, enter quantity of eggs you would like: ")
eggs_quantity: float = (number_eggs)
eggs_price: float = (2.10)
total_eggs_price: float = (float(eggs_quantity) * float(eggs_price))
print("Your total is " + str(total_eggs_price) + " dollars")
Yes_no: str = input ("would you like anything else?")
no = quit()