import  json
from datetime import datetime

class HighwayRepository:

    @staticmethod
    def __read_local_json_file(filename: str):
        fo = open(filename)
        response_json = fo.read()
        fo.close()
        return json.loads(response_json)

    @staticmethod
    def load_highways():
        dict_highways = HighwayRepository.__read_local_json_file("../doc/highways.json")
        highways = dict_highways['highways']
        for entry in highways:
            for key, value in entry.items():
                #Traffic jams is structured as a list of dictionaries
                if key == "traffic_jams":

                    print("Traffic Jams: ")
                    for traffic_jam in value: #list
                        info = "Traffic jam at "
                        info += f"{traffic_jam["location"]}"
                        info += f" -  {datetime.fromisoformat(traffic_jam["time"])}"
                        info += f" (length: {traffic_jam["length_km"]}, "
                        info += f"cause: {traffic_jam["cause"]})"

                        print(info)

                else:
                    print(f"{key} : {value}")

            print() #Whitespace between highway entries

    @staticmethod
    def filter_very_busy_highways(list_highways : list):
        busy_highways = []

        highways = list_highways['highways']
        for entry in highways:
            if entry['daily_traffic_intensity'] >= 100000:
                busy_highways.append(entry["routeID"])

        return busy_highways

    @staticmethod
    def filter_long_traffic_jams(list_highways : dict, min_length_traffic_jam : float) -> list:
        criteria_meeting_traffic_jams = []
        highways = list_highways['highways']

        for entry in highways:
            for key, value in entry.items():
                #Traffic jams is structured as a list of dictionaries
                if key == "traffic_jams":

                    for traffic_jam in value: #list
                        if traffic_jam["length_km"] >= min_length_traffic_jam:

                            info = "Traffic jam at "
                            info += f"{traffic_jam["location"]}"
                            info += f" -  {datetime.fromisoformat(traffic_jam["time"])}"
                            info += f" (length: {traffic_jam["length_km"]}, "
                            info += f"cause: {traffic_jam["cause"]})"

                            criteria_meeting_traffic_jams.append(info)

        return criteria_meeting_traffic_jams
# HighwayRepository.load_highways()

list_highways = HighwayRepository._HighwayRepository__read_local_json_file("../doc/highways.json") #name mangling not
#
# best approach
# busy_highways = HighwayRepository.filter_very_busy_highways(list_highways)
# print("\nThe very busy highways are those with a minimum of 100.000 vehicles per day.")
# print(f"These are: {busy_highways}")


selected_min_length_traffic_jams = float(input("\nEnter a minimum length of traffic jam: "))
print("Traffic jams that meet this criterion are: ")
searched = HighwayRepository.filter_long_traffic_jams(list_highways=list_highways,min_length_traffic_jam=selected_min_length_traffic_jams)

for traffic_jam in searched:
    print(traffic_jam)
