import turtle

rainbow = ["red", "orange", "yellow", "green", "blue", "purple"]

terry = turtle.Turtle()
terry.width(15)
terry.speed(4)

for side in rainbow:
    terry.color(side)

    terry.forward(50)
    terry.right(180)
    terry.forward(50)
    terry.left(90)
    terry.penup()
    terry.forward(15)
    terry.left(90)
    terry.pendown()
