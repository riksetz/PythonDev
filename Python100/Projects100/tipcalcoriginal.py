# Tip Calculator: Udemy Day 2 Project
# Math shortcut: 
# If the bill was $150.00, split between 5 people, with 12% tip. 
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# 12% of 150 = 18, instead of adding tip total to bill, multiply with + 1 (*1.<percent>), this is the same as adding intital bill.
# $150 = 100% = 100/100 = 1, $18 = 12%, 12/100 = 0.12.
# Use stucture as general program template. 

import math

while True:
    programname = "Tip Calculator"
    print (f"\nWelcome to {programname}!\n")

    bill = float(input(f"What was the total bill? $"))
    tip = int(input(f"What percentage tip would you like to give: 10, 12, or 15?\n"))
    people = int(input("How many poeple split the bill? "))

    finalbill = round((1 + (tip / 100))* bill / people,2)
    displaybill = "{:.2f}".format(finalbill)

    print(f"Each person should pay: ${displaybill}.\n")

    restart = input(f"Run {programname} again: (Y/N)\n").lower()
    if restart != "y":
        print (f"Exited {programname}.\n")
        break
    print(f"Restarting {programname}...\n")
