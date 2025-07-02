from products import Product
from datetime import datetime
class Inventory:
    all_inventories = []
    def __init__(self,inventory_id,product,quantity_in_stock):
        self.inventory_id = inventory_id
        self.product = product
        self.quantity_in_stock = quantity_in_stock
        self.last_stock_update = datetime.mow()
        
        Inventory.all_inventories.append(self)

    def get_product(self):
        return self.product
    
    def get_quantity_in_stock(self):
        return self.quantity_in_stock
    
    def add_to_inventory(self,quantity):
        self.quantity_in_stock+= quantity
        self.last_stock_update = datetime.now()

    def remove_from_inventor(self,quantity):
        if quantity<=self.quantity_in_stock:
            self.quantity_in_stock-=quantity
            self.last_stock_update = datetime.now()
        else:
            raise ValueError("Not Enough Stock")
        
    def update_stock(self,quantity):
        self.quantity_in_stock = quantity
        self.last_stock_update = datetime.now()

    def is_product_available(self,quantity):
        return self.quantity_in_stock >= quantity
    
    def get_inventory_value(self):
        return self.quantity_in_stock * self.product.price
    
    @classmethod
    def list_low_stock_products(cls,threshold):
        return [ inv for inv in cls.all_inventories if inv.quantity_in_stock < threshold]
    
    @classmethod
    def list_out_of_stock_products(cls):
        return[ inv for inv in cls.all_inventories if inv.quantity_in_stock == 0]
    
    @classmethod
    def list_all_products(cls):
        return [ (inv.product.product_name,inv.quantity) for inv in cls.all_inventories]
