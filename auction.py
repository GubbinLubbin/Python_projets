def max_dict(dictionary):
    for i in dictionary:
        max=0
        if(dictionary[i]>max):
            max=dictionary[i]
            name=i
            return name,max
logo=('''

                         ___________
                         /        /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________/
                         `'-------'`''')
print(logo)
biddings={}
choice="yes"
while(choice=="yes"):
    name=input("Enter your name:")
    bid=int(input("Enter your bid amount in $:"))
    biddings[name]=bid
    choice=input("Enter yes if you want to bid else no:")
    if(choice.lower()=="yes"):
        print("\n"*100)
highest=max_dict(biddings)
name,amount=max_dict(biddings)
print(f"The winner is {name} with amount {amount}")
