from inventory import Inventory
class Product:
    def __init__(self,product_id,product_name,description,price):
        self.product_id = product_id
        self.product_name = product_name
        self.description = description
        self.price = price

    def product_details(self):
        return(
            f"PRODUCT ID --> {self.product_id}\n"
            f"PRODUCT NAME --> {self.product_name}\n"
            f"DESCRIPTION --> {self.description}\n"
            f"PRICE --> {self.price}"
        )
    
    def update_product_info(self,product_name=None,description =None,price = None):
        if product_name:
            self.product_name = product_name
        if description :
            self.description = description
        if price:
            self.price = price

    def product_in_stock(self,inventory):
        return inventory.get_quantity_in_stock() > 0

