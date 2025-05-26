def addition(a,b):
    return a+b
def multiplication(a,b):
    return a*b
def subtraction(a,b):
    return a-b
def division(a,b):
    return a/b
calc='''
 _____________________
|  _________________  |
| |              0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | ÷ | |
| |___|___|___| |___| |
|_____________________|
'''
operation={
    "+":addition,
    "-":subtraction,
    "/":division,
    "*":multiplication
}
choice="y"
num1=float(input("Enter the first number:"))
for i in operation:
        print(i)
result=num1
while (choice == "y"):
    num1=result
    operation_choice=input("Enter the operation of your choice:")
    num2=float(input("Enter the second number:"))
    result=operation[operation_choice](num1,num2)
    print(f"{num1}{operation_choice}{num2}={result}")
    choice=input("Enter y if you want to continue else n:")
print("Thanks for using our calculator:)")

