from turtle import Turtle


class Dashboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def state_match(self, state_name, pos_x, pos_y):
        self.goto(pos_x, pos_y)
        self.write(f"{state_name}", align="center", font=("Arial", 12, "normal"))
