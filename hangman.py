word_list=word_list = [
    "PYTHON", "HANGMAN", "COMPUTER", "PROGRAM", "SEXY", "KEYBOARD", "FUNCTION", "VARIABLE", "ALGORITHM",
    "NETWORK", "INTERNET", "DATABASE", "PYRAMID", "ELEPHANT", "GIRAFFE", "KANGAROO", "CROCODILE", "ZEBRA", "LION",
    "TIGER", "JUNGLE", "BANANA", "MANGO", "PINEAPPLE", "STRAWBERRY", "AVOCADO", "PEACH", "CHERRY", "ORANGE",
    "WIZARD", "CASTLE", "DRAGON", "MAGICIAN", "POTION", "SWORD", "SHIELD", "KNIGHT", "VIKING", "PIRATE",
    "TREASURE", "ISLAND", "OCEAN", "SAILOR", "ANCHOR", "STORM", "BATTLE", "FIRE", "EARTH", "WATER", "WIND",
    "PLANET", "GALAXY", "UNIVERSE", "SATELLITE", "SPACESHIP", "ASTEROID", "COMET", "ROCKET", "ALIEN", "GRAVITY",
    "LIGHTNING", "THUNDER", "TORNADO", "EARTHQUAKE", "VOLCANO", "HURRICANE", "CYCLONE", "WEATHER", "FORECAST",
    "MOUNTAIN", "VALLEY", "FOREST", "RIVER", "LAKE", "DESERT", "ISLAND", "GLACIER", "CANYON", "PEAK",
    "PYJAMA", "GUITAR", "PIANO", "VIOLIN", "TRUMPET", "MUSICIAN", "ORCHESTRA", "CONCERT", "OPERA", "BALLET",
    "PAINTER", "SCULPTOR", "ACTOR", "DIRECTOR", "CINEMA", "THEATER", "SCRIPT", "DIALOGUE", "CAMERA", "LENS"
]

n=6
import random
to_print=""
choosen_word=random.choice(word_list)
store=choosen_word
for i in range(len(choosen_word)):
    to_print+="_"
print(to_print)
while(n>0):
    print(f'You have {n} options')
    guess=input("Guess a letter:").upper()
    if(guess in choosen_word):
        part=choosen_word.index(guess)
        to_print=to_print[:part]+guess+to_print[part+1:]
        choosen_word=choosen_word[:part]+"_"+choosen_word[part+1:]
        print(to_print)
        if(store==to_print):
            print("**************you won******************")
            break
    else:
        n-=1
        print(to_print)
        if(n==0):
            print("************You lost*************")
            print(f"The word was {store}")
