"""An example of a constructor definition."""

class Point:
    """A 2D Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """An example of a constructor function/method."""
        self.x = x
        self.y = y

def main() -> None:
    """The entry point."""
    p = Point(110.0,211.0)
    print(p.x)
    print(p.y)   
    

if __name__ == "__main__":
    main()
    