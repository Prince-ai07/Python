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
search = input("Enter the county: ")

found = False
for county in counties: 
    if county == search:
        found = True
        break

if found:
    print(search, "is available")
else:
    print(search, "is not available")

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

 
