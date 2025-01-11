from model.Hotel import Hotel
from model.Hotelguest import Hotelguest


class HotelRepository:

    @staticmethod
    def read_hotel_guest(hotel : Hotel):
        print(f"Hotel {str(hotel.name)}")
        print("*"*75)
        print(f"These are the geusts present at the hotel {hotel.name}:")
        for guest in hotel.guests:
            print(f"Hotelguest: {str(guest)}")


    pass


#Testing purposes

# guest1 = Hotelguest(parlastname="Smith", parfirstname="John", parbalance=100, par_checked_in=True)
# guest2 = Hotelguest(parlastname="Doe", parfirstname="Jane", parbalance=50, par_checked_in=False)
# guest3 = Hotelguest(parlastname="Johnson", parfirstname="Alice", parbalance=200, par_checked_in=True)
# guest4 = Hotelguest(parlastname="Brown", parfirstname="Charlie", parbalance=0, par_checked_in=False)


# hotel1 = Hotel("Howest")


# hotel1.check_in("Smith", "John")
# hotel1.check_in("Doe", "Jane")
# hotel1.check_in("Johnson", "Alice")
# hotel1.check_in("Brown", "Charlie")


# hotelRepository = HotelRepository()
# hotelRepository.read_guests(hotel=hotel1)