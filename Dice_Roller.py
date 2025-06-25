# A dice roller program:
import os
import random

def Clear_Screen():
    os.system("cls")

Roll_Choices = (1, 2, 3, 4, 5, 6)

Validation = ("yes", "no")

while True:
    Screen = input("Do you want to clear the screen or no? (y/n): ").lower()

    if Screen == "y":
        Clear_Screen()

    User_Choice = input("Do you want to roll the dice: (Yes/no): ").lower()

    while User_Choice not in Validation:
        User_Choice = input("Do you want to roll the dice: (yes/no): ").lower()

    if User_Choice == "yes":
        Roll_Choice = random.choice(Roll_Choices)
        print(Roll_Choice)
    else: 
        break

