from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape("turtle")
turtle.color("DarkRed")
for i in range(4):
    turtle.forward(100)
    turtle.left(90)

screen = Screen()
screen.exitonclick()
