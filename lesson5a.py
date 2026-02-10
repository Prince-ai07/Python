# Python functions
# They are a block of code/statements that performs a given task/action. They can be reused throughout the program to perform different tasks.
# Functions are defined using the def keyword. (define)
# We have two main types i.e 
# 1. In-built functions - They come pre-installed with the interpreter i.e print(), pop(), range(),append() etc...
# 2.User-defined functions - They are created by a programmer to solve a given task
# To define a function you need to give it a name followed by parenthesis.
# For the function body, it is usually indented and to invoke a function we use the function name.


def greetings():
    print("Hello, how are you?")

# below we call the function by use of its name
greetings()


print("========================")
# Addition function
def addition():
    num1 = 40
    num2 = 50
    sum = num1 + num2
    print("The sum of the numbers is: ",sum)

addition()

print("=============================")
# Create a function that is able to multiply three value

def product():
    a = 2
    b = 3
    c = 4
    product = a * b * c
    print("Product: ", product)
product()

print("============================")
# Below is a division function
def divide():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    quotient = number1 / number2
    print("The answer is: ", quotient)
    print("----------")

for function in range(3):
    divide()