class LeaseNotFoundException(Exception):
    def __init__(self,message = "Lease_Id not found in DataBase. "):
        super().__init__(message)