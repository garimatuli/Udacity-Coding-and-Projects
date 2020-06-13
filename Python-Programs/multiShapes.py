import turtle

t3 = turtle.Turtle()

def multiShapes():
    t3.color = "cyan"
    t3.width(4)
    t3.penup()
    t3.forward(20)
    t3.pendown()
    for side in range(4):
        t3.forward(100)
        t3.right(90)

    for side in range(5):
        t3.forward(100)
        t3.right(72)

    for side in range(12):
            t3.forward(80)
            t3.right(30)


multiShapes()