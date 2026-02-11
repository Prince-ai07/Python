# 1.Create a program to find simple interest
p = float(input("Enter the principal: "))
r = float(input("Enter the rate to be used: "))
t = float(input("Enter the time: "))
si = (p * r * t ) / 100 
print("The simple interest is: ", si)


print("=================================")

# 2.Create a Program to find body mass index
weight = float(input("Enter the weight of the person: "))
height = float(input("Enter the height of the person: "))
BMI = weight / (height ** 2)
print("The Body Mass Index is: ",BMI)

print("================================")

# 3.Create a program to find the area of a triangle
base = float(input("Enter the length of the base: "))
height = float(input("Enter the height: "))
area = (base * height) / 2
print("The area of the triangle is: ",area)

print("================================")

# 4.Create a program to find the area of a circle
radius = float(input("Enter the radius: "))
area = 3.142 * (radius ** 2)
print("The area of the circle is: ", area)

print("===============================")

# 5.Given the dictionary below
shopping = {
    "sugar" : 120,
    "rice" : 200,
    "milk" : 60,
    "bread" : 60
}
# print the dictionary
print(shopping)
# sum of the items in the dictionary
total = sum(shopping.values())
print("The sum of the items is: ", total)

print("===============================")

# 6.Please attempt the following question:
# Suppose we have a dictionary
# person = {
#     "john": 40,
#     "peter" : 45
# }


# What happens when we try retrieve a value using the expression print(person["susan"])
# Ans: What we will have is a key error
# working:
#  try:
#     person = {
#         "john" : 40,
#         "peter" : 45
#     }
#     print(person["susan"])
# except Exception as e:
#     print("This is an error: ", e)
# c.Since "susan" is not a key in the set, Python raises a KeyError exception


print("===========================")

# 7.Create a list of towns and reverse it

towns = ["Nairobi", "Mombasa", "Kisumu", "Eldoret", "Nakuru", "Thika"]

reversed_towns = towns [::-1]
print(reversed_towns)

print("=============================")

# 8.Create a Loop to print from 10 to 40

for number in range ( 10, 41):
    print(number)

print("=============================")

# 9.Create a loop to print from -10 to -50

for number in range ( -10, -51, -1):
    print(number)

print("=============================")

# 10. Create a Function to check if Year is Leap or Not

def leap_year():
    year = int(input("Enter the year: "))
    if year % 4 == 0 and year % 100 != 0:
        print("This is a Leap year")
    elif year % 400 == 0:
        print("This is a Leap year")
    else:
        print("This is not a Leap year")
leap_year()

print("=============================")

# 11.Create a function to find body mass index

def Body_Mass_index():
    weight = float(input("Enter the weight of the person: "))
    height = float(input("Enter the height of the person: "))
    BMI = weight / (height ** 2)
    print("The Body Mass Index is: ",BMI)
Body_Mass_index()


print("==============================")

# 12. Using if statements, write a Python program to check how much a traveler would pay based of distance

distance = float(input("Enter the distance covered: "))
if distance > 0 and distance <= 100:
    print("The cost is 5.00")
elif distance > 100 and distance <= 500:
    print("The cost is 8.00")
elif distance > 500 and distance < 1000:
    print("The cost is 10.00")
else:
    print("The cost is 12.00")


print("==============================")

# 13.Create a python program to find if number is Odd or Even
number = int(input("Enter the number: "))
if number % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")






