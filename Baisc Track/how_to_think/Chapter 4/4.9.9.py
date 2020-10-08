#Write a void function to draw a star, where the length of each side is 100 units. (Hint: You should turn the turtle
#by 144 degrees at each point.)

import turtle

paper = turtle.Screen()
leonardo = turtle.Turtle()

def draw_star(n):
    """
    Draw star
    :param n: length of side
    :return: 
    """
    for i in range (5):
        leonardo.right(144)
        leonardo.forward(n)

draw_star(100)
paper.exitonclick()
