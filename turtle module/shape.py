import turtle

d = turtle.Turtle()

d.color("blue", "cyan")

# Square
d.begin_fill()
d.forward(100)
d.setheading(90)
d.forward(100)
d.setheading(180)
d.forward(100)
d.setheading(270)
d.forward(100)
d.end_fill()

d.penup()
d.setheading(270)
d.forward(120)
d.pendown()

d.begin_fill()
d.setheading(0)
d.forward(100)
d.setheading(90)
d.forward(100)
d.setheading(180)
d.forward(100)
d.setheading(270)
d.forward(100)
d.end_fill()

turtle.done()