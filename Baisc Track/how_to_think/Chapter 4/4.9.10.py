import turtle

paper = turtle.Screen()
leo = turtle.Turtle()
paper.bgcolor("lightgreen")
leo.shape("arrow")
leo.color("pink")
leo.pensize(3)

def draw_star(n):
    """
    Draw star
    :param n: length of side
    :return:
    """
    for i in range (5):
        leo.right(144)
        leo.forward(n)


def draw_5_stars (n):
    for i in range(5):
        draw_star(n)
        #leo.penup()
        leo.forward(350)
        leo.right(144)
        #leo.pendown()

draw_5_stars (100)
paper.exitonclick()
