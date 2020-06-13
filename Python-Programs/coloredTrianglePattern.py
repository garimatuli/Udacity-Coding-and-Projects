import turtle

t = turtle.Turtle()
t.speed(0)

def shape(color, width, number, length, angle):
    t.color(color)
    t.width(width)
    for n in range(9):
        for n in range(6):
            t.forward(length)
            t.right(angle)
        t.right(12)

shape('blue', 4, 10, 100, 120)
shape('red', 4, 10, 100, 120)
shape('yellow', 4, 10, 100, 120)