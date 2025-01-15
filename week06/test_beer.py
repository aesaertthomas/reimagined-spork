# Ex02
# Test class Beer
from model.Beer import Beer

print("** Beer 1 ***")
b1 = Beer("Augustijn", "Bios", 12.0, "amber")
print(b1)
# change brewery to an empty string
b1.brewery = ""
print(b1)

print("** Beer 2 ***")
b2 = Beer("Jupiler", "", 3.3, "blond")
print(f"The color of {b2.name} is {b2.color} ")
print(f"Alcoholpercentage: {b2.alcoholpercentage} ")

b2.alcoholpercentage = "5,5"
print(f"Alcoholpercentage: {b2.alcoholpercentage} ")
