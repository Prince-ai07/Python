# Create a python program that is able to determine whether a number entered is an odd number or even number

# number = int(input("Enter the number: "))

# if number % 2 == 0 :
#     print("Even number")
# else:
#     print("Odd number")

# Create a python program that is able to determine whether a person can donate blood based on the age and weight of a person.. If the weight is greater than 50kg and age is above 18, then the person can donate ,else not possible.

Age = int(input("Enter Your Age: "))
Weight = float(input("Enter Your Weight: "))
if Age >= 18 and Weight >= 50:
    print("Can donate")
else: 
    print("Cannot Donate")

