class Payment:
    def __init__(self,payment_id,lease_id,payment_date,amount):
        self.payment_id = payment_id
        self.lease_id = lease_id
        self.payment_date = payment_date
        self.amount = amount

    def __str__(self):
        return(
             "------PAYMENT DETAILS--------\n"
             f"PAYMENT ID : {self.payment_id}\n"
             f"LEASE ID : {self.lease_id}\n"
             f"PAYMENT DATE : {self.payment_date}\n"
             f"AMOUNT : {self.amount}\n"

        )
        