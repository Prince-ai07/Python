# Loops => sometimes, we may need to do a piece of work a number of repeated times and in such case scenarios we use loops.
# A loop is a control stucture that allows us to execute a block of code repeatedly until a certain condition is met.
# There are two types of loops in python i.e: the for loop and the while loop

# Below is the syntax of a for loop in python
"""
for variable in sequenceprint(n):
    # block of code to be executed
"""

# print("Hello Jeremiah")
# print("Hello Jeremiah")
# print("Hello Jeremiah")
# print("Hello Jeremiah")
# print("Hello Jeremiah")

for greeting in range(5):
    print("Hello Jeremiah", greeting)

print("===================")

for number in range(10, 20):
    print(number)


print("===================") 
# Find the even numbers in the range of 50 to 71  
for number in range(50, 71, 2):
    print(number)

print("===================")
# Create a python program that prints the odd numbers from 100 to 150
for number in range(101, 150, 2):
    print(number)

print("===================")
# create a program that prints the multiples of 3 starting from 201 to 150
for number in range(201, 150, -3):
        print(number)

print("===================")
# create a python program that prints the leap in between 2000 and 2024
for year in range(2000, 2024):
     if year % 4 == 0:
        print(year)  