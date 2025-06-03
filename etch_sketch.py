from turtle import Turtle,Screen
screen=Screen()
tim=Turtle()
tim.shape("turtle")
tim.color("red")
tim.speed(5)
tim.pensize(5)
def move_forward():
    tim.forward(5)
def move_backward():
    tim.backward(5)
def turn_left():
    tim.left(5)
def turn_right():
    tim.right(5)
def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
screen.listen()
screen.onkey(move_forward,"d")
screen.listen()
screen.onkey(move_backward,"a")
screen.listen()
screen.onkey(turn_right,"x")
screen.listen()
screen.onkey(turn_left,"w")
screen.listen()
screen.onkey(clear_screen,"s")
screen.exitonclick()

