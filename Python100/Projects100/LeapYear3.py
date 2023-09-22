# Leap Year - Day 3 project. Date: Monday, 04/09/2023. 2:54 pm.

import math

year = int(input("Which year do you want to check? "))

var1 = year % 4.0 # True - if % = 0
var2 = year % 100.0    # False - if % = 0, unless var3 is true 
var3 = year % 400.0 # True - if % = 0
# leapyear = bool
if var1 == 0.0:
    if var2 == 0.0 and var3 == 0.0:
        leapyear = True
    elif var2 == 0.0 and var3 != 0.0:
        leapyear = False
    else:
        leapyear = True
else:
    leapyear = False
if leapyear == True:
    print("Leap year.")
else:
    print("Not leap year.")
    
# Alternatively 
if year % 4 == 0:
    if year % 100:
        if year % 400:
            print("Leap Year")
        else:
            print("Not leap year.")
    else:
        print ("Leap year.")
else:
    print("Not leap year.")