import turtle

t = turtle.Turtle()
t.color("lime")
t.width(3)
t.penup()

# to get shape as turtle instead of default shape arrow
t.shape("turtle")
t.speed(0)

for step in range(500):
    t.pendown()
    t.forward(1)

    # keep turtle bound with x coordinates between 150 & -150 pixels
    if t.xcor() > 150 or t.xcor() < -150:
        # t.penup()
        t.right(90)
        t.forward(20)
        # try with t.right(90) instead of t.right(180)
        t.right(180)
        t.color("blue")
        t.forward(20)
        # t.pendown()

