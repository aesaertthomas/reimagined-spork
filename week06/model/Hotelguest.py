# EX04
# step 1: create a class 'Hotelguest'
# step 2: add properties for each attribute: check the value in each setter-property. (A value can also be a boolean.)
# step 3: add the constructor: make use of the properties
# step 4: add the toString-method
class Hotelguest:

    def __init__(self, parlastname : str, parfirstname : str, parbalance : int, parchecked_in : bool):
        self.__lastname = parlastname
        self.__firstname = parfirstname
        self.__balance = parbalance
        self.__checked_in = parchecked_in


    def __str__(self) -> str:
        if self.checked_in:
            info = f"OK: {self.lastname} {self.balance} euro"
        else:
            info = f"X: {self.firstname} {self.lastname}"
        return info

    # ********** property lastname - (setter/getter) ***********
    @property
    def lastname(self) -> type:
        """ The lastname property. """
        return self.__lastname
    
    @lastname.setter
    def lastname(self, value: type = "Unknown") -> None:
        self.__lastname = value
    
    # ********** property firstname - (setter/getter) ***********
    @property
    def firstname(self) -> type:
        """ The firstname property. """
        return self.__firstname
    
    @firstname.setter
    def firstname(self, value: type = "Unknown") -> None:
        self.__firstname = value
    
    # ********** property balance - (setter/getter) ***********
    @property
    def balance(self) -> type:
        """ The balance property. """
        return self.__balance
    
    @balance.setter
    def balance(self, value: type) -> None:
        if value < 0:
            self.__balance = 0
        else:
            self.__balance = value
    # ********** property checked_in - (setter/getter) ***********
    @property
    def checked_in(self) -> type:
        """ The checked_in property. """
        return self.__checked_in
    
    @checked_in.setter
    def checked_in(self, value: type) -> None:
        if type(value) == bool:
            self.__checked_in = value
        else:
            self.__checked_in = False


    
    
    

