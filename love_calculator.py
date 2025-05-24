def calculate_love_score(name1, name2):
    true=0
    love=0
    for i in range(len(name1.lower())):
        if (name1[i] in "true"):
            true += 1
        if (name1[i] in "love"):
            love += 1
    for i in range(len(name2.lower())):
        if (name2[i] in "true"):
            true += 1
        if (name2[i] in "love"):
            love += 1
    return (str(true) + str(love))


your_name = input("Enter your name:")
soulmate_name = input("Enter your soulmate name:")
score = calculate_love_score(your_name, soulmate_name)
print("This is just a stupid calculation,there no calculation for your relation immense love but whatever it is:")
print(score)
