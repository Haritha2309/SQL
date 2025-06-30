class Customer:
    def __init__(self,customer_id,first_name,last_name,email,phone_number):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        
    def __str__(self):
        return(
            "-------CUSTOMER DETAILS----\n"
            f"CUSTOMER ID --> {self.customer_id}\n"
            f"FIRST NAME ---> {self.first_name}\n"
            f"LAST NAME ----> {self.last_name}\n"
            f"EMAIL --------> {self.email}\n"
            f"PHONE NUMBER -> {self.phone_number}\n"
        )