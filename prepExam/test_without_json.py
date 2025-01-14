from model.Review import Review
from model.Hike import Hike
from datetime import datetime

def create_reviews():
    print("\n*** Test 1 ***")
    print('*** 1a) creating a review')
    review1 = Review("Stijn", "Nice walk in the forest")
    print(review1)

    print('*** 1b) printing details of a review')
    print(review1.get_detail_info())

    print('*** 1c) testing equality between two reviews')
    review2 = Review("Marie", "Boring walk on the beach", datetime(2022,11,10), 1)
    review3 = Review("Marie", "Boring walk on the beach", datetime(2022,11,10), 2)
    if review2 == review3:
        print("Review2 and review3 are equal")
    else:
        print("Review2 and review3 are not equal")


    print("** 1d) Sorting and printing of a list")
    my_list = [review1, review2]
    print(f"Not sorted: {my_list}")
    my_list.sort()
    print(f"Sorted on rating: {my_list}")

def create_hikes():
    print("\n*** Test 2 ***")
    print('*** 2a) creating a hike')
    hike1 = Hike(1, "Kortrijk", "Discover Howest", "Nice walk around the Penta", 12.5, 120, "Easy")
    print(hike1)
    print(hike1.get_detail_info())

    print("** 2b) Sorting and printing of a list")
    hike2 = Hike(2, "Gent", "Explore city Gent", "The hike was a unique experience", 10.0, 95, "Average")
    my_list = [hike1, hike2]
    print(f"Not sorted: {my_list}")
    my_list.sort()
    print(f"Sorted on rating: {my_list}")

def create_hikes_with_reviews():
    print("\n*** Test 3 ***")
    print('*** 3a) creating a hike with reviews')
    hike1 = Hike(1, "Kortrijk", "Discover Howest", "Nice walk around the Penta", 12.5, 120, "Easy")
    hike1.add_image("https://source.unsplash.com/random/800x600/?sig=72&walk")
    hike1.add_image("https://source.unsplash.com/random/800x600/?sig=69&walk")
    review1 = Review("Stijn", "Boring walk", datetime(2022,11,10), 1)
    review2 = Review("Marie", "Nice walk in the forest", datetime(2022,9,20), 4)
    hike1.add_review(review1)
    hike1.add_review(review2)
    print(hike1.get_detail_info())

    print('*** 3b) printing reviews of a hike')
    for review in hike1.reviews:
        print(review.get_detail_info())


def create_errors():
    print("\n*** Test 4 - Wrong input ***")
    try:
        review1 = Review("Marie", "Boring walk on the beach", datetime(2022,11,10), 100)
        print(review1)
    except Exception as ex:
        print(f"Error: {ex}")

    try:
        hike1 = Hike(1, "Kortrijk", "Discover Howest", "Nice walk around the Penta", 12.5, 120, "Easy")
        hike1.add_review("Nice hike!")
    except Exception as ex:
        print(f"Error: {ex}")


create_reviews()
# create_hikes()
# create_hikes_with_reviews()
# create_errors()
