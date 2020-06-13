import turtle

links = [1, 2, 3, 4]
sides = [1, 2, 3]

weaver = turtle.Turtle()
weaver.width(5)
weaver.color('orange')

# Move back so the chain is centered.
weaver.penup()
weaver.back(80)
weaver.pendown()

for link in links:
    for side in sides:
        weaver.forward(30)
        weaver.right(120)

    # Scoot over to the next link.
    weaver.penup()
    weaver.forward(40)
    weaver.pendown()

weaver.hideturtle()

