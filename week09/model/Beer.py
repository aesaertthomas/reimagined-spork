class Beer:

    def __init__(self,  parname: str, parbrewery: str, paralcoholpercentage: float, parcolor: str) -> None:
        self.name = parname
        self.brewery = parbrewery
        self.alcoholpercentage = paralcoholpercentage
        self.color = parcolor

    # ********** property name - (setter/getter) ***********
    @property
    def name(self) -> str:
        """ The name property. """
        return self.__name
    
    def value_checker(self, given_value, expected_type): #Customer written function (because did not feel like copy pasting this every time 😅)
        if not isinstance(given_value, (expected_type)):
            raise TypeError("The inputted brewery name must be a string")
        if not given_value:
                raise ValueError("The inputted value cannot be empty")
        return given_value #If it didnt pass code would not get to here
    

    @name.setter
    def name(self, value: str) -> None:
        self.__name = self.value_checker(given_value=value, expected_type=str)
    
    # ********** property brewery - (setter/getter) ***********
    @property
    def brewery(self) -> str:
        """ The brewery property. """
        return self.__brewery
    
    @brewery.setter
    def brewery(self, value: str) -> None:
        self.__brewery = self.value_checker(value, str)
    
    # ********** property alcoholpercentage - (setter/getter) ***********
    @property
    def alcoholpercentage(self) -> float:
        """ The alcoholpercentage property. """
        return self.__alcoholpercentage
    
    @alcoholpercentage.setter
    def alcoholpercentage(self, value: float) -> None:
        if not isinstance(value, (float)):
            raise TypeError("Alcoholpercentage must be a float")
        if not (value >= 0 and value <= 100):
            raise ValueError("Alcholpercentage must be in the range 0 - 100")


    # ********** property color - (setter/getter) ***********
    @property
    def color(self) -> str:
        """ The color property. """
        return self.__color
    
    @color.setter
    def color(self, value: str) -> None:
        self.__color = self.value_checker(value, str)
    
    def __str__(self) -> str:
        return f"{self.name} {self.brewery} - {self.alcoholpercentage}"

