import turtle

# Set the number of sides of polygon
sides = 10

# Set the length of a side - the pixels by which the turtle will move forward.
length = 50

t = turtle.Turtle()
t.color("orange")
t.width(5)

for side in range(sides):
    t.forward(length)
    t.right(360/sides)  ## angle by which turtle turns
