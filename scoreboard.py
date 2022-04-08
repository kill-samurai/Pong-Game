from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player_1_score = 0
        self.player_2_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 190)
        self.write(self.player_1_score, align="center", font=("Courier", 80, "bold"))
        self.goto(100, 190)
        self.write(self.player_2_score, align="center", font=("Courier", 80, "bold"))


    def player_1_scores(self):
        self.player_1_score += 1
        self.update_scoreboard()


    def player_2_scores(self):
        self.player_2_score += 1
        self.update_scoreboard()
