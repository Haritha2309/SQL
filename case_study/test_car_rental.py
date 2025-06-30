import unittest
from entity.vehicle import Vehicle
from entity.lease import Lease
from entity.customer import Customer
from dao.I_Car_Lease_Repo_Impl import ICarLeaseRepoImpl
from Exception.CarNotFound import CarNotFoundException
from Exception.CustomerNotFound import CustomerNotFoundException
from Exception.LeaseNotFound import LeaseNotFoundException
from datetime import datetime,timedelta

class TestCarRental(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.repo = ICarLeaseRepoImpl()
    def test_add_car_and_find_by_id(self):
        car = Vehicle(None,"Honda","Civic",2021,3500,"Available",5,1500)
        saved= self.repo.add_car(car)
        fetched_car = self.repo.FindCarById(saved.vehicle_id)

        self.assertIsNotNone(fetched_car)
        self.assertEqual(fetched_car.vehicle_make,"Honda")

   

    def test_creat_lease_successful(self):
        car = Vehicle(None,"Hyundai","i20",2021,200,"Available",5,1200)
        car = self.repo.add_car(car)

        customer = Customer(None,"John","Lae","jonny@gmail.com","111-555-9876")
        customer = self.repo.add_customer(customer)
        start_date = datetime(2025, 6, 21).date()
        end_date = datetime(2025, 9, 8).date()
        lease = self.repo.create_lease(customer.customer_id,car.vehicle_id,start_date,end_date)
        
        self.assertIsNotNone(lease)
        self.assertIsInstance(lease,Lease)
        self.assertIsNotNone(lease.lease_id)
    
    def test_retrive_lease_success(self):
        car = Vehicle(None,"Toyota","Yaris",2022,205,"Available",5,2500)
        car = self.repo.add_car(car)

        customer = Customer(None,"Alice","Smith","alie@gmail.com","666-555-9874")
        customer = self.repo.add_customer(customer)

        start_date = datetime.now().date()
        end_date = start_date + timedelta(days = 45)
        lease = self.repo.create_lease(customer.customer_id,car.vehicle_id,start_date,end_date)
        leases = self.repo.ListLeaseHistory()

        found = any(l.lease_id == lease.lease_id for l in leases)
        self.assertTrue(found,f"Lease with ID {lease.lease_id} should be in the lease History.")

    def test_find_customer_with_invalid_id(self):
        invalid_id = -1
        with self.assertRaises(CustomerNotFoundException):
            self.repo.FindCustomerById(invalid_id)

    def test_find_car_with_invalid_id(self):
        invalid_id = -1
        with self.assertRaises(CarNotFoundException):
            self.repo.FindCarById(invalid_id)
        
    def test_invalid_lease_id(self):
        invalid_id = -1
        with self.assertRaises(LeaseNotFoundException):
            self.repo.return_car(invalid_id)