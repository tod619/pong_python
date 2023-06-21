# A game of Pong
# Created using the turtle graphics library in python
# 21/06/2023
from turtle import Screen, Turtle
from paddle import Paddle

# Set up the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Create the paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


# def go_up():
#     new_y = paddle.ycor() + 20
#     paddle.goto(paddle.xcor(), new_y)


# def go_down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(paddle.xcor(), new_y)


screen.listen()
# screen.onkey(go_up, "Up")
# screen.onkey(go_down, "Down")

game_is_on = True

while game_is_on:
    screen.update()


# Exit the screen on click
screen.exitonclick()
