import turtle

t = turtle.Turtle()
t.color("lime")
t.width(3)
t.penup()
t.shape("turtle")

for step in range(2000):
    t.forward(1)
    # t.ycor() will give y coordinates of turtle
    if t.xcor() < -170 or t.xcor() > 170:
        t.right(180)