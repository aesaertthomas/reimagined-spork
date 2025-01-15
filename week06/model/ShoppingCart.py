# EX06
# step 1: create a class 'ShoppingCart'
# step 2: add properties for each attribute. An attribute can also be a list
# step 3: add the constructor
# step 4: add the toString-method
# step 5: Add additional common methods
class ShoppingCart:
    #2
    def __init__(self):
        self.__products = []

    #3
    # ********** property products - (setter/getter) ***********
    @property
    def products(self) -> type:
        """ The products property. """
        return self.__products
    
    @products.setter
    def products(self, value: type) -> None:
        self.__products = value
    
    #4
    def __str__(self) -> str:
        info = f"{self.products}"
        return info
    
    #5
    def add_product(self, new_product : str):
        self.products.append(new_product)

    def remove_product(self, product : str):
        self.products.remove(product)