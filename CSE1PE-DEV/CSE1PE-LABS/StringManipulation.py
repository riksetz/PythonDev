# CSE1PE - Week 6
import io

# line = line.rstrip() - removes n/ character 
# Opening files & writing files
# Count lines in file program
# Search for file and open
filename = input("Enter the file name: ")
try:
    filename = open(filename)
except:
    print("File cannot be opened:", filename)
    quit() #Stop executing program without traceback error.
    
fhand = open ("table.txt")
count = 0
for i in fhand:
    count = count + 1
print ("Line Count:", count)
# Reading the whole file
inp = fhand.read()
print (len(inp))
print (inp[:])

# Parsing and extracting
# Slicing Strings
s = "\nMonty Python"
# print (s[0:4])
print (s[:])


# Iterations
fruit = "Banana"
index = 0
while index < len(fruit):
    letter = fruit[index]
    print (index, letter)
    index = index + 1
    
for letter in fruit:
    print (letter)

# Count letter 'a' in 'Banana'
word = "Banana"
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print (count)
