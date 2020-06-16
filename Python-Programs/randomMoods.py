import random
import turtle
riley = turtle.Turtle()
riley.width(5)

moods = ["happy", "angry", "party", "sad","other"]

def getColor():
    mood = random.choice(moods)

    if mood == "happy":
        riley.color("magenta")
    elif mood == "party":
        riley.color("blue")
    elif mood == "angry":
        riley.color("red")
    elif mood == "sad":
        riley.color("gray")
    else:
        riley.color("yellow")

for stars in range(3):
    for side in range(5):
        getColor();
        riley.forward(100)
        riley.right(144)
    riley.penup()
    riley.backward(100)
    riley.right(15)
    riley.pendown()