# Function - Calculate amount of whole pizza slices each person receives. Distributed slices must be equal.
# Hi Prof Nibal, I have commented out code changes I made to add features to the program. Thanks! - Raquelle

# Program submitted in LMS ->
# slices = int(input("Enter the number of whole pizza slices:\n"))
# people = int(input("How many people will be at the party?\n"))
# X = str(slices//people)
# print (X + " per person")

# Edits: If-else statements, while loops, truth conditions

import math

def program_cutter():
    while True:
            try:
                slices = float(input("\nEnter the number of pizza slices:\n"))
                people = float(input("\nHow many people will be at the party?\n"))
                X = str(round(slices/people, 3))
                remainder = int(slices-float(X)*people)
                print ("\nEveryone can have " + X + " slice(s) of pizza.")
                print ("There should always be a remainder of " + str(remainder) + " slice(s) left.")
                break
            except ValueError:
                print("\nInvalid input. Please enter a valid number.")
                
def program_nocutter():
    while True:
        try:
            slices = int(input("\nEnter the number of whole pizza slices:\n"))
            people = int(input("\nHow many people will be at the party?\n"))
            X = str(slices//people)
            remainder = str(slices-int(X)*people)
            print ("\nEveryone can have " + X + " slice(s) of pizza.")
            print ("There will be a remainder of " + remainder + " slice(s) left.")
            break
        except ValueError:
            print("\nInvalid input. Please enter a valid number.")
     
def main():
    while True:
        print("\nWelcome to the Equal Pizza Divider Program!\n")
        while True:
            answer = input("Do you have a pizza cutter? (Yes/No): ").lower()
            if answer == "yes" or answer == "no":
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        if answer == "yes":
            program_cutter()
        else:
            program_nocutter()
        while True:
            restart = input("\nDo you want to restart the program? (Yes/No):\n").lower()
            if restart == "yes" or "no":
                break
            elif restart == "maybe":
                print("Ok, answer question after some thought.")
            else: 
                print("Invalid input. Please enter (Yes/No).")
        if restart != "yes":
            print("\nExiting the program.\nHave a nice day! :)")
            break
        print("\nRestarting the program...\n")

if __name__ == "__main__":
     main()