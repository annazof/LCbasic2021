
import turtle
canvas = turtle.Screen()
leo = turtle.Turtle()

angles=[160, -43, 270, -97, -43, 200, -940, 17, -86]

for i in angles:
    leo.left(i)
    leo.forward(100)

canvas.exitonclick()
