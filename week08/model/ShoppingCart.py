class ShoppingCart:

    def __init__(self) -> None:
        #list of products
        self.__products = [] 

    # ********** property products - (only getter) ***********
    @property
    def products(self) -> list[str]:
        """ The products property. """
        return self.__products
    
    def add_product(self, new_product: str) -> None:
        self.products.append(new_product)

    def remove_product(self, removing_product: str) -> None:
        if removing_product in self.products:
            self.products.remove(removing_product)    


     


