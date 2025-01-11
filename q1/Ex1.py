# Ex01
#Thomas Aesaert 1CTAI1
# schrijf hier jouw functie/Write here your function
def get_departure_time(announcement : str) -> str:

    #split 1 is just splitting on spaces. (split into time, location, to add time )
    split1 = announcement.split()

    #This code checks wether or not there is time to be added. if there is no time to add. The original announcement is returned.
    if(len(split1) < 3):
        return announcement
    
    #split the time into usable chunks. created seperate variables for extra readability
    splitted_time = split1[0].split("h") 
    hours = int(splitted_time[0])
    minutes = int(splitted_time[1])

    minutes_to_add = int(split1[2][2:-1]) #Substring start from position 2 (so leave out first bracket and + sign) to -1 (leave out last bracket). Also converts to an integer

    #logic behind incrementing time
    if((minutes + minutes_to_add) >= 60):
        hours += 1
        minutes = (minutes + minutes_to_add) - 60 

    else: #This is for when amount of minutes + minutes to add sub 60 minutes (no incrementing of hours)
        minutes += minutes_to_add


    changed_announcement = f"The new departure time now becomes: {hours}h{minutes}"
    return changed_announcement




#ENG - Test your function
#Test1
announcement = "8h35 Kortrijk-Poperinge (+9)"
print(announcement) #Printing the original announcement
new_departure_time = get_departure_time(announcement) #calculating the new departure time
print(f"The announcement is: {announcement} \nThe new departure time now becomes: {new_departure_time}") #Printing new departure time

print() #Add some whitespace

#Test2
announcement = "19h59 Gent (+9)"
print(announcement) #Printing the original announcement
new_departure_time = get_departure_time(announcement) #calculating the new departure time
print(f"The announcement is: {announcement} \nThe new departure time now becomes: {new_departure_time}") #Printing new departure time

print() #add some whitespace

#Test3
announcement = "7h32 Brugge"
print(announcement) #Printing the original announcement
new_departure_time = get_departure_time(announcement)
print(f"The announcement is: {announcement} \nThe new departure time now becomes: {new_departure_time}")