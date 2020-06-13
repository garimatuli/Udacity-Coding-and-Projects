import turtle
jack = turtle.Turtle()
jack.color("yellow")
jack.width(4)

def draw_square():
    for side in range(4):
        jack.forward(100)
        jack.right(90)

jack.penup()
jack.back(150)
jack.pendown()

draw_square()
jack.forward(100)
draw_square()
jack.forward(100)
draw_square()