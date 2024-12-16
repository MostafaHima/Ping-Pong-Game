import turtle
from turtle import Turtle


class Paddles(Turtle):
    def __init__(self):
        super().__init__()

    def creat_paddle(self, x, y):
        """Create and position the paddle."""
        self.shape("square")  # Set the paddle shape
        self.color("white")  # Set the paddle color
        self.shapesize(stretch_wid=5, stretch_len=1)  # Set paddle size
        self.penup()  # Prevent drawing lines
        self.goto(x, y)  # Position the paddle

    def up(self):
        """Move the paddle up."""
        new_y = self.ycor() + 20  # Move up by 20 units
        self.goto(self.xcor(), new_y)  # Update the position

    def down(self):
        """Move the paddle down."""
        new_y = self.ycor() - 20  # Move down by 20 units
        self.goto(self.xcor(), new_y)  # Update the position





