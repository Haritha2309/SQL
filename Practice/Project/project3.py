import math
class bill_splitter:
    def __init__(self):
        self.total_amount = 0
        self.people ={}
    def input(self):
        n = int(input("Enter no of person: "))
        for i in range(n):
            name = input(f"Enter name {i+1}: ")
            can_pay = float(input("How much can be afforded: "))
            self.people[name] = can_pay

        amount = float(input("Enter the amount: "))
        tax = float(input("Enter gst% "))
        if tax > 0.00:
            amount = amount +( (tax / 100) * amount)
        self.total_amount += amount
        print(f"Total amount --> {self.total_amount}")

    def split(self):
        self.input()
        affordable = sum(self.people.values())
        persons = len(self.people)
        print(f"Total amount = {self.total_amount}")
        print(f"Affordables = {affordable}")
        if affordable >= self.total_amount:
            print("We have enough amount ")
            for name,share in self.people.items():
                ratio = share/affordable
                print(f"{name} pays {ratio}")
        else:
            balance = self.total_amount - affordable
            extra = balance / persons
            print("Not enough emough and so going for money split")
            print(f"Remaining --> {balance} \n everyone pays extra rs.{extra}")
            for name,can_pay in self.people.items():
                total_pay = can_pay+extra
                print(f"{name} pays rs.{total_pay}")

split = bill_splitter()
split.split()
