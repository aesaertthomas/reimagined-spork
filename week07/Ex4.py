# Ex04 - Don't forget to add the parameter to the functions
from model.Report import Report

#Part 2: Read file + print reports
def read_reports(filepath: str) -> list:
    reports = []  # List to store all the report objects
    
    with open(filepath, "r") as file:
        # If there's a header or unwanted line at the start, skip it
        next(file)  # Skip the first line if needed, or remove this line if not
        
        for line in file:
            line = line.strip()  # Remove any extra whitespace
            parts = line.split(":")
            print(f"Parts: {parts}")
            name = parts[0].strip()  # The student's name

            parts.pop(0)

            # Split scores by comma and then clean up each course
            scores = {}
            print(parts)
            for i, score in enumerate(parts):

                # Add course and score to the dictionary
                scores.update({f"course{i+1}" : float(parts[i])})
            
            # Create a Report object and add it to the list
            report = Report(name, scores)
            reports.append(report)

    return reports  # Return the list of reports

def print_reports(reports : list):
    for report in reports:
        print(report)

def search_report(reports : list, name : str) -> Report:
    
    for report in reports:
        
        if report.name.lower() == name.lower():
            return report 

        
    return None



reports = read_reports("doc/Reports.txt")
#Part 3: Search a report based on the name



