from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height= 400)
user_guess = screen.textinput("Let's race!", "Who is the winner? Enter a colour: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = -125
all_turtles = []
is_race_on = False

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-200, y_position)
    y_position += 50
    all_turtles.append(new_turtle)
if user_guess:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_guess == winning_color:
                print("Congratulations, You've won!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(1,10)
        turtle.forward(random_distance)


screen.exitonclick()