# A dice roller program:
import os
import random

def Clear_Screen():
    os.system("cls")

Validation = ("yes", "no")

while True:
    

    User_Choice = input("Do you want to roll the dice: (Yes/no): ").lower()
    Flag = True

    while User_Choice not in Validation:
        User_Choice = input("Do you want to roll the dice: (yes/no): ").lower()

    if User_Choice == "yes":
        
        while True:
            while True:
                try:
                    Size = int(input("How many sided die do you want to use? "))
                    break
                except:
                    print("Enter a valid integer value")
            if Size > 0:
                Roll_Choices = list(range(1, Size+1))
                break
            else:
                print("Please enter an integer value greater then 0")

        while True:
            while True:
                try:
                    Num_Of_Die = int(input(f"How many {Size} sided die do you want to use: "))
                    break
                except:
                    print("Enter a valid integer value")
            if Num_Of_Die > 0:
                width = len(str(Size))
                rolls = [f"{random.choice(Roll_Choices):0{width}}" for _ in range(Num_Of_Die)]
                print(", ".join(rolls))
                break
            else:
                print("Enter an integer value greater then 0")
    else: 
        Exiting = input("Are you sure you want to exit this program? (yes/no) ").lower()
        if Exiting == "yes":
            break
        
    
    print()

    while Flag == True:
        Screen = input("Do you want to clear the screen or no? (y/n) or (yes/no): ").lower()
        if Screen == "y" or Screen == "yes":
            Clear_Screen()
            Flag = False
        elif Screen == "n" or Screen =="no":
            print("Your terminal wont be cleared", end = "\r")
            Flag = False
        else:
            print("Please only enter yes/y or no/n as your input: ", end = "\r")    
