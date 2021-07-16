from turtle import Turtle, Screen

def clickme(x, y):
    pin.up()
    pin.goto(x, y)
    pin.down()

def dragging(x, y):
    pin.ondrag(None)
    pin.setheading(pin.towards(x, y))
    pin.goto(x, y)
    pin.ondrag(dragging)

screen = Screen()
screen.onclick(clickme)

pin = Turtle()
pin.speed(0)

pin.ondrag(dragging)

screen.mainloop()