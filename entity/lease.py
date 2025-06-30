class Lease:
    def __init__(self,lease_id,vehicle_id,customer_id,start_date,end_date,type):
        self.lease_id = lease_id
        self.vehicle_id = vehicle_id
        self.customer_id = customer_id
        self.start_date = start_date
        self.end_date = end_date
        self.type = type

    def __str__(self):
            return(
             "------LEASE  DETAILS--------\n"
             f"LEASE ID : {self.lease_id}\n"
             f"VEHICE ID : {self.vehicle_id}\n"
             f"CUSTOMER ID  : {self.customer_id}\n"
             f"START DATE : {self.start_date}\n"
             f"END DATE : {self.end_date}\n"
             f"TYPE : {self.type}\n"

        )
        
