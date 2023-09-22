# Tip Calculator
# If the bill was $150.00, split between 5 people, with 12% tip. 
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

import math

while True:
    programname = "Bill Calculator"
    print(f"\nWelcome to {programname}!\n")

    people = input("How many people would you like to split the bill with?\n")
    bill = input("Enter the bill amount:\n    $")
    tip = input("Add Tip: (Yes/No)\n").lower()
    if tip == "yes":
        while True:
                tipmethod = input("Select tip method: (Percent/Manual)\n").lower()
                if tipmethod != "percent" and tipmethod !="manual":
                    print ("Error: Invlaid response, please enter (Percent/Manual).")     
                elif tipmethod == "percent":
                    tippercent = float(float(input("Enter tip percentage:\n    "))/100.0)
                    tippp = float(bill)/float(people)*tippercent
                    print(f"Tip amount of ${tippp} will be added for each person.")
                elif tipmethod == "manual":
                    tipmanual = float(float(input("Enter tip amount:    $ \n"))/float(people))
                    tippp = float(bill)/float(people)+tipmanual
                    print(f"Tip amount of ${tippp} will be added for each person.")
                break
    else:
        tippp = 0.00
    billpp = float(bill)/float(people)
    totalbill = float(bill)
    amountdue = billpp + tippp
    print (f"\nBILL CALCULATION PER PERSON\n")
    print (f"\n    Total Bill: $ {totalbill}\n    Split Bill: $ {billpp} \n    Tip: $ {tippp}\n    Amount Due: $ {amountdue}")
    if tippp > 0.00:
        print ("\nThanks for tipping! :)\n")
    else:
        print ("\nNo tip added.\n")
        
    restart = input(f"Run {programname} again: (Yes/No)\n").lower()
    if restart != "yes":
        print(f"Exited {programname}.\n")
        break
    print(f"Restarting {programname}...\n")