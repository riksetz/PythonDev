num_char = len(input("What is your name? "))
# print ("Your name has " + num_char + " characters.\n")
# type() - Function checks data type received.
print(type(num_char))
# print(type(len(input("What is your name?"))))
#Type conversion (Type casting)
new_num_char = str(num_char)
print ("Your name has " + new_num_char+ " characters.\n")
a = float(123)
print(a)
#Also valid
print (70 + float("100.5"))
print (70 + float("100"))
#This outputs 70100.
print(str(70)+str(100))
#Program that adds numbers in string input
two_digit_number = input("Type a two digit number: ")
number1 = int(two_digit_number[0])
number2 = int(two_digit_number[1])
print (number1 + number2)

