import turtle

t1 = turtle.Turtle()
t2 = turtle.Turtle()

t1.color("orange")
t1.width(4)
## t1.speed(0) ## maximum speed

t2.color("yellow")
t2.width(5)
##t2.speed(10)

def shape1():
    for side in range(10):
        t1.forward(150)
        t1.right(80)

def shape2():
    t2.penup()
    t2.backward(350)
    t2.pendown()
    for side in range(10):
        t2.forward(150)
        t2.right(135)

shape1()
shape2()
