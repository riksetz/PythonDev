# CSE1PE W4: Text Box
# 1 Error: Implement try-catch block

import pip
import math

while True:
    programname = "Box Font"
    print (f"\nWelcome to {programname}!\n")
    displaymode = input("Select Display Mode:\nEnter H for Horizontal\nEnter V for Vertical\n").lower()
    if displaymode != "h" and displaymode != "v":
        displaymode = input("\nError: Invalid Input\nEnter (H/V)\n").lower()
# Horizontal Font
    elif displaymode == "h":
        text_input = input("Enter a line of text:\n")
        horizontal_line = "+-" + "-" * len(text_input) + "-+"
        print (horizontal_line)
        print ("| " + text_input + " |")
        print (horizontal_line)
# Vertical Font
    elif displaymode == "v":
        text_input = input("Enter a line of text:\n")
        print ("+---+")
        for each_index in text_input:
            print ("| " + each_index + " |")
        print ("+---+\n")
# Restart program    
    restart = input(f"Run {programname} again: (Y/N)\n").lower()
    if restart != "y":
        print (f"Exited {programname}.\n") 
        break
    print(f"Restarting {programname}...\n")