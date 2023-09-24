# CSE1PE Week 5: Functions and Objects

import math

def topic():
    print("\nCSE1PE Week 5: Functions and Objects\n")

topic()
# big = max("aAHELLOWORLD1234567890zZ")
# tiny = min("aAHELLOWORLD1234567890zZ")
# print (big)
# print (tiny)

# Python Objects


# Multiple Parameters/Arguments
def computepay (rate, hours):
    pay = rate * hours
    return pay
# Invoke
x = computepay (20, 5)
print (f"${x}")

# Void Function - No return value

# Define Function, set parameters
def greet(lang):
    if lang == "es":
        print ("Hola")
    elif lang == "fr":
        print ("Bonjour")
    else:
        print ("Hello")
# Invoke Function by stating parameters
greet("es")
greet("Es")
greet("fr")
greet("any")
# Return Values
def greetme(lang):
    if lang == "es":
        return "Hola"
    elif lang == "fr":
        return "Bonjour"
    else:
        return "Hello"
print (greetme("en"), "Raquelle\n")
