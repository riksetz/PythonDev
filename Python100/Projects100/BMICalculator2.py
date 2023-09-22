# BMI Calculator 2 - Day 3 project. Date: Monday, 04/09/2023. 1:42 pm.
# Could do i in range (10, 15, 0.1) etc but for assesssment purposes dumbed down

import math

while True:
    programname = "BMI Calculator V2"
    print (f"\nWelcome to {programname}!\n")
    print ("Find your BMI score below.\n")
    
    height = float(input("Enter your height in m:\n"))
    weight = float(input("Enter your weight in kg:\n"))
    bmi = round(weight/height**2)
    
    if bmi < 18.5:
        score = "underweight"
    elif bmi <25:
        score = "normal weight"
    elif bmi <30:
        score = "slightly overweight"
    elif bmi <35:
        score = "obese"
    elif bmi >35:
        score = "clincially obese"
        
    # Less efficient
    # if bmi < 18.5:
    #     score = "underweight"
    # elif bmi >18.5 and bmi <25:
    #     score = "normal weight"
    # elif bmi > 25 and bmi <30:
    #     score = "slightly overweight"
    # elif bmi >30 and bmi <35:
    #     score = "obese"
    # elif bmi > 35:
    #     score = "clincially obese"

    # bmi = (str(bmi))[0:2] - mistake
    # bmi = round(bmi) - rm no float value
    
    print(f"Your BMI is {bmi}, you are {score}.")

    restart = input(f"Run {programname} again: (Y/N)\n").lower()
    if restart != "y":
        print (f"Exited {programname}.\n") 
        break
    print(f"Restarting {programname}...\n")
