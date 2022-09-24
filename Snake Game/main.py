from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from boarder import Boarder
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
# Ask for level difficulty
user_input = screen.textinput("Chose Level", "Choose: EASY or HARD").lower()
# Tracer is used to turn on or off of the animation
screen.tracer(0)
# Create red boarder into the screen
boarder = Boarder()
# Create snake from snake class
snake = Snake()
# Create snake food
food = Food()
# Create scoreboard
scoreboard = Scoreboard()

# Create event listener using arrow keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# snake movement
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect the collision with boarder
    if user_input == "easy":
        if snake.head.xcor() > 270:
            snake.head.setx(-270)
        if snake.head.xcor() < -270:
            snake.head.setx(270)
        if snake.head.ycor() > 270:
            snake.head.sety(-270)
        if snake.head.ycor() < -270:
            snake.head.sety(270)
    elif user_input == "hard":
        if snake.head.xcor() > 270 or snake.head.xcor() < -270 or snake.head.ycor() > 270 or snake.head.ycor() < -270:
            scoreboard.reset()
            snake.reset()
    else:
        screen.bye()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
