import turtle

screen = turtle.Screen()
fred = turtle.Turtle()

steps = [160, -43, 270, -97, -43, 200, -940, 17, -86]

direction = 0
for step in steps:
    fred.left(step)
    fred.forward(100)
    direction += step

print("The final direction is", direction % 360)

screen.exitonclick()