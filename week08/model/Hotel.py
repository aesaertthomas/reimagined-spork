from model.Hotelguest import Hotelguest

class Hotel:
    

    def __init__(self, parname : str): 
        self.name = parname
        self.__guests = []

    # ********** property name - (setter/getter) ***********
    @property
    def name(self) -> type:
        """ The name property. """
        return self.__name
    
    @name.setter
    def name(self, value: type) -> None:
        if type(value) != str:
            raise TypeError("Your new hotelname has to be a string")
    
        if value == "":
            raise ValueError("Your new hotelname cannot be empty")
    
        self.__name = value
    
    # ********** property guests - (getter only) ***********
    @property
    def guests(self) -> type:
        """ The guests property. """
        return self.__guests
    
    


    # ********** property guests - (getter only) ***********
    @property
    def guests(self) -> type:
        """ The guests property. """
        return self.__guests
    
    def check_in(self, lastname : str, firstname : str):
        new_guest = Hotelguest(parfirstname=firstname, parlastname=lastname)
        
        #Check wether guest alr in lst
        if new_guest not in self.guests:
            self.__guests.append(new_guest)

            #Altr checked_in
            for guest in self.guests:    

                if guest.firstname == lastname and guest.lastname == lastname:
                    guest.is_checked_in(True)
                    
                    #Printing message
                    print(f"Succesfully checked in {str(guest)}")

        else:
            raise ValueError("Hotelguest is already in hotel")
    

    def check_out(self, firstname: str, lastname: str):
        #Find the guest by first and last names
        guest = self.__search_hotelguest(firstname=firstname, lastname=lastname)
        if guest:
            if guest.balance != 0.0:
                    print("The guest still has an unpaid balance and therefore cannot be checked out yet:")
                    print(f"Hotelguest: {str(guest)} - checked in: True (balance: {guest.balance} euro)")
            else:
                guest.is_checked_in = False
                self.guests.remove(guest)
            
    
    def print_info_guests(self):
        print(f"These are the guests present in the hotel {self.name}")
       
        for guest in self.guests:
            print(f"Hotelguest: {str(guest)}")
        
    def __search_hotelguest(self, lastname, firstname):

        for guest in self.guests:
            if guest.firstname == firstname and guest.lastname == lastname:
                return guest
        
        raise ValueError(f"{str(guest)} not present in hotel")

    def balance_paid_by_guest(self, name, firstname):
        
        searched_guest = self.__search_hotelguest(lastname=name, firstname=firstname)
        if not isinstance(searched_guest, Hotelguest): #If the ojbect that is returned is of the type hotelguest
            return #:using a return statement to end the function

        searched_guest.balance(0.0)


        pass    

    @staticmethod
    def add_guest(self, guest : Hotelguest):
        self.__guests.append(guest)

