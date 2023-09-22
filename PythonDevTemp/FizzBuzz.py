# Popular Software Interview Question
# Print numbers 1-100, for multiples of 3 print Fizz, for multiples for 5 print Buzz, for multiples of 3 and 5 print FIzzBuzz.
# 4 Outputs therefore, 4 selection branches required.

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print ("FizzBuzz")
    elif i % 3 == 0:
        print ("Fizz")
    elif i % 5 == 0:
        print ("Buzz")
    else:
        print(i)
    