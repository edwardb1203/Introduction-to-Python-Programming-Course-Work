"""Turtle Graphics tutorial."""

# this is how we import turtle functions
# # from turtle import [function_name]
# # <_turtlevariable_>: Turtle = Turtle() 
# in order to make the turtle do stuff we need to use turtle_object_variable.method_name()
#To move the turtle to a new x, y position: <turtlevariable>.goto(<x_coordinate>,<y_coordinate>)
# To prevent the turtle from drawing: <turtlevariable>.penup() or <turtlevariable>.up()
# To allow the turtle to draw: <turtlevariable>.pendown() or <turtlevariable>.down()
#To change the color with a string value: <turtlevariable>.color(“<color>”)
#In order to have more control over our colors we can use RGB (red, green, blue) values instead. Using the color picker, use the site to pick out your favorite color and copy the three numbers next to RGB.
#To enable RGB mode, add under the import statement: colormode(255)
#To change the color with RGB values: <turtlevariable>.color(<red>, <green>, <blue>)
#To fill in a shape we just have to tell the turtle when to start filling and end filling. It will fill with whatever the current color is.
#To begin fill: <turtlevariable>.begin_fill()
#To end fill: <turtlevariable>.end_fill()
# To set only pen color: <turtlevariable>.pencolor(<color>)
# To set only fill color: <turtlevariable>.fillcolor(<color>)
# To set fill and pen color: <turtlevariable>.color(<pencolor>, <fillcolor>)
# To change the speed: <turtlevariable>.speed(<speed>)
# To end fill: <turtlevariable>.hideturtle() or <turtlevariable>.ht()




from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

# leo.forward(50)
# leo.right(90)
# leo.forward(50)
# leo.right(90)
# leo.forward(50)
# leo.right(90)
# leo.forward(50)
# done()

# sick shape
# i: int = 0
# while (i < 4):
#     leo.forward(50)
#     leo.left(135)
#     leo.forward(50)
#     leo.left(135)
#     leo.forward(50)
#     i += 1
# done()

# #triangle
# i: int = 0
# while (i < 3):
#     leo.forward(300)
#     leo.left(120)
#     i += 1
# done()


side_length: int = 300

leo.speed(1000)
leo.hideturtle()
leo.penup()
leo.goto(-150, -150)
leo.pendown()

colormode(255)
leo.pencolor("red")
leo.fillcolor(31, 180, 243)


# colormode(255)
# leo.color(233, 66, 30)


# leo.begin_fill()
# # code for shape to be filled 
# leo.end_fill()

leo.begin_fill()
i: int = 0
while (i < 100):
    leo.forward(side_length)
    leo.left(118)
    i += 1
leo.end_fill()
done()

# pete: Turtle = Turtle()
# pete.speed(1000)
# pete.hideturtle()
# pete.penup()
# pete.goto(-150, -150)
# pete.pendown()
# pete.pencolor("orange")
# i: int = 0
# while (i < 100):
#     side_length = (side_length - 50) * .93
#     pete.forward(side_length)
#     pete.left(100)
#     i += 1
# done()


bob: Turtle = Turtle()

bob.pencolor("black")
bob.fillcolor(0, 0, 0)
bob.speed(50)
bob.penup()
bob.goto(-150, -150)
bob.pendown()

# i: int = 0
# while (i < 100):
#     side_length = side_length * .97
#     bob.forward(side_length)
#     bob.left(122)
#     i += 1
# done()








