# Ex Homework 2 - Fraction
import math

class Fraction:

    def __init__(self, parnum : float, pardenum : float):
        self.__num = parnum
        self.__denominator = pardenum

    # ********** property denum - (setter/getter) ***********
    @property
    def denominator(self) -> type:
        """ The denum property. """
        return self.__denominator
    
    @denominator.setter
    def denominator(self, value: type) -> None:
        self.__denominator = value
    
    # ********** property num - (setter/getter) ***********
    @property
    def num(self) -> type:
        """ The num property. """
        return self.__num
    
    @num.setter
    def num(self, value: type) -> None:
        self.__num = value
    
    
    def __str__(self) -> str:
        info = f"{self.num} / {self.denominator}"
        return info
    
    def simplify(self):
        gcd = math.gcd(self.num, self.denominator)
        if gcd != 0:
            self.num = self.num / gcd
            self.denominator = self.denominator / gcd