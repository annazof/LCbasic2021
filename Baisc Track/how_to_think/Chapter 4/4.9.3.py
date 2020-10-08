import turtle
canvas = turtle.Screen()
canvas.bgcolor("lightgreen")


def draw_poly(t,n,sz):
    """
    Draw polygon
    :param t:turtle
    :param n:number of sides
    :param sz:length of the side
    :return:
    """
    for i in range(n):
        t.forward(sz)
        t.left(360/n)
    t.pendown()


tess=turtle.Turtle()
tess.shape("arrow")
tess.color("pink")
tess.pensize(3)

draw_poly(tess, 8, 50)

canvas.exitonclick()
