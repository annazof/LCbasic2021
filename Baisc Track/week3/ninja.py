import turtle

paper = turtle.Screen()
paper.bgcolor("lightyellow") # Set the window background color
paper.title("It's Leonardo!") # Set the window title


leonardo = turtle.Turtle()
leonardo.shape("turtle")
leonardo.color("green") # Tell tess to change her color
leonardo.pensize(3) # Tell tess to set her pen width

leonardo.forward(50)
leonardo.penup()
leonardo.forward(50)
leonardo.pendown()
leonardo.stamp()

leonardo.forward(50)

#60 is the angle
leonardo.left(45)
leonardo.forward(50)
leonardo.left(45)
leonardo.forward(50)

#for element in [0,1,2,3,4,5]:
#    leonardo.forward(50)
#    leonardo.left(60)
#    print(element)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

for element in range(12):
    leonardo.color(colors[element % len(colors)])
    if element % 2 == 0:
        leonardo.forward(100)
    else:
        leonardo.forward(100)
    leonardo.forward(50)
    leonardo.left(30)

paper.exitonclick()
