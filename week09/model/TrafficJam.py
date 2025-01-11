import datetime as datetime

class TrafficJam:

    def __init__(self, parlocation : str, parlength : float, partimestamp : datetime, parcause : str, parweather_conditions : str):
        self.location = parlocation
        self.length = parlength
        self.timestamp = partimestamp
        self.cause = parcause
        self.weather_conditions = parweather_conditions


    def __str__(self) -> str:
        info = f"\nLocation: {self.location}\nLength: {self.length}\nTimestamp: {self.timestamp.strftime('%d/%m/%Y %H:%M')}\nCause: {self.cause}\nWeather Conditions: {self.weather_conditions}\n"
        return info

    # ********** property location - (setter/getter) ***********
    @property
    def location(self) -> type:
        """ The location property. """
        return self.__location

    @location.setter
    def location(self, value: type) -> None:
        if not isinstance(value, str):
            raise TypeError("New location is supposed to be of type string")
        self.__location = value
    # ********** property length - (setter/getter) ***********
    @property
    def length(self) -> type:
        """ The length property. """
        return self.__length

    @length.setter
    def length(self, value: type) -> None:
        if not isinstance(value, float):
            raise TypeError("New length is supposed to be of type float")
        self.__length = value
    # ********** property timestamp - (setter/getter) ***********
    @property
    def timestamp(self) -> type:
        """ The timestamp property. """
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, value: type) -> None:
        self.__timestamp = value
    # ********** property cause - (setter/getter) ***********
    @property
    def cause(self) -> type:
        """ The cause property. """
        return self.__cause

    @cause.setter
    def cause(self, value: type) -> None:
        if not isinstance(value, str):
            raise TypeError("New cause is not of type string")
        self.__cause = value
    # ********** property weather_conditions - (setter/getter) ***********
    @property
    def weather_conditions(self) -> type:
        """ The weather_conditions property. """
        return self.__weather_conditions

    @weather_conditions.setter
    def weather_conditions(self, value: type) -> None:
        if not isinstance(value, str):
            raise TypeError("New weather_conditions are not of type string")
        self.__weather_conditions = value


bogus_entry = {
    "parlocation": "Middle of Nowhere",
    "parlength": 42.0,
    "partimestamp": datetime.datetime(2023, 7, 21, 14, 35),
    "parcause": "Alien landing",
    "parweather_conditions": "Partly cloudy with a chance of UFOs"
}


instance = TrafficJam(**bogus_entry)
print(instance)
