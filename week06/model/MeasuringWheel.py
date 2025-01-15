# EX05
# step 1: create a class 'MeasuringWheel'
# step 2: add properties for each attribute
# step 3: add the constructor: make use of the properties. Remark: what if there is no setter-property?
# step 2 bis (new): add two "calculated properties": These get-properties has no attribute of its own, but returns a calculation based on the other properties.
# step 4: add the toString-method
# (step 5: Add additional common methods (don't forget the first parameter self!))
import math

class MeasuringWheel:
    

    def __init__(self, parradius : float, parrotations : int = 0):
        self.__radius = parradius
        self.__rotations = parrotations

    
    def __str__(self) -> str:
        info = f"Measuring wheel with radius {self.radius} and rotations {self.rotations}"
        return info

    # ********** property radius - (setter/getter) ***********
    @property
    def radius(self) -> type:
        """ The radius property. """
        return self.__radius
    
    @radius.setter
    def radius(self, value: type) -> None:
        self.__radius = value
    
    # ********** property rotations - (setter/getter) ***********
    @property
    def rotations(self) -> type:
        """ The rotations property. """
        return self.__rotations
    
    @rotations.setter
    def rotations(self, value: type) -> None:
        self.__rotations = value
    

    def circumference(self) -> float:
        return (2 * math.pi * self.radius )
    
    def distance(self) -> float:
        
        return self.rotations * self.circumference()