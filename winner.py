from turtle import Turtle

class Winner(Turtle):
    def __init__(self):
        super().__init__()
        self.one_score = 0
        self.two_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score_board()

    def score_board(self):
        self.clear()
        self.goto(100,280)
        self.write(self.one_score, font=("Arial", 50, "bold"))
        self.goto(-100,280)
        self.write(self.two_score, font=("Arial", 50, "bold"))

    def score_one(self):
        self.one_score += 1
        self.score_board()


    def score_two(self):
        self.two_score +=1
        self.score_board()




