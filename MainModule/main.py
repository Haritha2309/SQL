from Exception.CarNotFound import CarNotFoundException
from Exception.CustomerNotFound import CustomerNotFoundException
from Exception.LeaseNotFound import LeaseNotFoundException
from dao.I_Car_Lease_Repo_Impl import ICarLeaseRepoImpl
from entity.customer import Customer
from entity.lease import Lease
from entity.payment import Payment
from entity.vehicle import Vehicle
from datetime import datetime

def main():
    service = ICarLeaseRepoImpl()
    while True:
        print("----- WELCOME -----")
        print("      1. ADD CAR \n" \
        "      2. REMOVE CAR \n" \
        "      3. LIST AVAILABLE CARS\n" \
        "      4. LIST RENTED CARS\n" \
        "      5. FIND CAR BY ID\n" \
        "      6. ADD CUSTOMER\n" \
        "      7. REMOVE CUSTOMER\n" \
        "      8. LIST CUSTOMERS\n" \
        "      9. FIND CUSTOMER BY ID\n" \
        "      10. CREATE LEASE\n" \
        "      11. RETURN CAR\n" \
        "      12. LIST ACTIVE LEASES\n" \
        "      13. LIST LEASE HISTORY\n" \
        "      14. RECORD PAYMENT\n" \
        "      15. PAYMENT HISTORY\n" \
        "      16. TOTAL REVENUE\n" \
        "      17. EXIT\n"
        "   -----------------------------------------")
        choice = int(input("ENTER YOUR CHOICE: "))
        if choice == 1:
            try:
                make = input("ENTER CAR MAKE: ")
                model = input("ENTER CAR MODEL : ")
                rate = float(input("ENTER THE DAILY RATE: "))
                year = int(input("ENTER YEAR: "))
                status = 'Available'
                p_cap = int(input("ENTER PASSENGER CAPACITY: "))
                e_cap = float(input("ENTER ENGINE CAPACITY: "))
                car = Vehicle(None,make,model,year,rate,status,p_cap,e_cap)
                service.add_car(car)
                print("Car has been added..!")
            except Exception as e:
                print("ERROR.!")

        elif choice == 2:
            try:
                car_id = int(input("ENTER CAR ID : "))
                service.remove_car(car_id)
                print("CAR SUCCESSFULLY REMOVED..!")
            except CarNotFoundException as e:
                print(f"CAR WITH ID {car_id} is not found")

        elif choice ==3:
            for car in service.listAvailableCars():
                print(car)

        elif choice == 4:
            for car in service.ListRentedCars():
                print(car)

        elif choice == 5:
            try:
                id = int(input("ENTER CAR ID : "))
                print(service.FindCarById(id))
            except CarNotFoundException as e:
                print(f"CAR WITH ID {id} IS NOT FOUND")

        elif choice == 6:
            try:
                fname = input("ENTER YOUR FIRST NAME: ")
                lname = input("ENTER YOUR LAST NAME: ")
                email = input ("ENTER YOUR EMAIL : ")
                phone_num = input("ENTER YOUR PHONE NUMBER(NNN-NNN-NNNN): ")
                cus = Customer(None,fname,lname,email,phone_num)
                service.add_customer(cus)
                print("CUSTOMER ADDED..!\n")
            except Exception as e:
                print("AN ERROR OCCURED")

        elif choice == 7:
            try:
                cid = int(input("ENTER YOUR CUSTOMER ID: "))
                service.remove_customer(cid)
                print("CUSTOMER REMOVED SUCCESSFULLY..!\n")
            except CustomerNotFoundException as e:
                print(f"CUSTOMER WITH ID {e} IS NOT FOUND")

        elif choice == 8:
            for cus in service.listcustomer():
                print(cus)

        elif choice == 9:
            try:
                cus_id = int(input("ENTER YOUR CUSTOMER ID: "))
                print(service.FindCustomerById(cus_id))
            except CustomerNotFoundException as e:
                print(f"CUSTOMER WITH ID {e} IS NOT FOUND")

        elif choice ==10:
            try:
                c_id = int(input("ENTER YOUR VEHICLE ID: "))
                cus_id = int(input("ENTER YOUR CUSTOMER ID: "))
                start_date = datetime.now().date()
                end_date = input("enter the last date (YYYY-MM-DD): ")
                end_date= datetime.strptime(end_date,"%Y-%m-%d").date()
                service.create_lease(c_id,cus_id,start_date,end_date)
                print("LEASE SUCCESSFULLY CREATED..!")
            except (CarNotFoundException, CustomerNotFoundException) as e:
                print(f"LEASE CREATION FAILED {e}")
            except Exception as e:
                 print(f"An unexpected error occurred: {e}")

        elif choice == 11:
            try:
                l_id = int(input("ENTER LEASE ID : "))
                service.return_car(l_id)
                print("CAR RETURN SUCCESSFUL...!")
            except CarNotFoundException as e:
                print(f"CAR WITH LEASE ID {l_id} IS NOT FOUND")

        elif choice == 12:
            result = service.ListActiveLeases()
            if not result:
                print("NO ACTIVE LEASES...")
            else:
                for row in service.ListActiveLeases():
                    print(row)

        elif choice == 13:
            for row in service.ListLeaseHistory():
                print(row)

        elif choice == 14:
            try:
                l_id = int(input("ENTER LEASE ID : "))
                amount = float(input("ENTER AMOUNT: "))
                service.record_payemnt(l_id,amount)
                print("AMOUNT CREDITED AND RECORDED SUCCESSFULLY..!")
            except LeaseNotFoundException as e:
                print(f"LEASE WITH LEASE ID {l_id} IS NOT FOUND")

        elif choice == 15:
            try:
                cus_id = int(input("ENTER YOUR CUSTOMER ID: "))
                for row in service.get_payment_history(cus_id):
                    print(row)
            except CustomerNotFoundException as e:
                print(f"CUSTOMER WITH ID {cus_id} IS NOT FOUND")

        elif choice == 16:
            total = service.get_total_payment()
            print(f"TOTAL REVENUE = {total}")

        elif choice == 17:
            print("BREAKING...!")
            break

        else:
            print("ENTER VALID CHOICE...!")


if __name__ == "__main__":
    main()
