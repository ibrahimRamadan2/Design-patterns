from abc import ABC
from tax_utils import Product,CustomerStatus,UsEssentialProduct,UsLuxuryProduct,UsPremiumCustomer,UsStandardCustomer


class TaxCalculator(ABC):
    
    def __init__(self, params) -> None:
        self.customer_status = params["customer_status"]
        self.product_type = params["product_type"]
        self.country_name = params["country_name"]
        self.params = params
 
        
    def find_country_product_strategy(self):
        class_name = eval(f"{self.country_name.title()}{self.product_type.title()}{self.customer_status.title()}")
        return class_name()
    
    def calculate_tax(self,price):
        #  get CountryProductType tax
        country_product_tax = self.get_country_product_tax(self.params) # change params 
        #  get CountryCustomerStatux discount 
        country_customer_tax = self.get_country_customer_tax(self.params) # change params
        #  return the result .......
        # 1000$ , 10 , 12 
        tax = (price * country_product_tax / 100) - (price * country_customer_tax / 100)
        return tax

    
    def get_country_product_tax(self, params): 
        # UsEsseitial
        class_name = eval(f'{params["country_name"].title()}{params["product_type"].title()}Product')
        class_obj = class_name(params)
        return class_obj.get_tax_rate()
     
    def get_country_customer_tax(self, params):
        class_name = eval(f'{params["country_name"].title()}{params["customer_status"].title()}Customer') 
        class_obj = class_name() 
        return class_obj.get_discount()