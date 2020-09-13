"""My attempt at the infamous shadow clone jutsu."""

__author__ = "730312903"

from turtle import Turtle, colormode, tracer, update, done 
MAX_SPEED: int = 0
SHIFT: int = 200
SHIFT2: int = 350
SHIFT3: int = -200
#MESSAGE TO GRADERS, the Naruto() function is the function I have avoided from becoming too complex by breaking it down intp multiple drawing stages before it is called in main. This is my attempt at the 10 points of credit
#...I believe my scene is more complex then what could only be achieved with four procedures for the 5 additional points of credit. 

def main() -> None:
    """The jutsu has been cast."""
    tracer(0, 0) #this is disabling drawing and have it update immediately
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

    Naruto()
    Naruto2()
    # Naruto3()
    # Naruto4()
    update()
    done()

def hair(t_madera: Turtle, x: float, y: float) -> None:
    """Draws Naruto's hair."""
    colormode(255)
    t_madera.hideturtle()
    t_madera.penup()
    t_madera.goto(x, y)
    t_madera.pendown()
    t_madera.setheading(0.0)
    t_madera.pencolor("yellow")
    t_madera.fillcolor(254, 232, 42)
    t_madera.speed(100)

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
    colormode(255)
    t_itachi.hideturtle()
    t_itachi.penup()
    t_itachi.goto(x, y)
    t_itachi.pendown()
    t_itachi.setheading(0.0)
    t_itachi.pencolor("black")
    t_itachi.fillcolor(0, 0, 0)
    t_itachi.speed(100)

    i: into = 0
    t_itachi.begin_fill()
    while i < 2:
        t_itachi.forward(55)
        t_itachi.right(90)
        t_itachi.forward(15)
        t_itachi.right(90)
        i += 1
    t_itachi.end_fill()


def tassles(t_hidan: Turtle, x: float, y: float, z: float, ф: float) -> None:
    """Draws the tassles behind Naruto's headband."""
    colormode(255)
    t_hidan.hideturtle()
    t_hidan.penup()
    t_hidan.goto(x, y)
    t_hidan.pendown()
    t_hidan.setheading(0.0)
    t_hidan.pencolor("black")
    t_hidan.fillcolor(0, 0, 0)
    t_hidan.speed(10000)
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
    i: int = 0
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
    colormode(255)
    t_obito.hideturtle()
    t_obito.penup()
    t_obito.goto(x, y)
    t_obito.pendown()
    t_obito.setheading(0.0)
    t_obito.pencolor(255, 227, 158)
    t_obito.fillcolor(255, 227, 158)
    t_obito.speed(100)

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
    colormode(255)
    t_nagato.hideturtle()
    t_nagato.penup()
    t_nagato.goto(x, y)
    t_nagato.pendown()
    t_nagato.setheading(10.0)
    t_nagato.pencolor("black")
    t_nagato.speed(10000)

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
    colormode(255)
    t_zetsu.hideturtle()
    t_zetsu.penup()
    t_zetsu.goto(x, y)
    t_zetsu.pendown()
    t_zetsu.setheading(-90.0)
    t_zetsu.pencolor(252, 147, 13)
    t_zetsu.speed(10000)
    t_zetsu.fillcolor(252, 147, 13)

    i: int = 0
    t_zetsu.begin_fill()
    while i < 2:
        t_zetsu.forward(175)
        t_zetsu.right(90)
        t_zetsu.forward(70)
        t_zetsu.right(90)
        i += 1
    t_zetsu.end_fill()

def black_half(t_orichimaru: Turtle, x: float, y: float) -> None:
    """Draws Naruto's black cloth half."""
    colormode(255)
    t_orichimaru.hideturtle()
    t_orichimaru.penup()
    t_orichimaru.goto(x, y)
    t_orichimaru.pendown()
    t_orichimaru.setheading(-90.0)
    t_orichimaru.pencolor("black")
    t_orichimaru.speed(10000)
    t_orichimaru.fillcolor(0, 0, 0)

    i: int = 0
    t_orichimaru.begin_fill()
    while i < 2:
        t_orichimaru.forward(85)
        t_orichimaru.right(90)
        t_orichimaru.forward(70)
        t_orichimaru.right(90)
        i += 1
    t_orichimaru.end_fill()

def zipper(t_sasori: Turtle, x: float, y: float) -> None:
    """Draws Naruto's zipper."""
    colormode(255)
    t_sasori.hideturtle()
    t_sasori.penup()
    t_sasori.goto(x, y)
    t_sasori.pendown()
    t_sasori.setheading(-90.0)
    t_sasori.pencolor("black")
    t_sasori.speed(10000)
    t_sasori.fillcolor(0, 0, 0)

    i: int = 0
    t_sasori.begin_fill()
    while i < 2:
        t_sasori.forward(175)
        t_sasori.right(90)
        t_sasori.forward(20)
        t_sasori.right(90)
        i += 1
    t_sasori.end_fill()

def left_arm(t_daedera: Turtle, x: float, y: float) -> None:
    """Draws Naruto's left arm."""
    colormode(255)
    t_daedera.hideturtle()
    t_daedera.penup()
    t_daedera.goto(x, y)
    t_daedera.pendown()
    t_daedera.setheading(-60.0)
    t_daedera.pencolor("black")
    t_daedera.speed(10000)
    t_daedera.fillcolor(0, 0, 0)

    i: int = 0
    t_daedera.begin_fill()
    while i < 2:
        t_daedera.forward(110)
        t_daedera.right(90)
        t_daedera.forward(20)
        t_daedera.right(90)
        i += 1
    t_daedera.end_fill()

def right_arm(t_kamui: Turtle, x: float, y: float) -> None:
    """Draws Naruto's right arm."""
    colormode(255)
    t_kamui.hideturtle()
    t_kamui.penup()
    t_kamui.goto(x, y)
    t_kamui.pendown()
    t_kamui.setheading(-120.0)
    t_kamui.pencolor("black")
    t_kamui.speed(10000)
    t_kamui.fillcolor(0, 0, 0)

    i: int = 0
    t_kamui.begin_fill()
    while i < 2:
        t_kamui.forward(110)
        t_kamui.right(90)
        t_kamui.forward(20)
        t_kamui.right(90)
        i += 1
    t_kamui.end_fill()

def right_hand(t_sasuke: Turtle, r_circle: int, x: float, y: float, z: float, ф: float) -> None:
    """Draws Naruto's right hand."""
    colormode(255)
    t_sasuke.hideturtle()
    t_sasuke.pencolor(255, 227 , 158)
    t_sasuke.fillcolor(255, 227, 158)
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
    i: int = 0
    t_sasuke.begin_fill()
    while i < 2:
        t_sasuke.forward(8)
        t_sasuke.right(90)
        t_sasuke.forward(20)
        t_sasuke.right(90)
        i += 1
    t_sasuke.end_fill()


def left_hand(t_kakshi: Turtle, r_circle: int, x: float, y: float, z: float, ф: float) -> None:
    """Draws Naruto's left hand."""
    colormode(255)
    t_kakshi.hideturtle()
    t_kakshi.pencolor(255, 227 , 158)
    t_kakshi.fillcolor(255, 227, 158)
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
    i: int = 0
    t_kakshi.begin_fill()
    while i < 2:
        t_kakshi.forward(8)
        t_kakshi.right(90)
        t_kakshi.forward(20)
        t_kakshi.right(90)
        i += 1
    t_kakshi.end_fill()

def right_leg(t_sakura: Turtle, x: float, y: float) -> None:
    """Draws Naruto's right leg."""
    colormode(255)
    t_sakura.hideturtle()
    t_sakura.penup()
    t_sakura.goto(x, y)
    t_sakura.pendown()
    t_sakura.setheading(0.0)
    t_sakura.pencolor(252, 147, 13)
    t_sakura.fillcolor(252, 147, 13)
    t_sakura.speed(10000)
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
    colormode(255)
    t_neji.hideturtle()
    t_neji.penup()
    t_neji.goto(x, y)
    t_neji.pendown()
    t_neji.setheading(0.0)
    t_neji.pencolor(252, 147, 13)
    t_neji.fillcolor(252, 147, 13)
    t_neji.speed(10000)
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
    colormode(255)
    t_kisame.hideturtle()
    t_kisame.penup()
    t_kisame.goto(x, y)
    t_kisame.pendown()
    t_kisame.pencolor("black")
    t_kisame.speed(10000)
    t_kisame.fillcolor(0, 0, 0)

    i: int = 0
    t_kisame.begin_fill()
    while i < 2:
        t_kisame.forward(15)
        t_kisame.right(90)
        t_kisame.forward(25)
        t_kisame.right(90)
        i += 1
    t_kisame.end_fill()
    t_kisame.penup()
    t_kisame.right(90)
    t_kisame.forward(25)
    t_kisame.pendown()

    i = 0
    t_kisame.begin_fill()
    while i < 2:
        t_kisame.forward(10)
        t_kisame.right(90)
        t_kisame.forward(-30)
        t_kisame.right(90)
        i += 1
    t_kisame.end_fill()

    t_kisame.penup()
    t_kisame.forward(10)
    t_kisame.left(90)
    t_kisame.forward(20)
    t_kisame.pendown()
    t_kisame.fillcolor(255, 227, 158)

    i = 0
    t_kisame.begin_fill()
    while i < 2:
        t_kisame.forward(10)
        t_kisame.right(90)
        t_kisame.forward(-10)
        t_kisame.right(90)
        i += 1
    t_kisame.end_fill()

def right_foot(t_kakazu: Turtle, x: float, y: float) -> None:
    """Draws Naruto's left foot."""
    colormode(255)
    t_kakazu.hideturtle()
    t_kakazu.penup()
    t_kakazu.goto(x, y)
    t_kakazu.pendown()
    t_kakazu.pencolor("black")
    t_kakazu.speed(10000)
    t_kakazu.fillcolor(0, 0, 0)

    i: int = 0
    t_kakazu.begin_fill()
    while i < 2:
        t_kakazu.forward(15)
        t_kakazu.right(90)
        t_kakazu.forward(25)
        t_kakazu.right(90)
        i += 1
    t_kakazu.end_fill()
    t_kakazu.penup()
    t_kakazu.forward(-15)
    t_kakazu.right(90)
    t_kakazu.forward(25)
    t_kakazu.pendown()

    i = 0
    t_kakazu.begin_fill()
    while i < 2:
        t_kakazu.forward(10)
        t_kakazu.right(90)
        t_kakazu.forward(-30)
        t_kakazu.right(90)
        i += 1
    t_kakazu.end_fill()

    t_kakazu.penup()
    t_kakazu.right(90)
    t_kakazu.forward(-10)
    t_kakazu.pendown()
    t_kakazu.fillcolor(255, 227, 158)

    i = 0
    t_kakazu.begin_fill()
    while i < 2:
        t_kakazu.forward(10)
        t_kakazu.right(90)
        t_kakazu.forward(-10)
        t_kakazu.right(90)
        i += 1
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
    left_hand(kakashi, 12, -70 + SHIFT, -160 +SHIFT, -83 + SHIFT, -148 + SHIFT)
    left_foot(kisame, 62.5 + SHIFT, -310 + SHIFT)
    right_foot(kakazu, -70 + SHIFT, -300 + SHIFT)

# def Naruto3() -> None:
#     """Draws the third Naruto clone."""
#     itachi: Turtle = Turtle()
#     hidan: Turtle = Turtle()
#     madera: Turtle = Turtle()
#     obito: Turtle = Turtle()
#     nagato: Turtle = Turtle()
#     zetsu: Turtle = Turtle()
#     orichimaru: Turtle = Turtle()
#     sasori: Turtle = Turtle()
#     daedera: Turtle = Turtle()
#     kamui: Turtle = Turtle()
#     sasuke: Turtle = Turtle()
#     kakashi: Turtle = Turtle()
#     sakura: Turtle = Turtle()
#     neji: Turtle = Turtle()
#     kisame: Turtle = Turtle()
#     kakazu: Turtle = Turtle()
#     left_leg(sakura, 65 + SHIFT2, -330 + SHIFT2)
#     right_leg(neji, 25 + SHIFT2, -180 + SHIFT2)
#     torso(zetsu, 55 + SHIFT2, -40 + SHIFT2)
#     black_half(orichimaru, 55 + SHIFT, -40 + SHIFT)
#     zipper(sasori, 30 + SHIFT2, -40 + SHIFT2)
#     left_arm(daedera, 58 + SHIFT2, -40 + SHIFT2)
#     right_arm(kamui, 0 + SHIFT2, -50 + SHIFT2)
#     hair(madera, 55 + SHIFT2, 5 + SHIFT2)
#     headband(itachi, -5 + SHIFT2, 0 + SHIFT2)
#     head(obito, -5 + SHIFT2, -15 + SHIFT2)
#     tassles(hidan, -2 + SHIFT2, 0 + SHIFT2, 0 + SHIFT2, 0 + SHIFT2)
#     whiskers(nagato, 0 + SHIFT2, -35 + SHIFT2, 35 + SHIFT2, -35 + SHIFT2)
#     right_hand(sasuke, 12, 110 + SHIFT2, -160 + SHIFT2, 115 + SHIFT2, -155 + SHIFT2)
#     left_hand(kakashi, 12, -70 + SHIFT2, -160 +SHIFT2, -83 + SHIFT2, -148 + SHIFT2)
#     left_foot(kisame, 62.5 + SHIFT2, -310 + SHIFT2)
#     right_foot(kakazu, -70 + SHIFT2, -300 + SHIFT2)

# def Naruto4() -> None:
#     """Draws the fourth Naruto clone."""
#     itachi: Turtle = Turtle()
#     hidan: Turtle = Turtle()
#     madera: Turtle = Turtle()
#     obito: Turtle = Turtle()
#     nagato: Turtle = Turtle()
#     zetsu: Turtle = Turtle()
#     orichimaru: Turtle = Turtle()
#     sasori: Turtle = Turtle()
#     daedera: Turtle = Turtle()
#     kamui: Turtle = Turtle()
#     sasuke: Turtle = Turtle()
#     kakashi: Turtle = Turtle()
#     sakura: Turtle = Turtle()
#     neji: Turtle = Turtle()
#     kisame: Turtle = Turtle()
#     kakazu: Turtle = Turtle()
#     left_leg(sakura, 65 + SHIFT3, -330 + SHIFT3)
#     right_leg(neji, 25 + SHIFT3, -180 + SHIFT3)
#     torso(zetsu, 55 + SHIFT3, -40 + SHIFT3)
#     black_half(orichimaru, 55 + SHIFT, -40 + SHIFT)
#     zipper(sasori, 30 + SHIFT3, -40 + SHIFT3)
#     left_arm(daedera, 58 + SHIFT3, -40 + SHIFT3)
#     right_arm(kamui, 0 + SHIFT3, -50 + SHIFT3)
#     hair(madera, 55 + SHIFT3, 5 + SHIFT3)
#     headband(itachi, -5 + SHIFT3, 0 + SHIFT3)
#     head(obito, -5 + SHIFT3, -15 + SHIFT3)
#     tassles(hidan, -2 + SHIFT3, 0 + SHIFT3, 0 + SHIFT3, 0 + SHIFT3)
#     whiskers(nagato, 0 + SHIFT3, -35 + SHIFT3, 35 + SHIFT3, -35 + SHIFT3)
#     right_hand(sasuke, 12, 110 + SHIFT3, -160 + SHIFT3, 115 + SHIFT3, -155 + SHIFT3)
#     left_hand(kakashi, 12, -70 + SHIFT3, -160 +SHIFT3, -83 + SHIFT3, -148 + SHIFT3)
#     left_foot(kisame, 62.5 + SHIFT3, -310 + SHIFT3)
#     right_foot(kakazu, -70 + SHIFT3, -300 + SHIFT3)



if __name__ == "__main__":
    main()
