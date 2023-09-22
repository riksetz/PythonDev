# Used as a template to test program

import math

while True:
    programname = "Odd or Even"
    print (f"\nWelcome to {programname}!\n")
    print ("Even numbers can be divided by 2 with no remainder.\n")

    number = int(input("Enter a number:\n"))
    if number%2 == 0:
        print(f"This is an even number.")
    else:
        print(f"This is an odd number.\n")

    restart = input(f"Run {programname} again: (Y/N)\n").lower()
    if restart != "y":
        print (f"Exited {programname}.\n") 
        break
    print(f"Restarting {programname}...\n")