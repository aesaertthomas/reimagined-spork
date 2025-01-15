# EX03
# step 1: create a class 'Car'
# step 2: add properties for each attribute: sometimes a getter-property is enough (remove the setter)
# step 3: add the constructor: make use of the properties. Remark: what if there is no setter-property?
# step 4: add the toString-method
# step 5: Add additional common methods (don't forget the first parameter self!)
class Car:

    def __init__(self, parbrand : str, parmodel : str, parcolor : str, parfuel : str):
        self.__brand = parbrand
        self.__model = parmodel
        self.__color = parcolor
        self.__fuel = parfuel
        self.__mileage = 0.0

    def __str__(self) -> str:
        info = f"{self.__brand} (model: {self.__model} color: {self.__model})"
        return info
    
    # ********** property brand - (setter/getter) ***********
    @property
    def brand(self) -> type:
        """ The brand property. """
        return self.__brand
    
    @brand.setter
    def brand(self, value: type) -> None:
        self.__brand = value
    
    # ********** property model - (setter/getter) ***********
    @property
    def model(self) -> type:
        """ The model property. """
        return self.__model
    
    @model.setter
    def model(self, value: type) -> None:
        self.__model = value
    
    # ********** property color - (setter/getter) ***********
    @property
    def color(self) -> type:
        """ The color property. """
        return self.__color
    
    @color.setter
    def color(self, value: type) -> None:
        self.__color = value
    
    # ********** property fuel - (setter/getter) ***********
    @property
    def fuel(self) -> type:
        """ The fuel property. """
        return self.__fuel
    
    @fuel.setter
    def fuel(self, value: type) -> None:    
        self.__fuel = value

    # ********** property mileage - (setter/getter) ***********
    @property
    def mileage(self) -> type:
        """ The mileage property. """
        return self.__mileage
    
    @mileage.setter
    def mileage(self, value: type) -> None:
        self.__mileage = value
    
    

    def drive(self, extra_km : float):
        self.__mileage += extra_km

    def make_noise(self) -> str:
        noise = ""
        if self.fuel == "diesel":
            noise = "bwaahrooah"
        elif self.fuel == "petrol":
            noise = "swooaahsj"
        elif self.fuel == "electric":
            noise = "sssssssst"
        else:
            noise = "panne"

        return noise 
