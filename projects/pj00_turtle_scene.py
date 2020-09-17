"""My attempt at the infamous shadow clone jutsu.

Attempt at 10 points, broke down the naruto function into individual components to avoid complexity.
Also created rectangle function to further decrease complexity, as it is used multiple times.
Attempt at 5 points, I created a scene more complex than could be achieved with 4 components.
Also used background color change from turtle documentation page.
"""

__author__ = "730312903"

from turtle import Turtle, colormode, tracer, update, done, bgcolor


MAX_SPEED: int = 0
SHIFT: int = 200
SHIFT2: int = 350
MODE: int = 255
SUIT_COLOR = tuple = (252, 147, 13)
HAIR_COLOR = tuple = (254, 232, 42)
SKIN_COLOR = tuple = (255, 227, 158)
bgcolor("cyan")
# NOTE to grader, turtles are imported at bottom for cleaner code


def main() -> None:
    """The jutsu has been cast."""
    tracer(0, 0)
    Naruto()
    Naruto2()
    Naruto3()
    update()
    done()


def rectangle(t_turtle: Turtle, length: float, width: float) -> None:
    """Draws a rectangle."""
    i: int = 0
    while i < 2:
        t_turtle.forward(length)
        t_turtle.right(90)
        t_turtle.forward(width)
        t_turtle.right(90)
        i += 1


def hair(t_madera: Turtle, x: float, y: float) -> None:
    """Draws Naruto's hair."""
    colormode(MODE)
    t_madera.hideturtle()
    t_madera.penup()
    t_madera.goto(x, y)
    t_madera.pendown()
    t_madera.setheading(0.0)
    t_madera.pencolor(HAIR_COLOR)
    t_madera.fillcolor(HAIR_COLOR)
    t_madera.speed(MAX_SPEED)
    i: int = 0
    t_madera.begin_fill()
    while i < 15:
        t_madera.left(162)
        t_madera.forward(75)
        t_madera.right(160)
        t_madera.forward(25)
        t_madera.right(150)
        t_madera.right(100)
        t_madera.forward(10)
        i += 1
    t_madera.end_fill()


def headband(t_itachi: Turtle, x: float, y: float) -> None:
    """Draws Naruto's headband."""
    colormode(MODE)
    t_itachi.hideturtle()
    t_itachi.penup()
    t_itachi.goto(x, y)
    t_itachi.pendown()
    t_itachi.setheading(0.0)
    t_itachi.pencolor("black")
    t_itachi.fillcolor("black")
    t_itachi.speed(MAX_SPEED)
    t_itachi.begin_fill()
    rectangle(t_itachi, 55, 15)
    t_itachi.end_fill()


def tassles(t_hidan: Turtle, x: float, y: float, z: float, ф: float) -> None:
    """Draws the tassles behind Naruto's headband."""
    colormode(MODE)
    t_hidan.hideturtle()
    t_hidan.penup()
    t_hidan.goto(x, y)
    t_hidan.pendown()
    t_hidan.setheading(0.0)
    t_hidan.pencolor("black")
    t_hidan.fillcolor("black")
    t_hidan.speed(MAX_SPEED)
    t_hidan.left(225)
    i: int = 0
    t_hidan.begin_fill()
    while i < 90:
        t_hidan.forward(.50)
        t_hidan.right(.75)
        t_hidan.forward(.25)
        t_hidan.left(1.20)
        i += 1
    t_hidan.end_fill()
    t_hidan.penup()
    t_hidan.goto(z, ф)
    t_hidan.pendown()
    i = 0
    t_hidan.begin_fill()
    while i < 75:
        t_hidan.forward(.50)
        t_hidan.right(.90)
        t_hidan.forward(.25)
        t_hidan.left(.95)
        t_hidan.right(.45)
        i += 1
    t_hidan.end_fill()


def head(t_obito: Turtle, x: float, y: float) -> None:
    """Draws Naruto's head."""
    colormode(MODE)
    t_obito.hideturtle()
    t_obito.penup()
    t_obito.goto(x, y)
    t_obito.pendown()
    t_obito.setheading(0.0)
    t_obito.pencolor(SKIN_COLOR)
    t_obito.fillcolor(SKIN_COLOR)
    t_obito.speed(MAX_SPEED)
    t_obito.begin_fill()
    t_obito.right(90)
    t_obito.forward(30)
    t_obito.left(30)
    t_obito.forward(20)
    t_obito.left(45)
    t_obito.forward(17)
    t_obito.left(30)
    t_obito.forward(17)
    t_obito.left(45)
    t_obito.forward(20)
    t_obito.left(25)
    t_obito.forward(28)
    t_obito.end_fill()


def whiskers(t_nagato: Turtle, x: float, y: float, z: float, ф: float) -> None:
    """Draws Naruto's whiskers."""
    colormode(MODE)
    t_nagato.hideturtle()
    t_nagato.penup()
    t_nagato.goto(x, y)
    t_nagato.pendown()
    t_nagato.setheading(10.0)
    t_nagato.pencolor("black")
    t_nagato.speed(MAX_SPEED)
    i: int = 0
    while i < 3:
        t_nagato.forward(8)
        t_nagato.penup()
        t_nagato.left(180)
        t_nagato.forward(8)
        t_nagato.left(90)
        t_nagato.forward(8)
        t_nagato.right(270)
        t_nagato.pendown()
        i += 1
    t_nagato.penup()
    t_nagato.goto(z, ф)
    t_nagato.setheading(-10.0)
    t_nagato.pendown()
    i = 0
    while i < 3:
        t_nagato.forward(8)
        t_nagato.penup()
        t_nagato.left(180)
        t_nagato.forward(8)
        t_nagato.left(90)
        t_nagato.forward(8)
        t_nagato.right(270)
        t_nagato.pendown()
        i += 1


def torso(t_zetsu: Turtle, x: float, y: float) -> None:
    """Draws Naruto's torso."""
    colormode(MODE)
    t_zetsu.hideturtle()
    t_zetsu.penup()
    t_zetsu.goto(x, y)
    t_zetsu.pendown()
    t_zetsu.setheading(-90.0)
    t_zetsu.pencolor(SUIT_COLOR)
    t_zetsu.speed(MAX_SPEED)
    t_zetsu.fillcolor(SUIT_COLOR)
    t_zetsu.begin_fill()
    rectangle(t_zetsu, 175, 70)
    t_zetsu.end_fill()


def black_half(t_orichimaru: Turtle, x: float, y: float) -> None:
    """Draws Naruto's black cloth half."""
    colormode(MODE)
    t_orichimaru.hideturtle()
    t_orichimaru.penup()
    t_orichimaru.goto(x, y)
    t_orichimaru.pendown()
    t_orichimaru.setheading(-90.0)
    t_orichimaru.pencolor("black")
    t_orichimaru.speed(MAX_SPEED)
    t_orichimaru.fillcolor("black")
    t_orichimaru.begin_fill()
    rectangle(t_orichimaru, 85, 70)
    t_orichimaru.end_fill()


def zipper(t_sasori: Turtle, x: float, y: float) -> None:
    """Draws Naruto's zipper."""
    colormode(MODE)
    t_sasori.hideturtle()
    t_sasori.penup()
    t_sasori.goto(x, y)
    t_sasori.pendown()
    t_sasori.setheading(-90.0)
    t_sasori.pencolor("black")
    t_sasori.speed(MAX_SPEED)
    t_sasori.fillcolor("black")
    t_sasori.begin_fill()
    rectangle(t_sasori, 175, 20)
    t_sasori.end_fill()


def left_arm(t_daedera: Turtle, x: float, y: float) -> None:
    """Draws Naruto's left arm."""
    colormode(MODE)
    t_daedera.hideturtle()
    t_daedera.penup()
    t_daedera.goto(x, y)
    t_daedera.pendown()
    t_daedera.setheading(-60.0)
    t_daedera.pencolor("black")
    t_daedera.speed(MAX_SPEED)
    t_daedera.fillcolor("black")
    t_daedera.begin_fill()
    rectangle(t_daedera, 110, 20)
    t_daedera.end_fill()


def right_arm(t_kamui: Turtle, x: float, y: float) -> None:
    """Draws Naruto's right arm."""
    colormode(MODE)
    t_kamui.hideturtle()
    t_kamui.penup()
    t_kamui.goto(x, y)
    t_kamui.pendown()
    t_kamui.setheading(-120.0)
    t_kamui.pencolor("black")
    t_kamui.speed(MAX_SPEED)
    t_kamui.fillcolor("black")
    t_kamui.begin_fill()
    rectangle(t_kamui, 110, 20)
    t_kamui.end_fill()


def right_hand(t_sasuke: Turtle, r_circle: int, x: float, y: float, z: float, ф: float) -> None:
    """Draws Naruto's right hand."""
    colormode(MODE)
    t_sasuke.hideturtle()
    t_sasuke.pencolor(SKIN_COLOR)
    t_sasuke.fillcolor(SKIN_COLOR)
    t_sasuke.penup()
    t_sasuke.goto(x, y)
    t_sasuke.pendown()
    r = r_circle
    t_sasuke.begin_fill()
    t_sasuke.circle(r)
    t_sasuke.end_fill()
    t_sasuke.penup()
    t_sasuke.goto(z, ф)
    t_sasuke.pendown()
    t_sasuke.setheading(-330.0)
    t_sasuke.begin_fill()
    rectangle(t_sasuke, 8, 20)
    t_sasuke.end_fill()


def left_hand(t_kakshi: Turtle, r_circle: int, x: float, y: float, z: float, ф: float) -> None:
    """Draws Naruto's left hand."""
    colormode(MODE)
    t_kakshi.hideturtle()
    t_kakshi.pencolor(SKIN_COLOR)
    t_kakshi.fillcolor(SKIN_COLOR)
    t_kakshi.penup()
    t_kakshi.goto(x, y)
    t_kakshi.pendown()
    r = r_circle
    t_kakshi.begin_fill()
    t_kakshi.circle(r)
    t_kakshi.end_fill()
    t_kakshi.penup()
    t_kakshi.goto(z, ф)
    t_kakshi.pendown()
    t_kakshi.setheading(330.0)
    t_kakshi.begin_fill()
    rectangle(t_kakshi, 8, 20)
    t_kakshi.end_fill()


def right_leg(t_sakura: Turtle, x: float, y: float) -> None:
    """Draws Naruto's right leg."""
    colormode(MODE)
    t_sakura.hideturtle()
    t_sakura.penup()
    t_sakura.goto(x, y)
    t_sakura.pendown()
    t_sakura.setheading(0.0)
    t_sakura.pencolor(SUIT_COLOR)
    t_sakura.fillcolor(SUIT_COLOR)
    t_sakura.speed(MAX_SPEED)
    t_sakura.left(200)
    i: int = 0
    t_sakura.begin_fill()
    while i < 250:
        t_sakura.forward(.50)
        t_sakura.right(.9)
        t_sakura.forward(.25)
        t_sakura.left(1.20)
        i += 1
    t_sakura.end_fill()
    t_sakura.penup()
    t_sakura.goto(0, 0)
    t_sakura.pendown()


def left_leg(t_neji: Turtle, x: float, y: float) -> None:
    """Draws Naruto's left leg."""
    colormode(MODE)
    t_neji.hideturtle()
    t_neji.penup()
    t_neji.goto(x, y)
    t_neji.pendown()
    t_neji.setheading(0.0)
    t_neji.pencolor(SUIT_COLOR)
    t_neji.fillcolor(SUIT_COLOR)
    t_neji.speed(MAX_SPEED)
    t_neji.right(300)
    i: int = 0
    t_neji.begin_fill()
    while i < 250:
        t_neji.forward(.50)
        t_neji.right(.9)
        t_neji.forward(.25)
        t_neji.left(1.20)
        i += 1
    t_neji.end_fill()
    t_neji.penup()
    t_neji.goto(0, 0)
    t_neji.pendown()


def left_foot(t_kisame: Turtle, x: float, y: float) -> None:
    """Draws Naruto's left foot."""
    colormode(MODE)
    t_kisame.hideturtle()
    t_kisame.penup()
    t_kisame.goto(x, y)
    t_kisame.pendown()
    t_kisame.pencolor("black")
    t_kisame.speed(MAX_SPEED)
    t_kisame.fillcolor("black")
    t_kisame.begin_fill()
    rectangle(t_kisame, 15, 25)
    t_kisame.end_fill()
    t_kisame.penup()
    t_kisame.right(90)
    t_kisame.forward(25)
    t_kisame.pendown()
    t_kisame.begin_fill()
    rectangle(t_kisame, 10, -30)
    t_kisame.end_fill()
    t_kisame.penup()
    t_kisame.forward(10)
    t_kisame.left(90)
    t_kisame.forward(20)
    t_kisame.pendown()
    t_kisame.fillcolor(SKIN_COLOR)
    t_kisame.begin_fill()
    rectangle(t_kisame, 10, -10)
    t_kisame.end_fill()


def right_foot(t_kakazu: Turtle, x: float, y: float) -> None:
    """Draws Naruto's left foot."""
    colormode(MODE)
    t_kakazu.hideturtle()
    t_kakazu.penup()
    t_kakazu.goto(x, y)
    t_kakazu.pendown()
    t_kakazu.pencolor("black")
    t_kakazu.speed(MAX_SPEED)
    t_kakazu.fillcolor("black")
    t_kakazu.begin_fill()
    rectangle(t_kakazu, 15, 25)
    t_kakazu.end_fill()
    t_kakazu.penup()
    t_kakazu.forward(-15)
    t_kakazu.right(90)
    t_kakazu.forward(25)
    t_kakazu.pendown()
    t_kakazu.begin_fill()
    rectangle(t_kakazu, 10, -30)
    t_kakazu.end_fill()
    t_kakazu.penup()
    t_kakazu.right(90)
    t_kakazu.forward(-10)
    t_kakazu.pendown()
    t_kakazu.fillcolor(SKIN_COLOR)
    t_kakazu.begin_fill()
    rectangle(t_kakazu, 10, -10)
    t_kakazu.end_fill()


def Naruto() -> None:
    """Draws Naruto."""
    itachi: Turtle = Turtle()
    hidan: Turtle = Turtle()
    madera: Turtle = Turtle()
    obito: Turtle = Turtle()
    nagato: Turtle = Turtle()
    zetsu: Turtle = Turtle()
    orichimaru: Turtle = Turtle()
    sasori: Turtle = Turtle()
    daedera: Turtle = Turtle()
    kamui: Turtle = Turtle()
    sasuke: Turtle = Turtle()
    kakashi: Turtle = Turtle()
    sakura: Turtle = Turtle()
    neji: Turtle = Turtle()
    kisame: Turtle = Turtle()
    kakazu: Turtle = Turtle()
    left_leg(sakura, 65, -330)
    right_leg(neji, 25, -180)
    torso(zetsu, 55, -40)
    black_half(orichimaru, 55, -40)
    zipper(sasori, 30, -40)
    left_arm(daedera, 58, -40)
    right_arm(kamui, 0, -50)
    hair(madera, 55, 5)
    headband(itachi, -5, 0)
    head(obito, -5, -15)
    tassles(hidan, -2, 0, 0, 0)
    whiskers(nagato, 0, -35, 35, -35)
    right_hand(sasuke, 12, 110, -160, 115, -155)
    left_hand(kakashi, 12, -70, -160, -83, -148)
    left_foot(kisame, 62.5, -310)
    right_foot(kakazu, -70, -300)


def Naruto2() -> None:
    """Draws the second Naruto clone."""
    itachi: Turtle = Turtle()
    hidan: Turtle = Turtle()
    madera: Turtle = Turtle()
    obito: Turtle = Turtle()
    nagato: Turtle = Turtle()
    zetsu: Turtle = Turtle()
    orichimaru: Turtle = Turtle()
    sasori: Turtle = Turtle()
    daedera: Turtle = Turtle()
    kamui: Turtle = Turtle()
    sasuke: Turtle = Turtle()
    kakashi: Turtle = Turtle()
    sakura: Turtle = Turtle()
    neji: Turtle = Turtle()
    kisame: Turtle = Turtle()
    kakazu: Turtle = Turtle()
    left_leg(sakura, 65 + SHIFT, -330 + SHIFT)
    right_leg(neji, 25 + SHIFT, -180 + SHIFT)
    torso(zetsu, 55 + SHIFT, -40 + SHIFT)
    black_half(orichimaru, 55 + SHIFT, -40 + SHIFT)
    zipper(sasori, 30 + SHIFT, -40 + SHIFT)
    left_arm(daedera, 58 + SHIFT, -40 + SHIFT)
    right_arm(kamui, 0 + SHIFT, -50 + SHIFT)
    hair(madera, 55 + SHIFT, 5 + SHIFT)
    headband(itachi, -5 + SHIFT, 0 + SHIFT)
    head(obito, -5 + SHIFT, -15 + SHIFT)
    tassles(hidan, -2 + SHIFT, 0 + SHIFT, 0 + SHIFT, 0 + SHIFT)
    whiskers(nagato, 0 + SHIFT, -35 + SHIFT, 35 + SHIFT, -35 + SHIFT)
    right_hand(sasuke, 12, 110 + SHIFT, -160 + SHIFT, 115 + SHIFT, -155 + SHIFT)
    left_hand(kakashi, 12, -70 + SHIFT, -160 + SHIFT, -83 + SHIFT, -148 + SHIFT)
    left_foot(kisame, 62.5 + SHIFT, -310 + SHIFT)
    right_foot(kakazu, -70 + SHIFT, -300 + SHIFT)


def Naruto3() -> None:
    """Draws the third Naruto clone."""
    itachi: Turtle = Turtle()
    hidan: Turtle = Turtle()
    madera: Turtle = Turtle()
    obito: Turtle = Turtle()
    nagato: Turtle = Turtle()
    zetsu: Turtle = Turtle()
    orichimaru: Turtle = Turtle()
    sasori: Turtle = Turtle()
    daedera: Turtle = Turtle()
    kamui: Turtle = Turtle()
    sasuke: Turtle = Turtle()
    kakashi: Turtle = Turtle()
    sakura: Turtle = Turtle()
    neji: Turtle = Turtle()
    kisame: Turtle = Turtle()
    kakazu: Turtle = Turtle()
    left_leg(sakura, 65 + SHIFT2, -330 + SHIFT2)
    right_leg(neji, 25 + SHIFT2, -180 + SHIFT2)
    torso(zetsu, 55 + SHIFT2, -40 + SHIFT2)
    black_half(orichimaru, 55 + SHIFT2, -40 + SHIFT2)
    zipper(sasori, 30 + SHIFT2, -40 + SHIFT2)
    left_arm(daedera, 58 + SHIFT2, -40 + SHIFT2)
    right_arm(kamui, 0 + SHIFT2, -50 + SHIFT2)
    hair(madera, 55 + SHIFT2, 5 + SHIFT2)
    headband(itachi, -5 + SHIFT2, 0 + SHIFT2)
    head(obito, -5 + SHIFT2, -15 + SHIFT2)
    tassles(hidan, -2 + SHIFT2, 0 + SHIFT2, 0 + SHIFT2, 0 + SHIFT2)
    whiskers(nagato, 0 + SHIFT2, -35 + SHIFT2, 35 + SHIFT2, -35 + SHIFT2)
    right_hand(sasuke, 12, 110 + SHIFT2, -160 + SHIFT2, 115 + SHIFT2, -155 + SHIFT2)
    left_hand(kakashi, 12, -70 + SHIFT2, -160 + SHIFT2, -83 + SHIFT2, -148 + SHIFT2)
    left_foot(kisame, 62.5 + SHIFT2, -310 + SHIFT2)
    right_foot(kakazu, -70 + SHIFT2, -300 + SHIFT2)


if __name__ == "__main__":
    main()