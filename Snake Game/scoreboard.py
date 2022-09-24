from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        # OPEN data.txt file
        with open(file="data.txt") as data:
            self.higher_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.higher_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.higher_score:
            self.higher_score = self.score
            # WRITE the data into data.txt file
            with open(file="data.txt", mode="w") as data:
                data.write(f"{self.higher_score}")

        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAVE OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()



