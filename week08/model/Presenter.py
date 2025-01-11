class Presenter:

    def __init__(self, parlastname : str, parfirstname : str):
        self.lastname = parlastname
        self.firstname = parfirstname

    # ********** property lastname - (setter/getter) ***********
    @property
    def lastname(self) -> type:
        """ The lastname property. """
        return self.__lastname

    @lastname.setter
    def lastname(self, value: type) -> None:
        self.__lastname = value

    # ********** property firstname - (setter/getter) ***********
    @property
    def firstname(self) -> type:
        """ The firstname property. """
        return self.__firstname

    @firstname.setter
    def firstname(self, value: type) -> None:
        self.__firstname = value

    def __str__(self) -> str:
        info = f"Presenter: {self.lastname}, {self.firstname}"
        return info

    def __eq__(self, other) -> bool:
        if not isinstance(other, Presenter):
            raise TypeError("You should make sure the to compare to object is of type Presenter}")
        if (self.lastname == other.lastname) and (self.firstname == other.firstname):
            return True
        return False

presenter1 = Presenter("Thomas", "A")
presenter2 = Presenter("Thomas", "Ae")
presenter3 = Presenter("Thomas", "A")

print(presenter1 == presenter2)
print(presenter1 == presenter3)
