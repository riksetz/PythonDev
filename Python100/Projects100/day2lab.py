# Code sribbles
# Number Manipulation
print(round(8/3, 2))
#Floor division(integer division)
print(8//3)
#Math Operator before = allows numeric variable to be modified after declaration.
result = 4/2
result /=2
print(result)

score = 0
# User scores a point
score += 1
score += 1
score += 1
print(score)

#f-Strings
height = 1.65
isWinning = True
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}.")

# Exercise: Weeks in a life calculator
age = input("What is your current age? ")
currentage = int(age)
lifespan = 90

# Time left 
years = lifespan-currentage
months = years*12
weeks = years*52
days = years*365

print(f"You have {days} days, {weeks} weeks, and {months} months left.")

