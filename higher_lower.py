import random
print("*******Higher Lower game**********")
score=0
print("Comparing instagram followrs of top 75 people/businesses of instagram:")
top_instagram_accounts = [
    {"rank": 1, "username": "instagram", "followers_millions": 689},
    {"rank": 2, "username": "cristiano", "followers_millions": 654},
    {"rank": 3, "username": "leomessi", "followers_millions": 505},
    {"rank": 4, "username": "selenagomez", "followers_millions": 420},
    {"rank": 5, "username": "therock", "followers_millions": 394},
    {"rank": 6, "username": "kyliejenner", "followers_millions": 394},
    {"rank": 7, "username": "arianagrande", "followers_millions": 376},
    {"rank": 8, "username": "kimkardashian", "followers_millions": 356},
    {"rank": 9, "username": "beyonce", "followers_millions": 311},
    {"rank": 10, "username": "khloekardashian", "followers_millions": 303},
    {"rank": 11, "username": "nike", "followers_millions": 301},
    {"rank": 12, "username": "justinbieber", "followers_millions": 294},
    {"rank": 13, "username": "kendalljenner", "followers_millions": 288},
    {"rank": 14, "username": "taylorswift", "followers_millions": 282},
    {"rank": 15, "username": "natgeo", "followers_millions": 279},
    {"rank": 16, "username": "virat.kohli", "followers_millions": 272},
    {"rank": 17, "username": "jlo", "followers_millions": 249},
    {"rank": 18, "username": "neymarjr", "followers_millions": 229},
    {"rank": 19, "username": "nickiminaj", "followers_millions": 226},
    {"rank": 20, "username": "kourtneykardash", "followers_millions": 219},
    {"rank": 21, "username": "mileycyrus", "followers_millions": 213},
    {"rank": 22, "username": "katyperry", "followers_millions": 204},
    {"rank": 23, "username": "zendaya", "followers_millions": 179},
    {"rank": 24, "username": "kevinhart4real", "followers_millions": 177},
    {"rank": 25, "username": "realmadrid", "followers_millions": 173},
    {"rank": 26, "username": "iamcardib", "followers_millions": 164},
    {"rank": 27, "username": "kingjames", "followers_millions": 159},
    {"rank": 28, "username": "ddlovato", "followers_millions": 153},
    {"rank": 29, "username": "badgalriri", "followers_millions": 149},
    {"rank": 30, "username": "chrisbrownofficial", "followers_millions": 144},
    {"rank": 31, "username": "champagnepapi", "followers_millions": 143},
    {"rank": 32, "username": "theellenshow", "followers_millions": 136},
    {"rank": 33, "username": "fcbarcelona", "followers_millions": 136},
    {"rank": 34, "username": "billieeilish", "followers_millions": 124},
    {"rank": 35, "username": "k.mbappe", "followers_millions": 123},
    {"rank": 36, "username": "uefachampionsleague", "followers_millions": 120},
    {"rank": 37, "username": "gal_gadot", "followers_millions": 108},
    {"rank": 38, "username": "lalalalisa_m", "followers_millions": 105},
    {"rank": 39, "username": "vindiesel", "followers_millions": 103},
    {"rank": 40, "username": "nasa", "followers_millions": 96.8},
    {"rank": 41, "username": "shraddhakapoor", "followers_millions": 94.2},
    {"rank": 42, "username": "narendramodi", "followers_millions": 92.8},
    {"rank": 43, "username": "priyankachopra", "followers_millions": 92.4},
    {"rank": 44, "username": "shakira", "followers_millions": 91.8},
    {"rank": 45, "username": "nba", "followers_millions": 90.5},
    {"rank": 46, "username": "snoopdogg", "followers_millions": 88.4},
    {"rank": 47, "username": "davidbeckham", "followers_millions": 88.1},
    {"rank": 48, "username": "dualipa", "followers_millions": 87.4},
    {"rank": 49, "username": "jennierubyjane", "followers_millions": 87.1},
    {"rank": 50, "username": "aliaabhatt", "followers_millions": 86.3},
    {"rank": 51, "username": "gigihadid", "followers_millions": 85.2},
    {"rank": 52, "username": "deepikapadukone", "followers_millions": 84.7},
    {"rank": 53, "username": "khaby00", "followers_millions": 83.9},
    {"rank": 54, "username": "shawnmendes", "followers_millions": 83.2},
    {"rank": 55, "username": "emilyratakowski", "followers_millions": 82.6},
    {"rank": 56, "username": "ronaldinho", "followers_millions": 82.1},
    {"rank": 57, "username": "katrinakaif", "followers_millions": 81.4},
    {"rank": 58, "username": "neha_kakkar", "followers_millions": 80.7},
    {"rank": 59, "username": "emwatson", "followers_millions": 80.1},
    {"rank": 60, "username": "anushkasharma", "followers_millions": 79.5},
    {"rank": 61, "username": "zayn", "followers_millions": 78.9},
    {"rank": 62, "username": "parineetichopra", "followers_millions": 78.3},
    {"rank": 63, "username": "jacquelinef143", "followers_millions": 77.6},
    {"rank": 64, "username": "kritisanon", "followers_millions": 77.0},
    {"rank": 65, "username": "karanjohar", "followers_millions": 76.4},
    {"rank": 66, "username": "sidharthmalhotra", "followers_millions": 75.8},
    {"rank": 67, "username": "varundvn", "followers_millions": 75.2},
    {"rank": 68, "username": "ranveersingh", "followers_millions": 74.6},
    {"rank": 69, "username": "tigerjackieshroff", "followers_millions": 74.0},
    {"rank": 70, "username": "dishapatani", "followers_millions": 73.4},
    {"rank": 71, "username": "saraalikhan95", "followers_millions": 72.8},
    {"rank": 72, "username": "kartikaaryan", "followers_millions": 72.2},
    {"rank": 73, "username": "vickykaushal09", "followers_millions": 71.6},
    {"rank": 74, "username": "kiaraaliaadvani", "followers_millions": 71.0},
    {"rank": 75, "username": "taapsee", "followers_millions": 70.4}]
game_over=False
while not game_over:
    choice1 = random.randint(0, 74)
    choice2 = random.randint(0, 74)
    while choice2 == choice1:
        choice2 = random.randint(0, 74)

    account1 = top_instagram_accounts[choice1]
    account2 = top_instagram_accounts[choice2]

    print(f"\nWho do you think has more followers?")
    print(f"1. @{account1['username']}")
    print(f"2. @{account2['username']}")

    while True:
        try:
            pick = int(input("Pick between 1 and 2: "))
            if pick not in [1, 2]:
                print("Please enter 1 or 2.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")

    if (pick == 1 and account1["followers_millions"] > account2["followers_millions"]) or \
       (pick == 2 and account2["followers_millions"] > account1["followers_millions"]):
        score += 1
        print(f"You win! Your score is {score}.")
        print(f"{account1['username']} has {account1['followers_millions']} million followers.")
        print(f"{account2['username']} has {account2['followers_millions']} million followers.")
        con = input("Type 'y' to play again or 'n' to quit: ").lower()
        if con == "n":
            game_over = True
    else:
        print(f"{account1['username']} has {account1['followers_millions']} million followers.")
        print(f"{account2['username']} has {account2['followers_millions']} million followers.")
        print("You lose. Try again!")
        game_over = True