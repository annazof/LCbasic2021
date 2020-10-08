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

def draw_equitriangle(t, sz):
    """
    Draw equilateral triangle
    :param t:turtle
    :param sz:length of the side
    :return:
    """
    draw_poly(t, 3, sz)

tess=turtle.Turtle()
tess.color("blue")
tess.pensize(2)

draw_equitriangle(tess,50)
canvas.exitonclick()