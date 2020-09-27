
import turtle
canvas = turtle.Screen()
canvas.bgcolor("lightgreen")
leo = turtle.Turtle()

leo.shape("turtle")
leo.color("blue")
leo.stamp()
leo.penup()

for i in range(12):
    leo.forward(50)
    leo.pendown()
    leo.forward(5)
    leo.penup()
    leo.forward(10)
    leo.stamp()
    leo.backward(65)
    leo.left(30)

canvas.exitonclick()