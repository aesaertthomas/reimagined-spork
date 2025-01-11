from model.Beer import Beer
from repositories.BeerRepository import BeerRepository


def print_beers(list_beers):
    for beer in list_beers:
        print(f"{beer.name} ({beer.brewery}) -> alcoholpercentage: {beer.alcoholpercentage}")


def test_beers_a():
    #exercise part A: load the beers & print the list
    pass


#test_beers_a()


def test_beers_b():
    #exercise part B: load the beers & sort the list. Print now the sorted list
    pass

# test_beers_b()


def test_beers_c():
    #exercise part C: load the beers & sort the list. Print now the sorted list
    #Ask the user of a name of a brewery. Find & print beers from this brewery.
    part_brewery = input("\nEnter (a part of) the name of a brewery: ")
    print("Founded beers are: ")
    pass


# test_beers_c()
