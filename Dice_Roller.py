# A dice roller program:
import os
import random

def Clear_Screen():
    os.system("cls")

Roll_Choices = (1, 2, 3, 4, 5, 6)

Roll_Choice = random.choice(Roll_Choices)

Validation = ("yes", "No")

User_Choice = input("Do you want to roll the dice: (Yes/no): ")
while User_Choice not in Validation:
    User_Choice = input("Do you want to roll the dice: (yes/no): ").lower()
Clear_Screen()
