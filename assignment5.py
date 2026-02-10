# 1.Functions without parameters
# Create a function that: Takes no parameters, Uses arithmetic operators to calculate the area of a rectangle, Prints the result
def area():
    length = 15
    width = 5
    area = length * width
    print("Area: ", area)
area()

print("===========================================")
# 2.Functions with parameters
# Create a function that: Accepts two numbers as parameters, returns their sum, difference, product and division 

def numbers(a, b):
    sum = a + b
    difference = a - b
    product = a * b
    quotient = a / b
    print("The sum of the numbers is:", sum)
    print("The difference of the numbers is:",difference)
    print("The product of the numbers is:",product)
    print("The division of the numbers is:",quotient)

numbers(10, 5)

print("============================================")

# Control Statement (if...elif...else)
# Write a function that accepts a number(Use input function), checks whether the number is: positive, negative or zero.

def number():
    number = float(input("Enter the number:"))
    if number > 0:
        print("The number is positive")
    elif number < 0:
        print("The number is negative")
    else:
        print("The number is zero")

number()

print("=====================================")
# 4.Loop with arithmetic
# Write a function that: accepts a number n, uses it for a loop, calculates the sum of numbers from 1 to n

def sum(n):
    total = 0
    for x in range(1, n + 1):  # Loop from 1 to n
        total = total + x             # Add each number to total
    print("The sum of numbers from 1 to", n, "is", total)

# Example
sum(5)


print("=====================================")
# 5.While loop
# Write a function that: Accepts a number(Use input()function), uses a while loop, calculates the squares of numbers from 1 up to that number

def square():
    number = float(input("Enter the number: "))
    n = 1   
    while n <= number:
        square = n ** 2
        print("The square of", n, "is:", square)
        n = n + 1

square()




