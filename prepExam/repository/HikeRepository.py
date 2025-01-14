import json

from datetime import datetime

from model.Review import Review
from model.Hike import Hike

class HikeRepository:

    def load_file(filename : str) -> dict:
        fo = open(filename, "r")
        data = json.loads(fo.read())
        fo.close()
        return data

    def load_hikes(filename : str) -> list:

        file = HikeRepository.load_file(filename=filename)
        data = file["data"]
        hikes = []

        for hike_dict in data:
            id = hike_dict['id']
            name = hike_dict['name']
            description = hike_dict['description']
            city = hike_dict['city']
            if not city:
                city = "None"
            duration = hike_dict['duration']
            if duration <= 0:
                continue #break out of loop, If the duration is none the hike is worthless
            difficulty = hike_dict["difficulty"]["name"]
            distance = float(hike_dict["distance"])


            hike_object = Hike(parid=id, parcity=city, parname=name, pardescription=description, parduration=duration, pardifficulty=difficulty, pardistance=distance)
            #Created hike object already because 1 all needed params already pulled, and 2 more optimal to do now and append reviews directly into object
            for review in hike_dict['reviews']:
                user = review['user']
                comment = review['comment']
                rating = review['rating']
                format = "%Y-%m-%d"
                date = datetime.strptime(review['date'], format)
                review_object = Review(paruser=user, parcomment=comment, parrating=rating, parratingdate=date)
                #appending reviews into hike object
                hike_object.add_review(review=review_object)

            hikes.append(hike_object)

        return hikes

    @staticmethod

    def search_in_hikes(hikes : list, search_term : str) -> list:
        matching_hikes = []
        search_term = search_term.lower()

        for hike in hikes:
            if (search_term in hike.name.lower()) or (search_term in hike.city.lower()):
                matching_hikes.append(hike)

        return matching_hikes

    def  sort_hikes_by_difficulty(list_objects : list) -> dict:

        dict_hikes = {"Easy": [], "Average" : [], "Difficult" : []} #Creating dict with difficulties already made
        for hike in list_objects:
            dict_hikes[hike.difficulty].append(hike) #Directly inserting into correct list of difficulty

        return dict_hikes


    def filter_hikes_by_difficulty_duration(dict_hikes : dict, wanted_difficulty : str, max_duration : float) -> list:
        list_hikes_difficulty = dict_hikes[wanted_difficulty]
        filtered_hikes = []

        for hike in list_hikes_difficulty:
            if hike.duration <= max_duration:
                filtered_hikes.append(hike)

        return filtered_hikes

    def sort(list_objects : list) -> list:
        pass
