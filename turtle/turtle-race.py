from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500, height=500)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []


def start():
    y = -100
    for i in colors:
        n = Turtle(shape="turtle")
        n.penup()
        n.color(i)
        n.goto(-240, y)
        y += 40
        turtles.append(n)


if user_bet:
    is_race_on = True
start()
while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(
                    f"You won! The {winning_color} turtle got to the finish first!")
            else:
                print(f"You lost! The {winning_color} turtle won the race.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
