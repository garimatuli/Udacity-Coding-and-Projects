import turtle

jack = turtle.Turtle()
jack.color("yellow")

def draw_polygon(length, color, sides):
    for side in range(sides):
        jack.color(color)
        jack.forward(length)
        jack.right(360 / sides)

jack.penup()
jack.backward(100)
jack.pendown()

draw_polygon(120, "cyan", 8)
draw_polygon(100, "magenta", 7)
draw_polygon(80, "yellow", 6)
draw_polygon(60, "orange", 5)
draw_polygon(50, "pink", 4)
draw_polygon(30, "green", 3)


