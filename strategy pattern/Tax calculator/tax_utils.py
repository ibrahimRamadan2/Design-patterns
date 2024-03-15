from abc import ABC


class  Product(ABC):
    def __init__(self, params) -> None:
        self.price= 0 
        self.tax_rate=0 
        self.params = params
         
    def get_tax_rate(self):
        return self.tax_rate
    

class UsLuxuryProduct(Product):
    def __init__(self, params) -> None:
        super().__init__(params) 
        self.tax_rate = 7 + 3       # 7% is the the tax and 3% as it's luxury 
    

class UsEssentialProduct(Product):
    def __init__(self, params) -> None:
        super().__init__(params) 
        self.tax_rate = 7   # just 7% as normal tax
    
    
    
class CustomerStatus(ABC):
    def __init__(self) -> None:
        self.discount = 0  
        
    def get_discount(self):
        return self.discount
    
class UsStandardCustomer(CustomerStatus): 
    def __init__(self) -> None:
        self.discount = 0  
    
class UsPremiumCustomer(CustomerStatus): 
    def __init__(self) -> None:
        self.discount = 1 
        
 
    
    
 
