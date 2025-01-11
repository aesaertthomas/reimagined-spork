import random as rand

from Tvprogramme import Tvprogramme


class Tvchannel:

    # ********** property name - (setter/getter) ***********
    @property
    def name(self) -> type:
        """ The name property. """
        return self.__name

    @name.setter
    def name(self, value: type) -> None:
        if not isinstance(value, str):
                raise TypeError("New name is not of type string")

        self.__name = value #If name were not of type string program not reach this

    # ********** property programmes - (getter only) ***********
    @property
    def programmes(self) -> type:
        """ The programmes property. """
        return self.__programmes

    # ********** property language - (setter/getter) ***********
    @property
    def language(self) -> type:
        """ The language property. """
        return self.__language

    @language.setter
    def language(self, value: type) -> None:

        if not isinstance(value, str):
            raise TypeError("New language has to be of type string")

        acceptable_languages = ['NL','ENG','FR']
        if value not in acceptable_languages:
            value = "ERROR"

        self.__language = value


    def __init__(self, parname : str, parlanguage : str, parprogrammes : list):
        self.name = parname
        self.language = parlanguage
        self.programmes = parprogrammes

    def __str__(self) -> str:
        info = f"{self.name} -> {self.programmes}"
        return info

    def add_tvprogramme(self, programme : Tvprogramme):
        if not isinstance(programme, Tvprogramme):
            raise TypeError(f"{programme} is not of type {type(Tvprogramme)}")

        self.programmes.append(programme)

    def select_random_programme(self):
        index = rand.randint(0, len(self.programmes) - 1)
        return self.programmes[index]

    def search_inactive_programmes(self) -> list:
        inactives = []
        for programme in self.programmes:
            if programme.is_active: #if result .is_active == True append
                inactives.append(programme)

        return inactives
