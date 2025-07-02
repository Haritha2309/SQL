from orders import Orders
from products import Product
class Order_details:
    def __init__(self,order_detail_id,order,product,quantity):
        self.order_detail_id = order_detail_id
        self.order = order
        self.product = product
        self.quantity = quantity
        self.discount = 0

        order.order_details.append(self)
    
    def calculate_subtotal(self):
        subtotal = self.product.price * self. quantity
        if self.discount:
            subtotal *= ( 1 - self.discount)
        return subtotal
    
    def get_order_details_info(self):
        return (
            f"PRODUCT --> {self.product.product_name}\n"
            f"QUANTITY --> {self.quantity}\n"
            f"PRICE --> {self.product.price}\n"
            f"SUBTOTAL --> {self.calculate_subtotal()}"
        )
    
    def update_quantity(self,quantity):
        self.quantity = quantity

    def add_discount(self,discount):
        self.discount = discount
        