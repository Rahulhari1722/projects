# import turtle package 
import turtle 

score_a = 0
score_b = 0

# making turtle object 
win = turtle.Screen() 

# setup the screen size 
win.setup(800, 600) 
win.tracer(0)
# set the background color 
win.bgcolor("blue") 
win.title("Pong Game")

# left paddle
left_paddle = turtle.Turtle()
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.speed(0)
left_paddle.goto(-380, 0)

# right paddle
right_paddle = turtle.Turtle()
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.speed(0)
right_paddle.goto(380, 0)

# ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.dy = 0.15
ball.dx = 0.15

# score display
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))
pen.hideturtle()

# moving paddle
def left_paddle_up():
    y = left_paddle.ycor()
    if y < 250:  # Prevent going out of bounds
        left_paddle.sety(y + 20)

def left_paddle_down():
    y = left_paddle.ycor()
    if y > -240:  # Prevent going out of bounds
        left_paddle.sety(y - 20)

def right_paddle_up():
    y = right_paddle.ycor()
    if y < 250:  # Prevent going out of bounds
        right_paddle.sety(y + 20)

def right_paddle_down():
    y = right_paddle.ycor()
    if y > -240:  # Prevent going out of bounds
        right_paddle.sety(y - 20)

win.listen()
win.onkeypress(left_paddle_up, 'w')
win.onkeypress(left_paddle_down, 's')
win.onkeypress(right_paddle_up, 'Up') 
win.onkeypress(right_paddle_down, 'Down')

while True:
    win.update()
    
    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # ball collision with top
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    # ball collision with bottom
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # ball collision with left wall
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
        score_b+=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))

    # ball collision with right wall
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
        score_a+=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))
    # collision with right paddle
    if (360 < ball.xcor() < 370) and (right_paddle.ycor() - 50 < ball.ycor() < right_paddle.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1

    # collision with left paddle
    if (-370 < ball.xcor() < -360) and (left_paddle.ycor() - 50 < ball.ycor() < left_paddle.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1