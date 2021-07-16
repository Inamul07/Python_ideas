import turtle

def star(turtle, size):
    if size <= 10:
        return
    else:
        turtle.begin_fill()
        for i in range(5):
            turtle.forward(size)
            star(turtle, size/3)
            turtle.left(216)
            turtle.end_fill()

a = turtle.Turtle()
a.getscreen().bgcolor("black")

a.penup()
a.goto(-200, 100)
a.pendown()
a.color("blue")

a.speed(25)
star(a, 360)
turtle.done()