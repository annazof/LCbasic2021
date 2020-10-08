import turtle
canvas = turtle.Screen()
canvas.bgcolor("lightgreen")


def draw_square(animal, size):
    """
    Draw a square
    :param animal: This should be the turtle drawing the suare
    :param size: length of the sides of the square
    :return: nothing
    """
    for i in range(4):
        animal.forward(size)
        animal.left(90)

tess=turtle.Turtle()
tess.color("blue")
tess.pensize(3)
tess.speed(200)



for i in range(20):
    draw_square(tess,100)
    tess.left(18)

canvas.exitonclick()