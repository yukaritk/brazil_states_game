from turtle import Turtle, Screen
import pandas

turtle = Turtle()
screen = Screen()
screen.setup(800, 650)
screen.title("Brazil States Game")
image = "map_states.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("list_states.csv")
print(data)

screen.exitonclick()
