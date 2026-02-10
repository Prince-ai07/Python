# Function with parameters
# parameters: They are values that get passed as arguments given to a function inside of the parenthesis 

def greeting(name):
    print(f"{name}, how are you? Hope everything is fine.")

greeting("Jeremiah")
greeting("Braut")
greeting("Stacie")

print("================================================")
def message(names):
    print(f"{names}, we shall be having a general meeting on date 4 July. Please avail yourself.")

message("Jeremiah")
message("Braut")
message("Stacie")

print("================================================")
# Create a function that accepts parameters to add two numbers
def sum(num1, num2):
    sum = num1 + num2
    print("The sum of the numbers is: ", sum)

sum(10, 20)
