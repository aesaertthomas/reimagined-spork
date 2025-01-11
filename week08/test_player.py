from model.Player import Player
from model.Birthdate import Birthdate

# Test of class attribute & class method (=static method)


# def test_players():
#     # create a static method
#     Player.team_name = "Red devils"

#     player1 = Player("Thibault", "Courtois", "keeper", 8)
#     player2 = Player("Vincent", "Kompany", "striker", 8)
#     player3 = Player("Axel", "Witsel", "striker")
#     team = [player1, player2, player3]
#     print(team)

#     print("\nVincent scores!")
#     player2.make_goal()
#     print(player2)

#     print("\nAxel scores!")
#     player3.make_goal()
#     print(player3)

#     print(f"The total number of goals from the team { Player.team_name} is { Player.get_goals_team()}.")

# test_players()


# Test class association:we connect the dataclass Birthdate to Player:
# 1 add a new property 'birthdate' in de class Player
# 2 complete the constructor (init): add an extra parameter & call the new property

def test_ex4():
    player1 = Player("Thibault", "Courtous", "keeper",
                 8, Birthdate(11, 5, 1992))
    player2 = Player("Vincent", "Kompany", "striker",
                 8, Birthdate(10, 4, 1986))
    player3 = Player("Axel", "Witsel", "striker")             # no birthdate --> defaultvalue!

    print("\nThe birthdates of the players are:")
    for item in [player1, player2, player3]:
        print(f"{item} -> Birthdate: {item.birthdate}")


test_ex4()
