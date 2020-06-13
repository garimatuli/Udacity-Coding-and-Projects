import turtle

jack = turtle.Turtle()
jack.color("pink")
jack.speed(0)


def draw_square(length):
    for side in range(4):
        jack.forward(length)
        jack.right(90)


for square in range(50):
    draw_square(square)
    jack.forward(5)
    jack.left(5)

