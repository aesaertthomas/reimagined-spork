# Part 1: Test of data class
# my_report = Report("Stijn Walcarius",12,15,13,9,18)
# print(f"{my_report}")
# print(f"Average score: {my_report.average_score}")


class Report:

    def __init__(self, parname : str, parscores : dict):
        self.name = parname
        self.scores = parscores


    # ********** property name - (setter/getter) ***********
    @property
    def name(self) -> type:
        """ The name property. """
        return self.__name
    
    @name.setter
    def name(self, value: type) -> None:
        if value != "":
            self.__name = value
        else:
            self.__name = ""
    
    # ********** property scores - (setter/getter) ***********
    @property
    def scores(self) -> type:
        """ The scores property. """
        return self.__scores
    
    @scores.setter
    def scores(self, value: type) -> None:
        if isinstance(value, dict) and len(value) == 5:
            for course, score in value.items():

                if not isinstance(score, (int, float)):
                    raise ValueError(f"Score for {course} must be a number")
                if not (0 <= score <= 20):
                    raise ValueError("The number must be between 0 and 20")
                
            self.__scores = value
        else:
            raise ValueError("Scores must be a dictionary with 5 scores pairs")

    @property
    def average_score(self) -> float:
        return (sum(self.scores.values()) / len(self.scores)) if self.scores else 0 #If self.scores checks if the score is not empty
    

    def __str__(self) -> str:
        info = f"Report of {self.name} ->"

        for course, grade in self.scores.items():
            info += f", {course}: {grade}"
            
        return info
    


# my_report = Report("Stijn Walcarius",{"course1": 12, "course2" : 15, "course3" : 13, "course4" :9, "course5" : 18})
# print(f"{my_report}")
# print(f"Average score: {my_report.average_score}")