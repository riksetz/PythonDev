# Pizza Party - Day 3 project. Date: Monday, 04/09/2023. 5:00 pm.

import math

# print("Welcome to Python Pizza Deliveries!\n")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25

# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1
# print(f"Your final bill is: ${bill}.")

# Logical Operators
# Love Calculator 

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combinedname = (name1 + name2).lower()
t = combinedname.count("t")
r = combinedname.count("r")
u = combinedname.count("u")
e = combinedname.count("e")
true = t + r + u + e 
l = combinedname.count("l")
o = combinedname.count("o")
v = combinedname.count("v")
e = combinedname.count("e")
love = l + o + v + e
score = int(str(true) + str(love))

print (combinedname)
print (score)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print (f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")


