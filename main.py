import time
import turtle
from turtle import Screen
from paddle import Paddles
from ball import Ball
from winner import Winner

# Setup screen
screen = Screen()
screen.setup(height=750, width=1000)  # Set screen size
screen.bgcolor("black")  # Set background color
screen.title("Ping Pong")  # Game title
turtle.tracer(0)  # Disable automatic screen updates

# Create paddles
paddle_one = Paddles()  # Left paddle
paddle_one.creat_paddle(460, 0)  # Position left paddle

paddle_two = Paddles()  # Right paddle
paddle_two.creat_paddle(-460, 0)  # Position right paddle

# Keyboard bindings
screen.listen()
screen.onkeypress(fun=paddle_one.up, key="Up")  # Move left paddle up
screen.onkeypress(fun=paddle_one.down, key="Down")  # Move left paddle down
screen.onkeypress(fun=paddle_two.up, key="w")  # Move right paddle up
screen.onkeypress(fun=paddle_two.down, key="s")  # Move right paddle down

# Create ball
ball = Ball(0, 0)

# Scoreboard
winner = Winner()

# Game loop
is_on_game = True
while is_on_game:
    screen.update()  # Update the screen
    time.sleep(ball.move_speed)  # Control ball speed
    ball.move()  # Move the ball

    # Check for wall collisions
    if ball.ycor() > 350 or ball.ycor() < -325:
        ball.bounce_y()  # Bounce the ball vertically

    # Check for paddle collisions
    if (ball.distance(paddle_one) < 50 and ball.xcor() > 430) or (ball.distance(paddle_two) < 50 and ball.xcor() < -430):
        ball.bounce_x()  # Bounce the ball horizontally

    # Score check
    if ball.xcor() > 500:  # Right side score
        ball.rest_position()  # Reset ball
        winner.score_two()  # Player 2 scores

    if ball.xcor() < -500:  # Left side score
        ball.rest_position()  # Reset ball
        winner.score_one()  # Player 1 scores

screen.mainloop()  # Keep the window open
