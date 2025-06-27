from dao.IHospitalServiceImpl import I_Hospital_service_Impl
from entity.appointment import Appointment
from exception.PatientNotFoundException import PatientNotFoundException



def main():
    service = I_Hospital_service_Impl()
    while True:
        print("\n -----------------WELCOME ------------- ")
        print("1. SCHELUE APPOINTMENT \n" \
              "2. GET APPOINTMENT BY ID \n" \
              "3. GET APPOINTMENT FOR PATIENT \n" \
              "4. GET APPOINTMENT FOR DOCTOR \n" \
              "5. UPDATE APPOINTMENT \n" \
              "6. CANCEL APPOINTMENT \n" \
              "7. EXIT")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            # try :
            p_id = int(input("ENTER YOUR PATIENT ID : "))
            d_id = int(input("ENTER YOUR DOCTOR ID: "))
            dte = input("ENTER THE DATE (YYYY-MM-DD): ")
            desc = input("ENTER YOUR DESCRIPTION: ")
            apts = Appointment(None,p_id,d_id,dte,desc)
            service.schedule_appointment(apts)
            print("APPOINTMENT SCHEDULED..!")
            # except Exception as e:
            #     print("ERROR .!")

        elif choice == 2:
            # try: 
            a_id = int(input("ENTER APPOINTMENT ID: "))
            apt2 = service.get_appointment_by_id(a_id)
            print(apt2)
            print("SUCCESSFUL ..!")
            # except Exception as e:
            #     print("ERROR..!")

        elif choice == 3:
            # try:
            p_id = int(input("ENTER PATIENT ID: "))
            apt3 = service.get_appointments_for_patient(p_id)
            for a in apt3:
                print(a)
            # except PatientNotFoundException as e:
            #     print(e)
        
        elif choice == 4:
            try: 
                d_id = int(input("ENTER DOCTOR ID: "))
                apt = service.get_appointments_for_doctor(d_id)
                for a in apt:
                    print(a)
            except Exception as e:
                print("ERRROR...!")
        
        elif choice == 5:
            # try:
            a_id = int(input("ENTER APPOINTMENT ID : "))
            p_id = int(input("ENTER PATIENT ID: "))
            d_id = int(input("ENTER DOCTOR ID: "))
            dte = input("ENTER DATE(YYYY-MM-DD): ")
            desc = input("ENTER DESCRIPTION: ")
            apttt = Appointment(a_id,p_id,d_id,dte,desc)
            service.update_appointment(apttt)
            print("APPOINTMENT UPDATED SUCCESSFULLY")
            # except Exception as e:
            #     print("ERROR..!")
            
        elif choice == 6:
            # try:
            a_id = int(input("ENTER APPOINTMENT ID: "))
            service.cancel_appointment(a_id)
            print("APPOINTMENT CANCELLED..")
            # except Exception as e:
            #     print("ERROR..!")

        elif choice == 7:
            print("BREAKING..!")
            break
        else:
            print("ENTER VALID CHOICE ..!")

if __name__ == "__main__":
    main()
