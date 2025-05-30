#"Available commands:"
#'report': View current ingredients
 #'money': View total money collected
#'refill': Refill ingredients
#'stop': Turn off the machine
Menu = {
    "Espresso": {
        "Ingredients": {"Water": 50, "Coffee": 18, "Milk": 0},
        "Money": 1.5
    },
    "Latte": {
        "Ingredients": {"Water": 200, "Milk": 150, "Coffee": 24},
        "Money": 2.5
    },
    "Cappuccino": {
        "Ingredients": {"Water": 250, "Milk": 100, "Coffee": 24},
        "Money": 3.0
    }
}

Resources = {
    "Ingredients": {"Water": 1000, "Milk": 500, "Coffee": 250}
}

money = 0

def make_coffee(Type):
    global Resources
    ingredients = Menu[Type]["Ingredients"]
    for item in ingredients:
        if Resources["Ingredients"].get(item, 0) < ingredients[item]:
            print(f"Insufficient {item}")
            return False
    for item in ingredients:
        Resources["Ingredients"][item] -= ingredients[item]
    print("Making coffee... please wait...")
    print(f"{Type} is ready! ☕ Enjoy!\n")
    return True

def count_money(current_money, Type):
    return current_money + Menu[Type]["Money"]

Run = True

while Run:
    choice = input('''
Enter what you want (1, 2, 3):
1. Espresso
2. Latte
3. Cappuccino
''').strip().lower()

    if choice == "stop":
        Run = False

    elif choice == "refill":
        add = True
        while add:
            add_water = int(input("How much water to add (ml): "))
            Resources["Ingredients"]["Water"] += add_water
            add_milk = int(input("How much milk to add (ml): "))
            Resources["Ingredients"]["Milk"] += add_milk
            add_coffee = int(input("How much coffee to add (mg): "))
            Resources["Ingredients"]["Coffee"] += add_coffee
            print("Thanks for refilling!")
            more = input("Type 'y' to refill more: ")
            if more != "y":
                print("\n" * 20)
                add = False

    elif choice == "report":
        print("\nCurrent Resources:")
        for k, v in Resources["Ingredients"].items():
            print(f"{k}: {v}")
        input("Press Enter to continue...")
        print("\n" * 20)

    elif choice == "help":
        print("Available commands:")
        print("- 'report': View current ingredients")
        print("- 'money': View total money collected")
        print("- 'refill': Refill ingredients")
        print("- 'stop': Turn off the machine")
        input("Press Enter to continue...")
        print("\n" * 20)

    elif choice == "money":
        print(f"Money collected: ${money}")
        input("Press Enter to continue...")
        print("\n" * 20)

    elif choice == "1":
        if make_coffee("Espresso"):
            money = count_money(money, "Espresso")
        input("Press Enter to continue...")
        print("\n" * 20)

    elif choice == "2":
        if make_coffee("Latte"):
            money = count_money(money, "Latte")
        input("Press Enter to continue...")
        print("\n" * 20)

    elif choice == "3":
        if make_coffee("Cappuccino"):
            money = count_money(money, "Cappuccino")
        input("Press Enter to continue...")
        print("\n" * 20)

    else:
        print("Invalid input. Try again.")
