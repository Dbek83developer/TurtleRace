from turtle import Turtle, Screen
import random


def make_turtle(color, x, y):
    tim: Turtle = Turtle("turtle")
    tim.color(color)
    tim.penup()
    tim.goto(x, y)
    return tim


score = Turtle()
score.color("black")
score.hideturtle()
score.penup()
score.goto(0, 0)

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your bet!", "Which turtle win the race? Enter the color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
y_cor = [-150, -100, -50, 0, 50, 100, 150]
turtles = []

for joji_index in range(0, 7):
    joji = make_turtle(colors[joji_index], -230, y_cor[joji_index])
    turtles.append(joji)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                score.write(f"You've won! The {winning_color} turtle is won!", align="center",
                            font=("Arial", 20, "normal"))
                print(f"You've won! The {winning_color} turtle is won!")
            else:
                score.write(f"You've lost! The {winning_color} turtle is won!", align='center',
                            font=('Arial', 20, 'normal'))
                print(f"You've lost! The {winning_color} turtle is won!")
        else:
            distance = random.randint(0, 10)
            turtle.forward(distance)


screen.exitonclick()