import turtle
t = turtle.Turtle()
t.speed(0)

def circlify(length, color, sides):
    t.color(color)
    #t.penup()
    #t.back(length/2)
    #t.pendown()
    for side in range(100):
        t.forward(length)
        t.right(360/sides + 2)

circlify(150, "gold", 4)