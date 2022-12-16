from turtle import Turtle, Screen
import pandas
from dashboard import Dashboard


turtle = Turtle()
screen = Screen()
screen.setup(800, 650)
screen.title("Brazil States Game")
image = "map_states.gif"
screen.addshape(image)
turtle.shape(image)

dashboard = Dashboard()
data = pandas.read_csv("list_states.csv")
score = 0

game_on = True
while game_on:
    guess_states = screen.textinput(title=f"{score}/27", prompt="What's another state's names? ").lower()

    for state in data.Estado:
        if state.lower() == guess_states:
            correct_state = data[data.Estado == state]
            dashboard.state_match(state, float(correct_state.x), float(correct_state.y))
            score += 1


screen.exitonclick()
