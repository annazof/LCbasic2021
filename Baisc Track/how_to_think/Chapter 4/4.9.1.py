
import turtle
canvas = turtle.Screen()
canvas.bgcolor("lightgreen")
leo = turtle.Turtle()
leo.shape("arrow")
leo.color("pink")
leo.pensize(5)

def draw_square (size):
    for i in range (4):
        leo.forward(size)
        leo.left(90)

def draw_squares (number, size):
    """
    Draw squares
    :param number: number of squares
    :param size: size of the squares, input length of side
    :return: nothing
    """
    for i in range(number):
        draw_square(size)
        leo.penup()
        leo.forward(2*size)
        leo.pendown()
    leo.stamp()

draw_squares(5,20)

canvas.exitonclick()