class Customer:
    all_customers =[]

    def __init__(self,customer_id,first_name,last_name,email,phone,address):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address
        self.orders= []

        Customer.all_customers.append(self)


    def calculate_total_orders(self):
        return len(self.orders)
    
    def get_customer_details(self):
        return(f"CUSTOMER ID  --> {self.customer_id}\n"
                   f"NAME --->{self.first_name} {self.last_name}\n"
                   f"EMAIL ---> {self.email}\n"
                   f"PHONE --> {self.phone}\n"
                   f"ADDRESS --> {self.address}")
    
    def update_customer(self,email = None,phone = None,address = None):
        if email:
            self.email = email
        if phone:
            self.phone = phone
        if address:
            self.address = address
    @staticmethod
    def find_customer_by_id(customer_id):
        for customer in Customer.all_customers:
            if customer.customer_id == customer_id:
                return customer
        return None
         
