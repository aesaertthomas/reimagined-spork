# Ex03

def extend_file(path : str):

    with open(path, "a") as file:
        to_continue = True
        while to_continue:
            text = input("Enter a new line, or press enter to finish: ")
            
            if text != '': #This is to test wether to break off the while loop or to keep goingd
                file.write(text + "\n")
            elif text == "":
                to_continue = False

path = input("Please enter the path for your file: ")

extend_file(path=path)
