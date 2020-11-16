import turtle as t
from random import random
LEFT = 1.0
RIGHT = -1.0
TRUNK = 100.0
UP = 90.0

def tree(x: float, y: float) -> None:
    t.color("green")
    t.penup()
    t.goto(x, y)
    t.pendown()
    branch(TRUNK, 90.0)
    t.update()

def branch(length: float, angle: float) -> None:
    t.setheading(angle)
    t.forward(length)
    if length < 1:
        ... # base case
    else:
        branch(length * 0.7, angle + 30)
        branch(length * 0.6, angle - 75)
    t.setheading(angle + 180)
    t.forward(length)

if __name__ == "__main__":
    t.speed()
    t.tracer(0,0)
    t.getscreen().onclick(tree)
    tree(0, 0)
    t.done()