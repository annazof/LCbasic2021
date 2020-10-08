
import turtle
canvas = turtle.Screen()
canvas.bgcolor("lightgreen")
leo = turtle.Turtle()
leo.shape("arrow")
leo.color("pink")
leo.pensize(3)


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
        size +=20
        leo.penup()
        leo.left(-135)
        leo.forward(10*2**0.5)
        leo.left(135)
        leo.pendown()
    leo.stamp()

draw_squares(5,20)

canvas.exitonclick()