import turtle

jack = turtle.Turtle()
jack.color("yellow")


def draw_square(length, color):
    for side in range(4):
        jack.color(color)
        jack.forward(length)
        jack.right(90)


jack.penup()
jack.backward(100)
jack.pendown()

draw_square(200, "cyan")
draw_square(150, "magenta")
draw_square(100, "yellow")
draw_square(50, "orange")
draw_square(25, "pink")
draw_square(15, "violet")


