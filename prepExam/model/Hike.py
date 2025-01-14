from model.SportActivity import SportActivity
from model.Review import Review


class Hike(SportActivity):

    def __init__(self, parid : int, parcity : int, parname : str, pardescription : str, pardifficulty : str, pardistance : float, parduration : int):
        super().__init__(parid=parid, parcity=parcity)
        self.name = parname
        self.description = pardescription
        self.distance = pardistance
        self.duration = parduration
        self.difficulty = pardifficulty
        self.__reviews = []

    def add_review(self, review : Review):
        if not isinstance(review, Review):
            raise TypeError(f"Expected {review}, got {type(review)}")
        if review in self.reviews:
            raise ValueError(f"{review} already in {self.reviews}")
        self.__reviews.append(review)

    def calculated_property_average_speed(self) -> float:
        average_speed = round(self.distance / (self.duration/60),2)
        return average_speed

    def calculated_property_rating(self) -> float:
        if len(self.reviews) == 0:
            return -1.0
        summed = 0
        for review in self.reviews:
            summed += review.rating
        return round(summed/(len(self.reviews)), 2)

    def get_detail_info(self) -> str:
        detailed_info = (
            f"Hike '{self.name}' in City {self.city}\n"
            f"\t-Distance: {self.distance} km, Duration: {self.duration} min, Average Speed: {self.calculated_property_average_speed()}\n"
            f"\t-Number of reviews: {len(self.reviews)}\n"
            f"\t-Average Rating: {self.calculated_property_rating()}"
        )
        return detailed_info

    def __lt__(self, other) -> bool:
        if not isinstance(other, Hike):
            raise TypeError(f"Expected {Hike}, got {type(other)}")
        return (self.distance < other.distance)

    def __str__(self) -> str:
        info = f"{self.name} ({self.city}) - {self.distance} km"
        return info
    def __repr__(self) -> str:
        str_repr = f"{self.name} ({self.city})"
        return str_repr


    # ********** property name - (setter/getter) ***********
    @property
    def name(self) -> type:
        """ The name property. """
        return self.__name
    @name.setter
    def name(self, value: type) -> None:
        if not isinstance(value, str):
            raise TypeError(f"Expected {str}, got {type(value)}")
        if not value:
            raise ValueError(f"Name cannot be empty")
        self.__name = value

    # ********** property description - (setter/getter) ***********
    @property
    def description(self) -> type:
        """ The description property. """
        return self.__description

    @description.setter
    def description(self, value: type) -> None:
        if not isinstance(value, str):
            raise TypeError(f"Expected {str}, got {type}")
        if not value:
            raise ValueError(f"Description cannot be empty")
        self.__description = value

    # ********** property difficulty - (setter/getter) ***********
    @property
    def difficulty(self) -> type:
        """ The difficulty property. """
        return self.__difficulty

    @difficulty.setter
    def difficulty(self, value: type) -> None:
        if not isinstance(value, str):
            raise TypeError(f"Expected {str}, got {type(value)}")
        if not value:
            raise ValueError(f"Difficulty cannot be empty")
        self.__difficulty = value


    # ********** property distance - (setter/getter) ***********
    @property
    def distance(self) -> type:
        """ The distance property. """
        return self.__distance

    @distance.setter
    def distance(self, value: type) -> None:
        if not isinstance(value, float):
            raise TypeError(f"Expected {float}, got {type(value)}")
        if value <= 0:
            raise ValueError(f"Distance cannot be less than or equal to zero, got {value}")
        self.__distance = value

    # ********** property duration - (setter/getter) ***********
    @property
    def duration(self) -> type:
        """ The duration property. """
        return self.__duration

    @duration.setter
    def duration(self, value: type) -> None:
        if not isinstance(value, int):
            raise TypeError(f"Expected {int}, got {type(value)}")
        if value <= 0:
            raise ValueError(f"Duration cannot be equal to or less than 0, got {value}")
        self.__duration = value

    # ********** property reviews - (getter only) ***********
    @property
    def reviews(self) -> type:
        """ The reviews property. """
        return self.__reviews
