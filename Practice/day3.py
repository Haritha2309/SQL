class student_manager:
    def __init__(self):
        self.students={}
    def addstudent(self,roll_no,stu_name,grade):
        if roll_no in self.students:
            print(f"{roll_no} aldready exists")
        else:
            self.students[roll_no]= {"name":stu_name,"marks":grade}
            print(f"{roll_no} roll_no is added for {stu_name} is added ")
    def get_student_details(self,roll_no):
        if roll_no in self.students:
            return self.students[roll_no]
        else:
            return f"No student with roll_no {roll_no}"
    def get_top_student(self,criteria):
        top_students= [
            {"roll_no": roll_no,"stu_name":data["name"],"marks":data["marks"]}
            for roll_no,data in self.students.items()
            if data["marks"]>criteria
            ]
        return top_students
result = student_manager()
stu_data = [
    {"roll_no": 11,"stu_name":"Haritha","marks":95},
    {"roll_no": 12,"stu_name":"Harini","marks":85},
    {"roll_no": 13,"stu_name":"Hari","marks":45},
    {"roll_no": 14,"stu_name":"Haries","marks":65},    
]
for student in stu_data:
    result.addstudent(student["roll_no"],student["stu_name"],student["marks"])
print(result.get_student_details(11))
top_students = result.get_top_student(76)
print(top_students)
for student in top_students:
    print(student)

#----------------------- ENCAPSULATION

class bank_acc:
    def __init__(self,acc_holder,balance=0):
        self.acc_holder=acc_holder
        self._balance=balance
    def deposit(self,amount):
        if amount>0:
            self._balance=self._balance+amount
            print(f"{amount} is deposited and balance is {self._balance}")
        else:
            print("deposit amount is invalid")
    def get_balance(self):
        return self._balance
account = bank_acc("Haritha",3000)
print(account.acc_holder)
account.deposit(5000)
print(account.get_balance)
print(account._balance)

#---------------------- INHERITANCE

class bank_acc:
    def __init__(self,acc_holder,balance=0):
        self.acc_holder=acc_holder
        self._balance=balance
    def deposit(self,amount):
        if amount>0:
             self._balance=self._balance+amount
             print(f"{amount} is deposited and balance is {self._balance}")
        else:
             print("deposit amount is invalid")
    def get_balance(self):
        return self._balance
class savings(bank_acc):
    def __init__(self, acc_holder, balance=0,interest_rate=0.05):
        super().__init__(acc_holder, balance)
        self.interest_rate=interest_rate
    def calc_interest(self):
        interest = self._balance * self.interest_rate
        self._balance = self._balance + interest
        print(f"{interest} is added and the new balance is {self._balance}")

saving = savings("Haritha",balance = 1000, interest_rate=0.02)
saving. deposit(5000)
saving.calc_interest()
print(f"Total amount available {saving.get_balance()}")

#---------------------- POLYMORPHISM

class bank_acc:
    def __init__(self,acc_holder,balance=0):
        self.acc_holder=acc_holder
        self._balance=balance
    def deposit(self,amount,currency = "INR"):
        

        if amount>0:
             self._balance=self._balance+amount
             print(f"{amount} is deposited and balance is {self._balance}")
        else:
             print("deposit amount is invalid")
    def withdraw(self,amount):
        if amount<= self._balance:
            self._balance=self._balance - amount
            print(f"{amount} is withrawn and the balance is {self._balance}")
    
class savings(bank_acc):
    def __init__(self, acc_holder, balance=0,overdraft_limit = 100):
        super().__init__(acc_holder, balance)
        self.overdraft_limit = overdraft_limit
    def withdraw(self, amount):
        if amount<=self._balance + self.overdraft_limit:
            self._balance=self._balance - amount
            print(f"amount withdrawn is {amount} and balance is {self._balance}")
        else:
            print("Exceeded overdraft limit")
basic_acc =  bank_acc("Haritha",100)
basic_acc.deposit(200)
basic_acc.deposit(200,"USD") # mtd overloading

sav_acc = savings("Hari",balance=300,overdraft_limit=200)
sav_acc.withdraw(5000) # mtd overriding by same mtd 
sav_acc.withdraw(5000)

# ------------------------ PRACTISE
# 1. GET STUDENT DETAILS

class student:
    def __init__(self):
        self.students={}
    def add_stu(self,roll_no,stu_name):
        if stu_name in self.students:
            print(f"{stu_name} aldready exists")
        else:
            self.students[stu_name]={"name":stu_name,"roll_no":roll_no}
            print(f"{stu_name} is added")
    def get_details(self,stu_name):
        if stu_name in self.students:
            return self.students[stu_name]
        else:
            print("No student ")

stu=student()
stu_data=[
    {"roll_no":123,"stu_name":"HARITHA"},
    {"roll_no":456,"stu_name":"HARIES"},
    {"roll_no":789,"stu_name":"HARI"},
    {"roll_no":987,"stu_name":"HASINI"},
]
for student in stu_data:
    stu.add_stu(student["roll_no"],student["stu_name"])
print(stu.get_details('HARITHA'))


# 2. RECTANGLE CLASS

class rectangle:
    def __init__(self,length,width):
        self.length= length
        self.width = width
    def cal_area(self):
        area= self.length * self.width
        print(f"area is {area}")
rect = rectangle(9,10)
rect.cal_area()

# 3. EMPLOYEE CLASS WITH OVERTIME CALC
class employee:
    def __init__(self,emp_id,emp_name,emp_salary,emp_dept,emp_whr):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_dept = emp_dept
        self.emp_whr = emp_whr
    def overtime_pay (self):
        if self.emp_whr >45:
            overtime_hrs = self.emp_whr - 45
            over_pay = overtime_hrs * 1000
            print (f"overtime payment is {over_pay}")
            return over_pay
        else:
            print("No overtime worked")
    def get_details(self,emp_id):
        overall_salary = self.emp_salary + self.overtime_pay()
        print("DETAIL:")
        print(f"emp_name: {self.emp_name}")
        print(f"emp_id :{self.emp_id}"),
        print(f"salary: {overall_salary}")

emp = employee(1234,"HARITHA",5000,"hr",50)
emp.get_details(1234)
