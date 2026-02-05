# A dictionary is a data type that stores data in terms of key - value pair.
# It is introduced by the use pf the curly braces {} 
# The values stored inside of a dictionary can be of any data type.
# To access the values in a dictionary we use the keys.


phonebook = {
    "Benson" : "25478956432",
    "Mary" : "2545674567",
    "Stephen" : "2546787645"
}

# Showing the entire dictionary

print(phonebook)
print(type(phonebook))

# print out benson's number
print(phonebook["Benson"])

print('==================')

player = {
    "name" : "Messi",
    "age" : 40,
    "teams" : ["PSG", "Barcelona", "Argentina"]
}

print(player["teams"][1])