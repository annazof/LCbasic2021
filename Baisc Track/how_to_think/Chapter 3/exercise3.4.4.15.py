#An equilateral triangle

import turtle
canvas = turtle.Screen()
leo = turtle.Turtle()

#triangle
for i in range(3):
    leo.forward(50)
    leo.left(120)

#square
for i in range(4):
    leo. forward(100)
    leo.left(90)

#hexagon
for i in range(6):
    leo.forward(80)
    leo.right(60)

#octagon
for i in range(8):
    leo.forward(150)
    leo.left(45)

canvas.exitonclick()
