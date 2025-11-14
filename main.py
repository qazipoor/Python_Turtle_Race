import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
gap_between_turtles = 40
x_pos = -screen.window_width() / 2 + 50
y_pos = -screen.window_height() / 2 + 100
speeds = [5, 10, 30]
end_of_game = False

turtles = []
for i in range(len(colors)):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(x=x_pos, y=y_pos + float(i * gap_between_turtles))
    turtles.append(turtle)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")


while not end_of_game:
    for turtle in turtles:

        if turtle.xcor() >= (screen.window_width() / 2) - 30:
            if user_bet == turtle.pencolor():
                print(f"You won! the winner is {turtle.pencolor()}")
            else:
                print(f"You lose. the winner is {turtle.pencolor()}")

            end_of_game = True
            break
        else:
            turtle.forward(random.choice(speeds))



screen.exitonclick()


