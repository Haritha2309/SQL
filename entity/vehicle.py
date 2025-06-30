class Vehicle:
    def __init__(self,vehicle_id,vehicle_make,vehicle_model,vehicle_year,daily_rate,vehicle_status,passenger_capacity,engine_capacity):
        self.vehicle_id = vehicle_id
        self.vehicle_make = vehicle_make
        self.vehicle_model = vehicle_model
        self.vehicle_year = vehicle_year
        self.daily_rate = daily_rate
        self.vehicle_status = vehicle_status
        self.passenger_capacity = passenger_capacity
        self.engine_capacity = engine_capacity

    def __str__(self):
        return(
            "--------VEHICLE DETAILS --------\n"
            f"VEHICLE ID ----------------> {self.vehicle_id}\n"
            f"VEHICLE MAKE --------------> {self.vehicle_make}\n"
            f"VEHICLE MODEL--------------> {self.vehicle_model}\n"
            f"VEHICLE YEAR --------------> {self.vehicle_year}\n"
            f"VEHICLE DAILY RATE --------> {self.daily_rate}\n"
            f"VEHICLE STATUS ------------> {self.vehicle_status}\n"
            f"PASSENGER CAPACITY --------> {self.passenger_capacity}\n"
            f"ENGINE CAPACITY -----------> {self.engine_capacity}\n"
        )