import turtle
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple", "lime", "cyan"]

t = turtle.Turtle()
t.width(12)
t.speed(0)

for step in range(100):
    # randint() generates a random number from the given range (inclusive)
    angle = random.randint(-90, 90)

    # choice() returns a random item from the list
    color = random.choice(colors)

    t.color(color)
    t.right(angle)
    t.forward(10)


