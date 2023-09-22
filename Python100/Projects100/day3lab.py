# Udemy Day 3 Lab: Monday 04/09/2023. 1:20 pm.
# Topic: Control flow and logical operators.
import math

while True:
    programname = "Roller Coaster"
    print (f"\nWelcome to {programname}!\n")
    print (f"To ride the {programname} you must be at least (x) tall.\n")
    
    bill = 0
    height = int(input("How tall are you in cm?\n"))
    if height >= 120:
        print("You can ride the rollercoaster.")
        age = int(input("What is your age?\n"))
        if age >= 45 and age <= 55:
            print("Mid-life crisis, enjoy the free ride. Ticket: $0.")
        elif age >= 18: 
            bill = bill + 10
            print("Adult ticket: $10.")
        elif age < 5:
            print("Underaged person. Ride unavailable.")
        else:
            bill = bill + 5
            print("Children ticket: $5.")
        
        photo = input("Do you want a photo taken?\n")
        if photo == "y".lower():
            bill += 3   # Same as bill = bill + 3
            # bill = bill + 3
        print(f"Your bill is ${bill}.")
    else:
        print("Sorry, you have to grow taller before you can ride.")
    
    restart = input(f"Run {programname} again: (Y/N)\n").lower()
    if restart != "y":
        print (f"Exited {programname}.\n") 
        break
    print(f"Restarting {programname}...\n")