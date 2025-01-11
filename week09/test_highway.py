from datetime import datetime

from model.TrafficJam import TrafficJam
from model.Highway import Highway


highway_E403 = Highway("E403",60.5,50000,1985, 2)
trafficjam1 = TrafficJam("Roeselare",2.5,datetime.now(),"Accident","Fog")
trafficjam2 = TrafficJam("Brugge",3.7,datetime.now(),"Roadworks on the highway","Sunny")
highway_E403.add_traffic_jam(trafficjam1)
highway_E403.add_traffic_jam(trafficjam2)
print(highway_E403)
print()
highway_E403.print_traffic_jams()
