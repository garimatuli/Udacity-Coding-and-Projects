# staircase pattern with modulo operation

import turtle

t = turtle.Turtle()

t.speed(0)
t.width(5)
t.color("blue")

t.penup()
t.backward(150)
t.pendown()

for i in range(9):
    t.forward(50)
    if (i % 2 == 0):
        t.left(90)
        t.color("red")
    else:
        t.right(90)
        t.color("blue")

t.hideturtle()



