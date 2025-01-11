class Player:

    def __init__(self, parlastname : str, parfirstname : str, parage : int):
        self.firstname = parfirstname
        self.lastname = parlastname
        self.age = parage

    def __str__(self) -> str:
        info = f"{self.lastname.upper()}, {self.firstname} ({self.age})"
        return info
    
    # ********** property lastname - (setter/getter) ***********
    @property
    def lastname(self) -> type:
        """ The lastname property. """
        return self.__lastname
    
    @lastname.setter
    def lastname(self, value: str) -> None:
        self.__lastname = value
    
    # ********** property firstname - (setter/getter) ***********
    @property
    def firstname(self) -> type:
        """ The firstname property. """
        return self.__firstname
    
    @firstname.setter
    def firstname(self, value: type) -> None:
        self.__firstname = value
    
    # ********** property age - (setter/getter) ***********
    @property
    def age(self) -> type:
        """ The age property. """
        return self.__age
    
    @age.setter
    def age(self, value: type) -> None:
        self.__age = value
    