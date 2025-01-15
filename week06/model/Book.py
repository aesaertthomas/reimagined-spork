# EX01
# step 1: create a class 'Book'
# step 2: add properties for each attribute
# step 3: add the constructor: make use of the properties
# step 4: add the toString-method
class Book:
    def __init__(self, partitle : str, parauthor : str, parpublisher : str, parisbn : str, par_pubyear : str = "2024"):
        self.__title = partitle
        self.__author = parauthor
        self.__publisher = parpublisher
        self.__isbn = parisbn
        self.__pubyear = par_pubyear

    def __str__(self) -> str:
        info = f"{self.__author}, {self.__title} ({self.__publisher}) *{self.__pubyear}*"
        return info

    # ********** property title - (setter/getter) ***********
    @property
    def title(self) -> type:
        """ The title property. """
        return self.__title
    
    @title.setter
    def title(self, value: type) -> None:
        self.__title = value
    

    # ********** property author - (setter/getter) ***********
    @property
    def author(self) -> type:
        """ The author property. """
        return self.__author
    
    @author.setter
    def author(self, value: type) -> None:
        self.__author = value
    
    # ********** property publisher - (setter/getter) ***********
    @property
    def publisher(self) -> type:
        """ The publisher property. """
        return self.__publisher
    
    @publisher.setter
    def publisher(self, value: type) -> None:
        self.__publisher = value
    
    # ********** property isb - (setter/getter) ***********
    @property
    def isb(self) -> type:
        """ The isb property. """
        return self.__isb
    
    @isb.setter
    def isb(self, value: type) -> None:
        self.__isb = value
    
    # ********** property pubyear - (setter/getter) ***********
    @property
    def pubyear(self) -> type:
        """ The pubyear property. """
        return self.__pubyear
    
    @pubyear.setter
    def pubyear(self, value: type) -> None:
        self.__pubyear = value
    
    
    
