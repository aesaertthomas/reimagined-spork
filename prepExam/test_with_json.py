from repository.HikeRepository import HikeRepository

print("****1) reading hikes ****")
list_hikes = HikeRepository.load_hikes("doc/hike_EN.json")
print(f"Number of walks: {len(list_hikes)}")
print(list_hikes)

print("\n****2) sorting hikes + print detail info****")
list_hikes.sort()
for hike in list_hikes:
    print(hike.get_detail_info())

print("\n****3) filter hikes ****")
search_pattern = input("Enter a (part of a) city or name of the walk:> ")
print("These are the search results:")
for hike in HikeRepository.search_in_hikes(list_hikes,search_pattern):
    print(hike.get_detail_info())

print("\n****4) sort hikes on  difficulty****")
dict_result = HikeRepository.sort_hikes_by_difficulty(list_hikes)
for difficulty, list_hikes in dict_result.items():
    print(f"* Difficulty {difficulty}:")
    print(f"{list_hikes}")

print("\n****5) filter hikes on difficulty and duration****")
max_duration = int(input("Enter a maximum duration:> "))
difficulty = input("Enter a difficulty:> ")
list_result = HikeRepository.filter_hikes_by_difficulty_duration(dict_result, difficulty, max_duration)
print("These are the search results:")
for hike in list_result:
    print(hike.get_detail_info())
