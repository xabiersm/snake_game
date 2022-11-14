from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 270)
        self.pencolor("white")
        self.score = 0
        # self.high_score = 0
        with open("high_score.txt") as data:
            self.high_score = int(data.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score {self.score} High score {self.high_score}", align=ALIGNMENT, font=FONT)
        with open("high_score.txt", mode="w") as data:
            data.write(str(self.high_score))

    def increase(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

#    def game_over(self):
#        self.goto(0, 0)
#        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
