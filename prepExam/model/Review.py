from datetime import datetime

class Review:

    def __init__(self, paruser : str, parcomment : str, parratingdate : datetime = datetime.now(), parrating : int = 3):
        self.user = paruser
        self.comment = parcomment
        self.ratingdate = parratingdate
        self.rating = parrating

    # ********** property user - (setter/getter) ***********
    @property
    def user(self) -> type:
        """ The user property. """
        return self.__user

    @user.setter
    def user(self, value: type) -> None:
        if not isinstance(value, str):
            raise TypeError(f"Expected {str}, got {type(value)}")
        self.__user = value

    # ********** property comment - (setter/getter) ***********
    @property
    def comment(self) -> type:
        """ The comment property. """
        return self.__comment

    @comment.setter
    def comment(self, value: type) -> None:
        if not isinstance(value, str):
            raise TypeError(f"Expected {str}, got {type(value)}")
        self.__comment = value

    # ********** property ratngdate - (setter/getter) ***********
    @property
    def ratingdate(self) -> type:
        """ The ratngdate property. """
        return self.__ratngdate

    @ratingdate.setter
    def ratingdate(self, value: type) -> None:
        if not isinstance(value, datetime):
            raise TypeError(f"Expected {datetime}, got {type(value)}")
        self.__ratngdate = value

    # ********** property rating - (setter/getter) ***********
    @property
    def rating(self) -> type:
        """ The rating property. """
        return self.__rating

    @rating.setter
    def rating(self, value: type) -> None:
        if not isinstance(value, int):
            raise TypeError(f"Expected {int}, got {type(value)}")
        self.__rating = value

    def __str__(self) -> str:
        info = f"{self.comment} {self.user} [{self.ratingdate}]"
        return info

    def __repr__(self) -> str:
        info = f"{self.comment} {self.user}"
        return info


    def __lt__(self, other) -> bool:
        if not isinstance(other, Review):
            raise TypeError(f"Expected {Review}, got {type(other)}")
        return (self.rating < other.rating)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Review):
            raise TypeError(f"Expected {Review}, got {type(other)}")
        return ((self.user == other.user) & (self.comment == other.comment))

    def get_detail_info(self) -> str:
        info = (
            f"Review from {self.user.upper()}:\n"
            f"\t- Comment: {self.comment}\n"
            f"\t- Rating: {self.rating}\n"
            f"\t- Date: {self.ratingdate}\n"
        )
