import random
from turtle import Turtle,Screen
message_turtle = Turtle()
message_turtle.hideturtle()
message_turtle.penup()
message_turtle.goto(0, 0) 
message_turtle.color("white") 
is_race_on=True
participants={"tim":"red","tommy":"pink","timmy":"yellow","tina":"purple","tuna":"blue"}
screen=Screen()
user_bet=screen.textinput(title="Make your bet:",prompt="Which colour do you think is gonna win red,pink,yellow,purple,blue")
screen.setup(600,600)
screen.title("Freaking race game")
screen.bgcolor("Black")
cordinates=[(-280,0),(-280,120),(-280,240),(-280,-120),(-280,-240)]
racers=[]
for name,cor in zip(participants,cordinates):
    turtle=Turtle()
    turtle.shape("turtle")
    turtle.color(participants[name])
    turtle.penup()
    turtle.goto(cor)
    racers.append(turtle)
while is_race_on:
    for turtles in racers:
        randomdistance=random.randint(1,10)
        turtles.forward(randomdistance)
        if(turtles.xcor()>280):
            is_race_on=False
            winner=turtles.pencolor()
            if user_bet.lower() == winner.lower():
                message_turtle.write(" You Won! ")
            else:
                message_turtle.write(" You Lost!")
screen.exitonclick()

