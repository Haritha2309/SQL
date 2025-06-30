from abc import ABC,abstractmethod

class ICarLeaseRepositary(ABC):
    @abstractmethod
    def add_car(self,car): pass
    @abstractmethod
    def remove_car(self,car_Id): pass
    @abstractmethod
    def listAvailableCars(self): pass
    @abstractmethod
    def ListRentedCars(self) : pass
    @abstractmethod
    def FindCarById(self,car_Id): pass

    @abstractmethod
    def add_customer(self,customer): pass
    @abstractmethod
    def remove_customer(self,customer_Id): pass
    @abstractmethod
    def listcustomer(self): pass
    @abstractmethod
    def FindCustomerById(self,customer_Id): pass

    @abstractmethod
    def create_lease(self,customer_Id,car_Id,start_date,end_date): pass
    @abstractmethod
    def return_car(self,lease_Id): pass
    @abstractmethod
    def ListActiveLeases(self):pass
    @abstractmethod
    def ListLeaseHistory(self): pass

    @abstractmethod
    def record_payemnt(self,lease_Id,amount): pass
    @abstractmethod
    def get_payment_history(self,customer_Id): pass
    @abstractmethod
    def get_total_payment(self): pass
    