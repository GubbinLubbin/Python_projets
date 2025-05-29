#to make a game which gives number guess on easy and hard mode,in easy we get 5 attemps and on hard 3 and gives shit 
#to high,to low ,near !
import random
print("**********Welcome to the number guessing game**********")
diffi=input("Enter the difficulty level as hard and easy:")
if(diffi.lower()=="hard"):
    chances=5
if(diffi.lower()=="easy"):
    chances=10
number=random.randint(0,100)
while(chances!=0):
    guess=int(input("Enter the number between 1 and 100(including them ):"))
    if(guess==number):
        print("You win the number is",number)
        break
    if(guess>number):
        print("You are higher than the number")
    else:
        print("You are lower than the number")
    chances-=1
    if(chances>0):
        print(f"You still have {chances} chances to get it right.")
    else:
        print(f"You lose the number was {number}")