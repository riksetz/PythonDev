# CSE1PE Week 4 lab: Iteration

import math
import time

print ("\nCSE1PE W4: Iteration\n")

# Aggregation
# Sum
total = 0
for x in range(1, 10):
    total = total + x
print(total)
# Average (Mean)
total = 0
count = 0
for x in range(1, 10):
    total = total + x
    count = count + 1
average = total / count
print(average)
# Maximum Value
maximum = 0
for x in [3, 1, 8, 4]:
    if x > maximum:
        maximum = x
print(maximum)
# Count
count = 0
for x in [4, 9, 5, 8, 9]:
    if x > 5:
        count = count + 1
print(count)

# # Loops: While and For
# # For loop: print numbers below 10
# for i in range(99):
#     print(i)
# # While loop: print numbers below 10
# i = 0
# while i < 10:
#     print(i)
#     i = i + 1

# # Sh**test program ever, when x = 1, inner loop prints 1 time, when x = 3, inner loop prints 3 times.
# x = 0
# while x < 5:
#     if x % 2 == 0:
#         x = x + 1
#         continue
#     # Prints all values less than 3.
#     y = 0
#     while y < x:
#         print(y)
#         y = y + 1
#     x = x + 1
    
# # Program prints even numbers less than 10, including 0.
# x = 0
# while x < 10:
#     if x % 2 == 1:
#         x = x + 1
#         continue
#     print(x)
#     x = x + 1

# # Finite loop - x condition inside while loop
# x = 1
# while x * 2 < 10:
#     print(x)
#     x = x + 1

# # Infinite loop - x condition outside while loop
# x = 1
# while x * 2 < 10:
#     print(x)
# x = x + 1

# # Program which calculates the total stopping time. Collatz conjecture.
# n = int(input('Enter n: '))
# t = 0
# while n != 1: # Repeat until n reaches 1.
#     if n % 2 == 0:
#         # n is even.
#         n = n / 2
#     else:
#         # n is odd.
#         n = n * 3 + 1
#     # Increment the total stopping time.
#     t = t + 1
# print(t)

# Same sh*t example with 1 less line
# total_cost = 0
# while True:
#     item_cost = float(input('Item cost: '))
#     if item_cost < 0:
#         break
#     total_cost = total_cost + item_cost
# print(total_cost)
# Program below adds cost until a negative number is entered.
# total_cost = 0
# item_cost = float(input('Item cost: '))
# while item_cost >= 0:
#     total_cost = total_cost + item_cost
#     item_cost = float(input('Item cost: '))
# print(total_cost)

# # Linear solution
# start_time = time.time()
# # input("Hit Enter when you think 5 seconds have elapsed")
# target=10000000000000000 
# for number in range(1,target//2):
#     if number**2>target:
#         break

# print(target,number-1)

# end_time = time.time()

# print(end_time - start_time, " secs")