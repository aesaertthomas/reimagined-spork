# Ex02
import os



def read_myfile(path : str):
    with open(path, 'r') as file: #Chose to just use reports.txt as my file
        for line in file:
            print(line, end="")

def write_input_to_file(path : str):
    to_continue = True
    with open(path, "w") as file: #Make a new "instance/object (dont know the term) of a file with path and in mode write. (if not exist file is created)

        while to_continue:
            text = input("Enter a new line, or press enter to finish: ")
            
            if text != '': #This is to test wether to break off the while loop or to keep goingd
                file.write(text + "\n")
            elif text == "":
                to_continue = False

    


path = input("Please enter the path for your file: ")

if os.path.exists(path):
    read_myfile(path=path)
else:
    write_input_to_file(path=path)


