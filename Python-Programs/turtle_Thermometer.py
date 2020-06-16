import turtle


def temperature_color(temp):
    if temp < 20:
        return "blue"
    elif temp < 80:
        return "purple"
    else:
        return "red"

    return "green"


def draw_temperature(temp):
    t = turtle.Turtle()
    t.penup()
    t.back(100)
    t.width(20)
    t.pendown()
    for n in range(temp):
        t.color(temperature_color(n))
        t.forward(1)


def draw_therm_box():
    t = turtle.Turtle()
    t.speed(0)
    t.width(4)
    t.color("gray")
    t.penup()
    t.back(120)
    t.pendown()
    t.left(90)
    for side in [20, 240, 40, 240, 20]:
        t.forward(side)
        t.right(90)
    t.hideturtle()


draw_therm_box()
draw_temperature(120)

