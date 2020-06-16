import turtle


def polygon(sides, length):
    t = turtle.Turtle()
    t.color("lime")
    t.speed(0)

    # formula for exterior angle of a polygon
    angle = 360 / sides

    for side in range(sides):
        t.forward(length)
        t.right(angle)

    t.hideturtle()


# Draw polygons from 3 sides to 14 sides
for numSide in range(3, 15):
    polygon(numSide, 50)
