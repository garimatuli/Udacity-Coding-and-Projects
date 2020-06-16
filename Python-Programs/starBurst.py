import turtle


def star(color, sides, length, angle, distance, width):
    galileo = turtle.Turtle()
    galileo.color(color)  # colorful!
    galileo.width(width)  # visible!
    galileo.speed(0)  # fast!
    galileo.penup()
    galileo.left(angle)  # away from center
    galileo.forward(distance)
    galileo.pendown()  # start drawing
    for side in range(sides):
        galileo.forward(length)
        galileo.left(720 / sides)
    galileo.hideturtle()  # just the star


# draw outer circle
for angle in [180, 135, 90, 45, 0, -45, -90, -135]:
    star("violet", 5, 50, angle, 100, 5)

# draw middle circle

# for angle in [180, 135, 90, 45, 0, -45, -90, -135]:

# Above line or below both draws same result

for angle in [315, 270, 225, 180, 135, 90, 45, 0]:
    star("blue", 5, 30, angle, 60, 4)

# draw inner circle
for angle in [180, 135, 90, 45, 0, -45, -90, -135]:
    star("orange", 5, 30, angle, 20, 2)