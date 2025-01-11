# Ex01

def read_myfile(path : str):
    with open(path, "r") as file: #Chose to just use reports.txt as my file
        for line in file:
            print(line, end="")

read_myfile(path="doc/Reports.txt")

