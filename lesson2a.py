# Python lists
# A List in python is a collection of items that are ordered in a certain way
# A list is introduced by the use of the square brackets [].
# The items of a list are stored inside of indexes. Note: In programming we start counting from index zero(0). bmw, benz, hiance
# A list is mutable i.e the contents of a list can be changed.

cars = ["BMW", "BENZ", "Hiance", "Prado", "Probox", "McLaren", "Range"]

print(cars)
print(type(cars))

# Accessing items of a list
print(cars[2])
print( "The car on index four is: ", cars[4])

# List slicing - This is creating a list from a given bigger list
print(cars[4:])

# printing from index 0 to index 3
print(cars[:4])

# printing from hiance to probox
print(cars[2:5])

# List - Mutability
# We use the function append to add an item at the end of a list
cars.append("Mercedes")
print(cars)

cars.append("Subaru")
print(cars)

# We use the pop function to remove an item at the end of a list.
cars.pop()
print(cars)

# We can use an index to add items to a list
cars[5] = "Pajero"
print(cars)

# We can use the sort function to sort our items in alphabetical order
cars.sort()
print(cars)