# Ex Homework 1


class Parcel:

    def __init__(self, pardescription : str, parwidth : str, parheight : str, pardepth : str):
        self.__description = pardescription
        self.__width = parwidth
        self.__height = parheight
        self.__depth = pardepth

    # ********** property description - (getter) ***********
    @property
    def description(self) -> type:
        """ The description property. """
        return self.__description

    # ********** property width - (setter/getter) ***********
    @property
    def width(self) -> type:
        """ The width property. """
        return self.__width
    
    @width.setter
    def width(self, value: int) -> None:
        self.__width = value if value > 0 else 1
    # ********** property height - (setter/getter) ***********
    @property
    def height(self) -> type:
        """ The height property. """
        return self.__height
    
    @height.setter
    def height(self, value: int) -> None:
        self.__height = value if value > 0 else 1
    
    # ********** property depth - (setter/getter) ***********
    @property
    def depth(self) -> type:
        """ The depth property. """
        return self.__depth
    
    @depth.setter
    def depth(self, value: int) -> None:
        self.__depth = value if value > 0 else 1

    @property
    def volume(self) -> float:
        return round(self.height * self.width * self.depth, 3)
    
    def __str__(self) -> str:
        info = f"{self.description} ({self.depth}cm * {self.width}cm * {self.height}cm)"
        return info
    
    


