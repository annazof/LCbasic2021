steps=[(90,50),(30,50),(120,50),(120,50),(-135,50*2**0.5), (135,50),(135,50*2**0.5),(135,50)]


import turtle
canvas = turtle.Screen()
leo = turtle.Turtle()

for angle, dis in steps:
    leo.left(angle)
    leo.forward(dis)

canvas.exitonclick()