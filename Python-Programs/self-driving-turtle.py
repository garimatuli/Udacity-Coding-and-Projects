import turtle
import random

def draw_box(length):
    tur = turtle.Turtle()
    tur.speed(0)
    tur.color("gray")
    tur.penup()
    tur.back(length/2)
    tur.left(90)
    tur.forward(length/2)
    tur.right(90)
    tur.pendown()
    for side in range(4):
        tur.forward(length)
        tur.right(90)
    tur.hideturtle()

draw_box(260)

t = turtle.Turtle()
t.shape("turtle")
t.color("olive")
t.penup()
t.speed(1)

for e in range(2000):
    t.right(random.randint(-10, 10))
    t.forward(10)
    # Code to keep the turtle within box boundaries using x & y coordinates
    outOfBoundary = t.xcor() <= -110 or t.xcor() >= 110 or t.ycor() <= -110 or t.ycor() >= 110
    if outOfBoundary:
        t.right(180)
        t.forward(10)
