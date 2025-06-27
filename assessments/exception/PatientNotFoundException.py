class PatientNotFoundException:
    def __init__(self,message= "Patient number not found") :
        super().__init__(message)