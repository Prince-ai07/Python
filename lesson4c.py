# A for loop can also be used to iterate through a list, a tupple, string or even a dictionary.

name = "Jeremiah"

for letter in name:
    if letter == "m":
        print("m=This is letter m")
    else:
        print(letter)

print("==========================")
# Below is a list of counties
counties = ["Nairobi", "Mombasa", "Kisumu", "Nakuru", "Eldoret", "Kajiado", "Machakos", "Meru", "Embu"]
print(counties)

for county in counties:
        print(county)


print("==========================")
for county in counties: 
    if "Mombasa" in counties:
        print("Mombasa is found")
        break
    else:
        print("Mombasa is not found")


print("==========================")
# A for loop can also be used to iterate through a dictionary

player = {
     "name": "Mbappe",
     "age": 25 ,
     "teams" : ["Monaco", "PSG", "Real Madrid"],
     "nationality" : "French"
}

for key in player:
     print(key)

print("==========================")
# Print values
for value in player:
    print(player[value])

print("==========================")
# Loop through the teams the player has played for
for team in player["teams"]:
    print(team)

 
