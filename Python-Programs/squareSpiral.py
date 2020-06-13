import turtle

t3 = turtle.Turtle()
t3.width(4)
t3.color('blue')
sides = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for length in sides:
    t3.forward(length)
    t3.right(90)



