from model.TrafficJam import TrafficJam

class Highway:

    def __init__(self, parid : str, partotallength : float, parintensity : int, paryear_of_construction : int, parnumber_of_lanes : int):
        self.id = parid
        self.totallength = partotallength
        self.intensity = parintensity
        self.year_of_construction = paryear_of_construction
        self.number_of_lanes = parnumber_of_lanes
        self.__traffic_jams = []

    def __str__(self) -> str:
        info = f""
        return info
    def __repr__(self) -> str:
        info = f""
        return info

    def __eq__(self, other) -> bool:
        if not isinstance(other, Highway):
            raise TypeError(f"{other} has to be of type {Highway}")
        if (str(self) == str(other)):
            return True

    def add_traffic_jam(self, traffic_jam : TrafficJam):
        if not isinstance(traffic_jam, TrafficJam):
            raise TypeError(f"{traffic_jam} is not of type {type(TrafficJam)}")
        if traffic_jam not in self.traffic_jams:
            self.__traffic_jams.append(traffic_jam)

    def print_traffic_jams(self):
        for traffic_jam in self.traffic_jams:
            print(traffic_jam)


#------------------------------ Properties -----------------------------------------------
    # Getter and setter for id
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, str):
            raise TypeError("id must be an string")
        self._id = value

    # Getter and setter for totallength
    @property
    def totallength(self):
        return self._totallength

    @totallength.setter
    def totallength(self, value):
        if not isinstance(value, float):
            raise TypeError("totallength must be a float")
        self._totallength = value

    # Getter and setter for intensity
    @property
    def intensity(self):
        return self._intensity

    @intensity.setter
    def intensity(self, value):
        if not isinstance(value, int):
            raise TypeError("intensity must be an integer")
        self._intensity = value

    # Getter and setter for year_of_construction
    @property
    def year_of_construction(self):
        return self._year_of_construction

    @year_of_construction.setter
    def year_of_construction(self, value):
        if not isinstance(value, int):
            raise TypeError("year_of_construction must be an integer")
        self._year_of_construction = value

    # Getter and setter for number_of_lanes
    @property
    def number_of_lanes(self):
        return self._number_of_lanes

    @number_of_lanes.setter
    def number_of_lanes(self, value):
        if not isinstance(value, int):
            raise TypeError("number_of_lanes must be an integer")
        self._number_of_lanes = value

    # Getter for traffic_jams
    @property
    def traffic_jams(self):
        return self.__traffic_jams
