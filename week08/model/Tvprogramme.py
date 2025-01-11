from Presenter import Presenter

class Tvprogramme:

    def __init__(self, partitle : str, parpresenter : Presenter, paris_active : bool):
        self.__title = partitle
        self.presenter = parpresenter
        self.is_active = paris_active

    def __str__(self) -> str: #str is for when you try to represent the object as a string
        info = f"Tvprogramme {self.title} by {self.presenter}"
        return info

    def __repr__(self) -> str: #Repr is for when you try to represent the object directly (because if you don't use this you wil get a memory address as response)
        info = f"Tvprogramme {self.title} by {self.presenter}"
        return info



    # ********** property title - (getter) ***********
    @property
    def title(self) -> type:
        """ The title property. """
        return self.__title




    # ********** property presenter - (setter/getter) ***********
    @property
    def presenter(self) -> type:
        """ The presenter property. """
        return self.__presenter

    @presenter.setter
    def presenter(self, value: type) -> None:
        if not isinstance(value, Presenter):
            value = None

        self.__presenter = value



    # ********** property is_active - (setter/getter) ***********
    @property
    def is_active(self) -> type:
        """ The is_active property. """
        return self.__is_active

    @is_active.setter
    def is_active(self, value: type) -> None:
        if not isinstance(value, bool):
            value = False

        self.__is_active = value
