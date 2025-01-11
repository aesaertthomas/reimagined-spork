from model.Birthdate import Birthdate

class Player:

    def __init__(self, parlastname: str, parfirstname: str, partype: str,  parvalue: int =0, parbirthdate : Birthdate = None ) -> None:
        self.lastname = parlastname
        self.firstname = parfirstname
        self.value_player = parvalue
        self.type = partype
        self.__goals_player = 0
        self.birthdate = parbirthdate

    # ********** property lastname - (setter/getter) ***********
    @property
    def lastname(self) -> str:
        """ The name property. """
        return self.__lastname
    
    @lastname.setter
    def lastname(self, value: str) -> None:
        if isinstance(value, str) and value != "":
            self.__lastname = value
        else:
            self.__lastname = "unknown"

    # ********** property firstname - (setter/getter) ***********
    @property
    def firstname(self) -> str:
        """ The firstname property. """
        return self.__firstname
    
    @firstname.setter
    def firstname(self, value: str) -> None:
        if isinstance(value, str) and value != "":
            self.__firstname = value
        else:
            self.__firstname = "unknown"


    # ********** property value_player - (setter/getter) ***********
    @property
    def value_player(self) -> int:
        """ The value_player property. """
        return self.__value_player
    
    @value_player.setter
    def value_player(self, value: int) -> None:
        if isinstance(value, int) and value >= 0:
            self.__value_player = value
        else:
            self.__value_player = -1

    # ********** property type - (setter/getter) ***********
    @property
    def type(self) -> str:
        """ The type property. """
        return self.__type
    
    @type.setter
    def type(self, value: str) -> None:
        if isinstance(value, str) and value != "":
            self.__type = value
        else:
            self.__type = "unknown"
    
    # ********** property goals_player - (getter only) ***********
    @property
    def goals_player(self) -> int:
        """ The goals_player property. """
        return self.__goals_player
    
    def __str__(self) -> str:
        return f"Player: {self.firstname}, {self.lastname} (value: {self.value_player}/10) goals: {self.goals_player}"

    # ********** property birthdate - (setter/getter) ***********
    @property
    def birthdate(self) -> type:
        """ The birthdate property. """
        return self.__birthdate
    
    @birthdate.setter
    def birthdate(self, value: type) -> None:
        if value != None:
            if not isinstance(value, Birthdate):
                raise TypeError("Please make sure your entered birthdate is of the the BirthDate")
            self.__birthdate = value
        else:
            self.__birthdate = value
