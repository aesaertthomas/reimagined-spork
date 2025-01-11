# Lab week 9 - exercise 1
from model.Beer import Beer

def test1():
    #Create an object of the class Beer
    #Change one of the properties to a wrong value
    #Use now exception handling
    pass

test1()


def test2():
    beername = input("Enter a new name:> ")
    breweryname = input("Enter a new brewery:> ")
    color = input("Enter a new color:> ")
    alcoholpercentage = float(input("Enter a new alcoholpercentage:> "))
    print("Making beer...")
    beer1 = Beer(parname=beername, parbrewery=breweryname, paralcoholpercentage=alcoholpercentage, parcolor=color)
    #Create an object of the class Beer and print the object
    print(beer1)
    #Apply exception handling so that the user receives an error message in case of invalid input.
    beer1.brewery(102)
    beer1.brewery("")
    beer1.brewery("HOPAAAA")

    print(beer1)
test2()
