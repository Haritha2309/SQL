class CustomerNotFoundException(Exception):
    def __init__(self,message = "Customer_Id not found in DataBase. "):
        super().__init__(message)