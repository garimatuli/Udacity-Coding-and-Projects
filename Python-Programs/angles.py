import turtle

builder = turtle.Turtle()
builder.color("red")
builder.width(5)

angles = [-90, 0, 0, -90,
          135, 0, 0, 0,
          90, 0, 0, 0,
          135, -90, 0, 0,
          90, 0, 0, 0]

for angle in angles:
    builder.right(angle)
    builder.forward(25)

