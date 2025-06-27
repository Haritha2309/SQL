class Appointment:
    def __init__(self,appointment_id,patient_id,doctor_id,appointment_date,description):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_date = appointment_date
        self.description = description
        
    def __str__(self):
        return f"Appointment[ID = {self.appointment_id},patient ID = {self.patient_id}, doctor ID = {self.doctor_id}, Date = {self.appointment_date},description = {self.description}]"