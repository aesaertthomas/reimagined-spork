#Find the errors!!!!

class ShoppingCart:

    def __init__(self) -> None:
        self.__products = [] 

    # ********** property products - (only getter) ***********
    @property
    def products(self) -> list[str]:
        """ The products property. """
        return self.products   
    
    def __add_product(self, new_product: str) -> None:  
        self.products += new_product       

    def __remove_product(self, removing_product: str) -> None:  
        if removing_product in self.products:
            self.products -= removing_product   

    def __str__(self) -> str:
        return f"There are {len(self.products)} products in the shopping cart: {self.products}"

    def __add__(self) -> object: 
        w = ShoppingCart()
        for product in self.products:
            w.add_product(product)       
        return w        


