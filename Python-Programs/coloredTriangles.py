import turtle

def triangle_boogie(color, start):
  t = turtle.Turtle()
  t.color(color)
  t.speed()
  t.width(5)
  t.right(start)
  for shape in range(6):
    for side in range(3):
        t.forward(100)
        t.right(120)
    t.right(15)
  t.hideturtle()

triangle_boogie("red", 0)
triangle_boogie("orange", 120)
triangle_boogie("blue", 240)