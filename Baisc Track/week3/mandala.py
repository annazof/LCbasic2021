import turtle

paper = turtle.Screen()
paper.bgcolor("lightyellow")
paper.title("Mandala")

leo = turtle.Turtle()
leo.shape("turtle")
leo.color("green")
leo.pensize(3)
leo.speed(50)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']


for element in range(12):
    leo.color(colors[element % len(colors)])
    if element % 2 == 0:
        leo.forward(50)
    else:
        leo.forward(50)
    leo.forward(25)
    leo.left(30)

for i in range(100):
    leo.forward(10)
    leo.right(3.6)

leo.right(90)
leo.forward(100)
leo.left(40)









paper.exitonclick()