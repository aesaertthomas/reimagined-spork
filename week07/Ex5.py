# Ex05 - Don't forget to add the parameter to the functions
from model.Player import Player

import random

def read_players(path : str) -> list:
    players = []
    with open(path, "r") as file:
        for line in file:
            line = line.replace("\n", "").strip()

            # line.strip()
            parts = line.split(";")
            player = Player(parts[0],parts[1],parts[2])


            players.append(player)

    
    return players


def print_players(player_list : list, teamname : str):
    print(f"name team: {teamname}")
    for player in player_list:
        print(player)

def select_random_players(players : list) -> list:
    selected_players = []
    
    for i in range(0, 11):
        player_pos = random .randint(0, len(players) - i) #Dynamically shorten the player position based on how many have already been selected

        selected_players.append(players[player_pos])

    return selected_players

def save_players(random_players : list):
    path = "doc/RandomPlayers.txt"

    with open(path, "w") as file:
        for player in  random_players:
            
            lastname = player.lastname
            firstname = player.firstname
            age = player.age

            file.write(f"{lastname};{firstname};{age}\n")

    file.close()
    pass


# Part 1: Test data class
# player1 = Player("Walcarius","Stijn",40)
# player2 = Player("Dewitte","Marie",25)
# player3 = Player("Berthier","Frederiek",32)
# player4 = Player("Claerhout","Joerie",30)
# players = [player1, player2, player3, player4]
# for player in players:
#     print(player)


#Part 2: read file + print players
 
#Part 3: select random team + save team


players = read_players("doc/Players.txt")

print_players(player_list=players, teamname="The Red Devils")

random_players = select_random_players(players=players)

save_players(random_players=random_players)
