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
all_states = data.Estado.to_list()
score = []
missing_states = []

game_on = True
while game_on:
    guess_states = screen.textinput(title=f"{len(score)}/27", prompt="What's another state's names? ").lower()
    if guess_states == "exit":
        for state in data.Estado:
            if state not in score:
                missing_states.append(state)
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("states_to_learn.csv")
        break
    for state in all_states:
        if state.lower() == guess_states:
            correct_state = data[data.Estado == state]
            dashboard.state_match(state, float(correct_state.x), float(correct_state.y))
            if state not in score:
                score.append(state)
