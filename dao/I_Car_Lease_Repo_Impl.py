from util.connection import Connection
from Exception.CarNotFound import CarNotFoundException
from Exception.CustomerNotFound import CustomerNotFoundException
from Exception.LeaseNotFound import LeaseNotFoundException
from dao.I_Car_Lease_Repo import ICarLeaseRepositary
from entity.customer import Customer
from entity.lease import Lease
from entity.payment import Payment
from entity.vehicle import Vehicle
from datetime import datetime

class ICarLeaseRepoImpl(ICarLeaseRepositary):
    def __init__(self):
        db = Connection()
        self.conn = db.get_connection()
        if self.conn is None:
            raise Exception ("connectivity failed")
        self.cursor = self.conn.cursor()
    
    def add_car(self, car):
        self.cursor.execute("""
            INSERT INTO Vehicle(vehicle_make,vehicle_model,vehicle_year,daily_rate,vehicle_status,passenger_capacity,engine_capacity)
            VALUES(?,?,?,?,?,?,?)""",
            (car.vehicle_make,car.vehicle_model,car.vehicle_year,car.daily_rate,car.vehicle_status,car.passenger_capacity,car.engine_capacity))        
        self.conn.commit()
        self.cursor.execute("SELECT TOP 1 * FROM vehicle ORDER BY vehicle_id DESC")
        row = self.cursor.fetchone()
        new_car = Vehicle(*row)
        print(new_car)
        car.vehicle_id = new_car.vehicle_id
        return new_car

    def remove_car(self, car_Id):
        self.cursor.execute("DELETE FROM VEHICLE WHERE vehicle_id = ?",(car_Id))
        if self.cursor.rowcount ==0:
            raise CarNotFoundException (f" Car with ID {car_Id} is not found.")
        self.conn.commit()
    
    def listAvailableCars(self):
        self.cursor.execute("""
            SELECT * 
            FROM Vehicle
            WHERE vehicle_status = 'Available'
            """)
        rows = self.cursor.fetchall()
        return [Vehicle(*row) for row in rows]
    def ListRentedCars(self):
        self.cursor.execute("""
            SELECT * 
            FROM Vehicle
            WHERE vehicle_status = 'Not Available'
            """)
        rows = self.cursor.fetchall()
        return [Vehicle (*row)  for row in rows ]
    
    def FindCarById(self, car_Id):
        self.cursor.execute("""
            SELECT * 
            FROM Vehicle 
            WHERE vehicle_id = ?
            """,(car_Id))
        result = self.cursor.fetchone()
        if not result:
            raise CarNotFoundException(f"Car with {car_Id} is not available")
        return Vehicle(*result)
        
    def add_customer(self, customer):
        self.cursor.execute("""
                            INSERT INTO Customer(first_name,last_name,email,phone_number)
                            VALUES (?,?,?,?)""",(customer.first_name,customer.last_name,customer.email,customer.phone_number))
        self.conn.commit()
        self.cursor.execute("SELECT TOP 1 * FROM customer ORDER BY customer_id DESC")
        row = self.cursor.fetchone()
        new_cus = Customer(*row)
        print(new_cus)
        return new_cus
    
    def remove_customer(self, customer_Id):
        self.cursor.execute("DELETE FROM Customer WHERE customer_id =?",(customer_Id))
        if self.cursor.rowcount == 0:
            raise CustomerNotFoundException (f"Customer with ID {customer_Id} is not found")
        self.conn.commit()

    def listcustomer(self):
        self.cursor.execute("SELECT * FROM customer")
        rows = self.cursor.fetchall()
        return [Customer(*row) for row in rows]
    
    def FindCustomerById(self, customer_Id):
        self.cursor.execute("SELECT * FROM Customer WHERE customer_Id = ?",(customer_Id))
        row= self.cursor.fetchone()
        if not row:
            raise CustomerNotFoundException (f" Customer with ID {customer_Id} is not found")
        return Customer(*row)
    
    def create_lease(self, customer_Id, car_Id, start_date, end_date):
        car_obj = self.FindCarById(car_Id)
        customer_obj = self.FindCustomerById(customer_Id)
        self.cursor.execute("UPDATE Vehicle SET vehicle_status = 'Not Available' WHERE vehicle_Id = ?",(car_Id))
        
        if (end_date - start_date).days<=30:
            lease_type = "daily"
        else:
            lease_type = "Monthly"
        self.cursor.execute("""
                        INSERT INTO lease(vehicle_Id,Customer_Id,start_date,end_date,type)
                        VALUES(?,?,?,?,?)
                            """,(car_Id,customer_Id,start_date,end_date,lease_type))
        self.conn.commit()
        self.cursor.execute("SELECT TOP 1 * FROM lease ORDER BY lease_id DESC")
        row = self.cursor.fetchone()
        return Lease(*row)

    def return_car(self, lease_Id):
        self.cursor.execute("SELECT * FROM lease where lease_Id = ?",(lease_Id))
        row = self.cursor.fetchone()
        if not row:
            raise LeaseNotFoundException(f"Car with lease ID {lease_Id} is not found")
        vehicle_id = row[0]
        self.cursor.execute("UPDATE Vehicle SET vehicle_status = 'Available' WHERE vehicle_Id = ?",(vehicle_id))
        self.conn.commit()
        print(f"Car with Vehicle_ID {vehicle_id} is now available")

    def ListActiveLeases(self):
        self.cursor.execute("SELECT * FROM lease WHERE end_date >= ?",(datetime.now().date()))
        rows = self.cursor.fetchall()
        return [Lease (*row) for row in rows]
    
    def ListLeaseHistory(self):
        self.cursor.execute("SELECT * FROM Lease")
        rows = self.cursor.fetchall()
        return [ Lease(*row ) for row in rows]
    
    def record_payemnt(self, lease_Id, amount):
        self.cursor.execute("SELECT * FROM payment WHERE lease_id = ?",(lease_Id))
        if self.cursor.fetchone()[0] ==0:
            raise LeaseNotFoundException (f"LEASE ID {lease_Id} is not found")
        self.cursor.execute("SELECT amount FROM payment WHERE lease_id =?",(lease_Id))
        row = self.cursor.fetchone()    
        exis_amount = float(row[0])
        new = float(exis_amount + amount)
        tdy = datetime.now().date().strftime('%Y-%m-%d')
        self.cursor.execute(""" UPDATE payment 
                            SET amount=?,payment_date =?
                            WHERE lease_id =?""",(new,tdy,lease_Id))
        self.conn.commit
        print(f"PAYMENT UPDATED SUCCESSFULLY. THE TOTAL PAID AMOUNT FOR THE LEASE ID -> {lease_Id} is {new}")

    def get_payment_history(self, customer_Id):
        self.cursor.execute(""" SELECT p.* 
                            FROM payment p 
                            JOIN lease l on p.lease_Id = l.lease_Id
                            WHERE l.customer_Id = ?""",(customer_Id))
        rows = self.cursor.fetchall()
        return [Payment(*row) for row in rows]
    
    def get_total_payment(self):
        self.cursor.execute("SELECT SUM(amount) FROM payment")
        result = self.cursor.fetchone()
        return result[0] if result[0] is not None else 0.0
