from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def forward():
    turtle.forward(10)


def backward():
    turtle.back(10)


def right():
    turtle.right(10)


def left():
    turtle.left(10)


def clear():
    turtle.reset()


screen.listen()
screen.onkey(forward, "w")
screen.onkey(backward, "s")
screen.onkey(right, "d")
screen.onkey(left, "a")
screen.onkey(clear, "c")
screen.exitonclick()
