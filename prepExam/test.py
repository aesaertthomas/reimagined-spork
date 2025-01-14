from datetime import datetime

from model.Review import Review
from model.Hike import Hike

from repository.HikeRepository import HikeRepository

list_hikes = HikeRepository.load_hikes(filename="doc/hike_EN.json")

print("Length of list hikes: ", len(list_hikes))
dict_hikes = HikeRepository.sort_hikes_by_difficulty(list_hikes)

filtered_hikes = HikeRepository.filter_hikes_by_difficulty(dict_hikes, "Easy", 100)

for hike in filtered_hikes:
    print(f"{hike}, Duration: {hike.duration}, Difficulty: {hike.difficulty}")
