class SportActivity:

    def __init__(self, parid : int, parcity : str):
        self.__id = parid
        self.city = parcity
        self.__imgages = []

    # ********** property id - (getter only) ***********
    @property
    def id(self) -> type:
        """ The id property. """
        return self.__id

    # ********** property city   - (setter/getter) ***********
    @property
    def city(self) -> type:
        """ The city property. """
        return self.__city

    @city.setter
    def city(self, value: type) -> None:
        if not isinstance(value, str):
            raise TypeError(f"Expected {str}, got {type(value)}")
        if not value:
            raise ValueError(f"City cannot be empty string")
        self.__city = value

    # ********** property images - (getter only) ***********
    @property
    def images(self) -> type:
        """ The images property. """
        return self.__images

    def add_image(self, image : str):
        if not isinstance(image, str):
            raise TypeError(f"Expected {str}, got {type(image)}")
        if not image:
            raise ValueError(f"Image cannot be empty")
        if image in self.images:
            raise ValueError(f"{image}, already exists in {self.images}")
        #If passed test cases
        self.__images.append(image)

    def __eq__(self, other) -> bool:
        if not isinstance(other, SportActivity):
            raise TypeError(f"Expected {SportActivity}, got {type(other)}")
        return ((self.city == other.city) & (self.id == other.id))

    def __lt__(self, other) -> bool:
        if not isinstance(other, SportActivity):
            raise TypeError(f"Expected {SportActivity}, got {type(other)}")
        return (self.id < other.id)

    def __str__(self) -> str:
        info = f"{self.id} [{self.city}]"
        return info

    def __repr__(self) -> str:
        representation = f"{self.id}"
        return representation
