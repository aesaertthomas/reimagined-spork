from model.Beer import Beer

def read_beers(path : str) -> list:
    beers = []
    
    with open(path, "r") as file:
        next(file) #Rm header
        for line in file:
            #Cleaning file output
            line = line.replace("\n","").strip()
            parts = line.split(";")

                #Saving file data to var. (beer __init__ more readable)
            name = parts[1].strip()
            brewery = parts[2].strip()
            color = parts[3].strip()
            alcohol = parts[4].strip()

            beer = Beer(parname=name,paralcohol=alcohol, parbrewery=brewery, parcolor=color)

            #Appending beers into beer list
            beers.append(beer)

    return beers


def print_beers(beers : list): 
    for beer in beers:
        print(beer)

def search_beer_by_name(beers : list, beer_to_find : str) -> Beer:
    
    for beer in beers:
        if(beer.name == beer_to_find):
            return beer
         
    return None

    pass


beers = read_beers("doc/beers.csv")

print_beers(beers=beers)

print("\n")
beer_to_find = input("Please enter the name for type beer you wish to find: ")
result_beer_search = search_beer_by_name(beers=beers, beer_to_find=beer_to_find)

if(result_beer_search != None):
    print(result_beer_search)