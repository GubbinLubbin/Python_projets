import random
from turtle import Turtle,Screen
is_race_on=False
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet:",prompt="Enter which color do you think gonna win the race:")
turtles=["timmy",'tommy','tom','tim',"lumber"]
colors=["red",'orange','blue','purple','black']
y_axis=180
all_turtles=[]
for i,j in zip(turtles,colors):
    i=Turtle()
    i.shape("turtle")
    i.color(j)
    i.pensize(5)
    i.penup()
    i.goto(x=-220,y=y_axis)
    y_axis=y_axis-80
    all_turtles.append(i)
if user_bet:
    is_race_on=True
while is_race_on:
    for turtle in all_turtles:
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)
        if(turtle.xcor()>200):
            winner_color=turtle.pencolor()
            is_race_on=False
            result_writer = Turtle()
            result_writer.hideturtle()
            result_writer.penup()
            result_writer.goto(0, 0)
            result_writer.color("green" if winner_color == user_bet else "red")
            message = "You won! 🎉" if winner_color == user_bet else f"You lost. 😞 The winner was {winner_color}."
            result_writer.write(message, align="center", font=("Arial", 16, "bold"))
screen.exitonclick()
