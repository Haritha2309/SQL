from util.connection import Connection
from dao.IHospitalService import I_Hospital_Service
from entity.appointment import  Appointment
from entity.doctor import Doctor
from entity.patient import Patient
from exception.PatientNotFoundException import PatientNotFoundException

class I_Hospital_service_Impl(I_Hospital_Service):
    def __init__(self):
        db = Connection()
        self.conn = db.get_connection()
        if self.conn is None:
            raise Exception ("connectivity failed")
        self.cursor = self.conn.cursor()

    def get_appointment_by_id(self, appointment_id):
        self.cursor.execute("SELECT * FROM appointment WHERE appointment_id = ?",(appointment_id))
        row = self.cursor.fetchone()
        return Appointment(*row)
    
    def get_appointments_for_patient(self, patient_id):
        self.cursor.execute("SELECT * FROM appointment WHERE patient_id = ?",(patient_id))
        rows = self.cursor.fetchall()
        if not rows:
            raise PatientNotFoundException(f"Patient ID {patient_id} is not found")
        return [Appointment(*row) for row in rows]
    
    def get_appointments_for_doctor(self, doctor_id):
        self.cursor.execute("SELECT * FROM appointment WHERE doctor_id = ?",(doctor_id))
        rows = self.cursor.fetchall()
        return [Appointment(*row) for row in rows]
    
    def schedule_appointment(self, appointment):
        self.cursor.execute("""
                            INSERT INTO appointment (patient_id,doctor_id,appointment_date,description)
                            VALUES(?,?,?,?)""",(appointment.patient_id,appointment.doctor_id,appointment.appointment_date,appointment.description))
        self.conn.commit()

    def update_appointment(self, appointment):
        self.cursor.execute("""
                            UPDATE appointment 
                            SET doctor_id = ?, description = ?,appointment_date =?
                            WHERE appointment_id = ? AND patient_id = ?
                            """,(appointment.doctor_id,appointment.description,appointment.appointment_date,appointment.appointment_id,appointment.patient_id))
        self.conn.commit()

    def cancel_appointment(self, appointment_id):
        self.cursor.execute("DELETE FROM appointment WHERE appointment_id =?",(appointment_id))
        self.conn.commit()