class CarNotFoundException(Exception):
    def __init__(self,message = "Car_Id not found in DataBase. "):
        super().__init__(message)