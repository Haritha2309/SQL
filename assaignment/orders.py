from customer import Customer
from order_details import Order_details
from inventory import Inventory
from datetime import datetime
class Orders:
    def __init__(self,order_id,customer,order_date = None):
        self.order_id = order_id
        self.customer = customer
        self.order_date = order_date if order_date else datetime.now().date()
        self.total_amount = 0.0
        self.status = "Processing"
        self.order_details = []
        customer.orders.append(self)

    def calculate_total_amount(self):
        self.total_amount = sum(detail.calculate_subtotal() for detail in self.order_details)
        return self.total_amount
    
    def get_order_details(self):
        details = [detail.get_order_details_info() for detail in self.order_details]
        return(
            f"ORDER ID --> {self.order_id}\n"
            f"CUSTOMER NAME --> {self.customer.first_name} {self.customer.last_name}\n"
            f"DATE --> {self.order_date}\n"
            f"TOTAL AMOUNT --> {self.calculate_total_amount()}\n"
            f"STATUS --> {self.status}\n"
             f"ORDER ITEMS:\n" + "\n".join(details)
        )
    
    def order_status_update(self,status):
        self.status = status

    def cancel_order(self):
        self.status = "Cancelled"
        for detail in self.order_details:
            detail.inventory.add_to_inventory(detail.quantity)

    