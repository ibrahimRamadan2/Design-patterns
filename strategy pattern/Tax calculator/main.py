from abc import ABC
from tax_calculator import TaxCalculator



def take_input():
    params ={}
    # country list can expand 
    params["country_name"] = str(input("[*] Please enter Country name from this List [US]:  "))
    params["product_type"] = str(input("[*] Please enter product type from this List [Luxury , Essential]: "))
    params["customer_status"] = str(input("[*] Please enter customer status from this List [Standard , Premium]: "))
    params["product_cost"]  = int(input("[*] Please enter product price (price should be a number): "))
    
    # validation should be added here

    return params



if __name__ == '__main__':
    params = take_input()
    tax_calculator = TaxCalculator(params)
    print(f"Your product tax = {round(tax_calculator.calculate_tax(params["product_cost"]), 2)}$  ^_^")