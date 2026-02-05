# Tuple
# Is an imutable type of a list (It cannot chnage)
# To introduce a tuple, we use parenthesis ()

counties = ("Nairobi", "Mombasa", "Nakuru", "Eldoret", "Kajiado", "Kisii")
print(counties)
print(type(counties))

# slicing of tuples
print(counties[3:])

# accessing items of a tuple by use of the indexes
print(counties[5])

# Note: Below will generate an error
# Attribute error
counties.append("Machakos")
print(counties)