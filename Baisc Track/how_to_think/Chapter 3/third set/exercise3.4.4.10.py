steps=[(160, 20), (-43, 10), (270, 8), (-43, 12)]

import turtle
canvas = turtle.Screen()
leo = turtle.Turtle()

for angle, dis in steps:
    leo.left(angle)
    leo.forward(dis)

canvas.exitonclick()
