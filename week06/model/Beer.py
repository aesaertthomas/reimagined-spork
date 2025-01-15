# EX02
# step 1: create a class 'Beer'
# step 2: add properties for each attribute: check the value in each setter-property
# step 3: add the constructor: make use of the properties
# step 4: add the toString-method
class Beer:

    def __init__(self, parname : str = "unknown", parbrewery : str = "unknown", paralcohol : float = "unknown", parcolor : str = "unknown"):
        
        self.__name = parname
        self.__brewery = parbrewery
        self.__color = parcolor
        self.__alcoholpercentage = paralcohol

    def __str__(self) -> str:
        info = f"{self.__name} {self.__brewery} - {self.__alcoholpercentage}"
        return info
    
    # ********** property name - (setter/getter) ***********
    @property
    def name(self) -> type:
        """ The name property. """
        return self.__name
    
    @name.setter
    def name(self, value: type = "unkown") -> None:
        self.__name = value
        # ********** property brewery - (setter/getter) ***********
    @property
    def brewery(self) -> type:
        """ The brewery property. """
        return self.__brewery
    
    @brewery.setter
    def brewery(self, value: type = "unkown") -> None:
        self.__brewery = value
    
    # ********** property color - (setter/getter) ***********
    @property
    def color(self) -> type:
        """ The color property. """
        return self.__color
    
    @color.setter
    def color(self, value: type = "unkown") -> None:
        self.__color = value
    
    # ********** property alcohol - (setter/getter) ***********
    @property
    def alcoholpercentage(self) -> type:
        """ The alcohol property. """
        return self.__alcoholpercentage
    
    @alcoholpercentage.setter
    def alcoholpercentage(self, value: type = "unknown") -> None:
        if type(value) == float and value <= 100 and value >= 0:
            self.__alcoholpercentage = value
        else:
            self.__alcoholpercentage = -1
    
    
    
    