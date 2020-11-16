"""Introduction to Recursion!"""

def icarus(flaps: int) -> None:
    if flaps > 5:
        print("base case!")
    else:
        print(f"flaps: {flaps}")
        icarus(flaps + 1)
        print(f"coming down {flaps}")


icarus(0)

# base case is where recursion temrinates