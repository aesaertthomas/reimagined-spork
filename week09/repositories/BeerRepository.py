#Simple imports
import json
import os
import json

#From imports
from typing import List

#Own classes imports
from ..model.Beer import Beer

class BeerRepository:

    @staticmethod
    def __reading_local_json_file(filename: str):
        fo = open(filename)
        response_json = fo.read()
        fo.close()
        return json.loads(response_json)

    @staticmethod
    def load_beers():
        current_dir = os.path.dirname(__file__) #Gets the direcotry the script is running in
        beer_path = os.path.join(current_dir, '..','doc','beers.json') #Construct the path to get to the beers.json file

        beers_data = BeerRepository.__reading_local_json_file(beer_path)

        return beers_data

    @staticmethod
    def filter_beers_brewery(list_beers : list[Beer], searched_brewery : str) -> List[Beer]:
        result = []
        for beer in list_beers:
            if beer.brewery == searched_brewery:
                result.append(beer)
        return result


BeerRepository.load_beers()
