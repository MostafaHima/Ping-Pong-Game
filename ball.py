from turtle import Turtle
import random

POSITIONS = [5, 5]

class Ball(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.score = 0  # Initialize score
        self.segments = []  # List to store ball's trail positions
        self.shape("circle")  # Set ball shape
        self.shapesize(stretch_wid=1, stretch_len=1)  # Set ball size
        self.color("white")  # Set ball color
        self.penup()  # Prevent drawing lines
        self.goto(x, y)  # Position the ball
        self.x_cor = 10  # Set horizontal speed
        self.y_cor = 10  # Set vertical speed
        self.move_speed = 0.1  # Set ball speed

    def move(self):
        """Move the ball to the next position."""
        new_x = self.xcor() + self.x_cor  # Update X position
        new_y = self.ycor() + self.y_cor  # Update Y position
        self.teleport(new_x, new_y)  # Move the ball to the new position
        self.segments.append(self.position)  # Add the new position to the trail

    def bounce_y(self):
        """Reverse the vertical direction of the ball."""
        self.y_cor *= -1  # Reverse vertical movement

    def bounce_x(self):
        """Reverse the horizontal direction and speed up the ball."""
        self.x_cor *= -1  # Reverse horizontal movement
        self.move_speed *= 0.9  # Increase ball speed

    def rest_position(self):
        """Reset the ball to the center and reverse its direction."""
        self.goto(0, 0)  # Move the ball to the center
        self.move_speed = 0.1  # Reset speed
        self.bounce_x()  # Reverse the horizontal direction to restart
