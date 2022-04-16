from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score =int(data.read())

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.refresh()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.refresh()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("game over", move=False, align="center", font=("Aerial", 20, "normal"))

    def refresh(self):
        self.clear()
        self.write(f"score board: {self.score} High score: {self.high_score}", move=False, align="center", font=("Aerial", 20, "normal"))





