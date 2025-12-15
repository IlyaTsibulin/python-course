# import colorgram

# colors = colorgram.extract('turtle/hirst.Jpeg', 6)
# rgb_colors = []
# for i in colors:
#     rgb_colors.append((i.rgb[0], i.rgb[1], i.rgb[2]))
# print(rgb_colors)

import random
from turtle import Turtle, Screen
color_list = [(229, 228, 227), (226, 224, 225), (198, 175, 119),
              (125, 36, 23), (187, 157, 50), (170, 104, 56)]

screen = Screen()
screen.colormode(255)
turtle = Turtle()
turtle.width(20)
turtle.speed(10)
turtle.hideturtle()


def line(lenght):
    for i in range(lenght):
        turtle.pencolor(color_list[random.randint(0, len(color_list)-1)])
        turtle.dot(20)
        turtle.penup()
        turtle.forward(40)
        turtle.pendown()


def go_back():
    turtle.penup()
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(400)
    turtle.left(180)
    turtle.pendown()


turtle.penup()
turtle.setheading(225)
turtle.forward(250)
turtle.setheading(0)

for i in range(10):
    line(10)
    if i == 9:
        break
    go_back()

screen.exitonclick
