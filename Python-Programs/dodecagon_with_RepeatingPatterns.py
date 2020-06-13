# a 12-sided shape (a dodecagon) with repeating pattern of 4 colors

import turtle

t = turtle.Turtle()
t.width(5)
t.speed(0)

for n in range(12):

    if (n % 4 == 0):
        t.color("red")
    elif (n % 4 == 1):
        t.color("yellow")
    elif (n % 4 == 2):
        t.color("orange")
    else:
        t.color("limegreen")

    t.forward(50)
    t.right(360 / 12)

