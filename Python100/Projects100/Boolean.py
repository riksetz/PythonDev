# CSE1PE Week 3: Booleans
#
import math

while True:
    programname = "ISBN"
    #print (f"\nWelcome to {programname}!\n")
    #print ("Even numbers can be divided by 2 with no remainder.\n")

    ISBN = int(input("Enter the ISBN number:\n"))
    if len(str(ISBN)) == 13:
        ISBN = ISBN - 9780000000000
    else:
        ISBN = ISBN
    if ISBN <= 1999999999:
        print ("English")
    elif ISBN >= 2000000000 and ISBN < 3000000000:
        print ("French")
    elif ISBN >= 3000000000 and ISBN < 4000000000:
        print("German")
    else:
        ISBN >= 4000000000
        print ("Unknown")   
    restart = input(f"Run {programname} again: (Y/N)\n").lower()
    if restart != "y":
        print (f"Exited {programname}.\n") 
        break
    print(f"Restarting {programname}...\n")