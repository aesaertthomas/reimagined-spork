# Ex03
#Thomas Aesaert 1CTAI1
# Schrijf hier jouw functies/Write here your functions.
import random as rand

#Functino for randomly assigning activities from a list to all the people mentioned in a list. and returning it in the form of a dictionary
def divide_participants(people : list, activities : list) -> dict:
    people_with_activities = {} #List that holds the people with their corresponding activities

    for person in people:
        activity_pos = rand.randint(0, len(activities)-1) #Create a random number that corresponds to the position of an activity
        people_with_activities.update({person : activities[activity_pos]}) #Match person with said activity

    return people_with_activities

#Function for creating an overview of what people do what activity in the form of a dictionary
def give_list_per_activity(people_with_activities : dict) -> dict:
    activities_with_corresponding_people = { #Initializing dictionary with activities and empty list of people
        "Ballet dancing" : [],
        "Pole dancing" : [],
        "Trampoline jumping" : [],
        "Pony riding" : []
    }

    for person, activity in people_with_activities.items(): #For every person in the dictionary add them to the correct activity in the overview dictionary
        activities_with_corresponding_people[activity].append(person) 

    return activities_with_corresponding_people

#ENG - Test your functions
participants = ["Stijn", "Joerie", "Frederiek", "Marie", "Dieter", "Tom", "Christophe", "Henk", "Bart", "Johan", "Hans"]
activities = ["Trampoline jumping", "Pole dancing", "Pony riding", "Ballet dancing"]

#Assigning people to activities randomly
print("These activities were randomly assigned to the following people:")
people_with_activities = divide_participants(people=participants, activities=activities)

#Printing out people with their corresponding activities
for activity, person in people_with_activities.items():
    print(f"\t{person} -> {activity}")

print() #Adding some whitespace to make output more readable and clean

#Getting dictionary of every activity with person doing said activity
print("This is an overview of who is assigned to each activity: ")
overview_people_activity = give_list_per_activity(people_with_activities=people_with_activities)

#Printing every activity with corresponding people list
for activity, people_list in overview_people_activity.items():
    print(f"\t{activity} -> {people_list}")