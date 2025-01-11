class Birthdate:

    def __init__(self, parday : int, parmonth : int, paryear : int):
        self.day = parday
        self.month = parmonth
        self.year = paryear

    def __str__(self) -> str:
        info = f"{self.day}/{self.month}/{self.year}"
        return info

    def __eq__(self , other): #2 birthdates are equal when the string representations match
        if isinstance(other, Birthdate):
            return (str(self) == str(other))

    def __repr__(self):
        return self.__str__()

    # ********** property day - (setter/getter) ***********
    @property
    def day(self) -> type:
        """ The day property. """
        return self.__day

    @day.setter
    def day(self, value: type) -> None:
        if value != 0:
            self.__day = value


    # ********** property month - (setter/getter) ***********
    @property
    def month(self) -> type:
        """ The month property. """
        return self.__month

    @month.setter
    def month(self, value: type) -> None:
        if value != 0:
            self.__month = value

    # ********** property year - (setter/getter) ***********
    @property
    def year(self) -> type:
        """ The year property. """
        return self.__year

    @year.setter
    def year(self, value: type) -> None:
        if value != 0:
            self.__year = value
