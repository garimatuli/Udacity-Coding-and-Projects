import turtle

romeo = turtle.Turtle()
romeo.color("violet")
romeo.width(5)
romeo.speed(0)

def draw_square(some_turtle):
    for side in range(4):
        some_turtle.forward(40)
        some_turtle.right(90)


# draw_flower(romeo)
def draw_flower():
    for petal in range(6):
        draw_square(romeo)
        romeo.right(60)

for bunch in range(6):
    draw_flower()
    romeo.penup()
    romeo.right(60)
    romeo.forward(120)
    romeo.pendown()

romeo.hideturtle()