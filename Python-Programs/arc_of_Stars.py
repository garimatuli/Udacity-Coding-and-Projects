import turtle


def star(color, sides, length, angle, distance):
    galileo = turtle.Turtle()
    galileo.color(color)  # colorful!
    galileo.width(5)  # visible!
    galileo.speed(0)  # fast!
    galileo.penup()
    galileo.left(angle)  # away from center
    galileo.forward(distance)
    galileo.pendown()  # start drawing

    for side in range(sides):
        galileo.forward(length)
        galileo.left(720 / sides)
    galileo.hideturtle()  # just the star


# To draw outer arc of Stars
for angle in [180, 135, 90, 45, 0]:
    star("magenta", 5, 50, angle, 100)

# To draw inner arc of Stars
for angle in [180, 135, 90, 45, 0]:
    star("limegreen", 5, 30, angle, 50)

