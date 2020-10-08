import turtle
canvas = turtle.Screen()
canvas.bgcolor("lightgreen")


tess=turtle.Turtle()
tess.color("blue")
tess.pensize(2)
tess.speed(200)

s=1

for i in range(99):
    tess.right(90)
    tess.forward(s)
    s+=2
tess.stamp()


tess.penup()
tess.left(45)
tess.forward(200)
tess.pendown()

l=1
for i in range(99):
    tess.right(91)
    tess.forward(l)
    l+=2

canvas.exitonclick()
