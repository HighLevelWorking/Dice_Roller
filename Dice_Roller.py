# A dice roller program:
import os
import random

def Clear_Screen():
    os.system("cls")



Roll_Choices = (1, 2, 3, 4, 5, 6)

Validation = ("yes", "no")

while True:
    

    User_Choice = input("Do you want to roll the dice: (Yes/no): ").lower()
    Flag = True

    while User_Choice not in Validation:
        User_Choice = input("Do you want to roll the dice: (yes/no): ").lower()

    if User_Choice == "yes":
        Num_Of_Die = int(input("How many 6 sided die do you want to use: "))
        for i in range (0, Num_Of_Die):
            Roll_Choice = random.choice(Roll_Choices)
            print(f"{Roll_Choice: >2}", end = ", ")
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
