# operators

num_1 = float(input("Enter a number: "))
num_2 = float(input("Enter number: "))
add = num_1+num_2
sub = num_1-num_2
mul = num_1*num_2
div = num_1 / num_2
mod = num_1 % num_2
pow = num_1 ** num_2
print (f"add -->{add}\n sub -->{sub} \n mul -->{mul}\n div --> {div}\n mod -->{mod}\n pow -->{pow}")

#datatypes string

a = input("enter a str: ")
print(a *2)
print(a+"2")
b = "NEW STRING_OPERTIONS"
print(b)
print(f"reversing {b[::-1]}")
print(f"length = {len(b)}")
print(b.find('hii'))
print("NEW " in b)
print(b.replace(' ','_'))
print(b.isalpha())
 

#date 
from datetime import datetime,date,time
print(datetime.now())
print(date.today())
dt = datetime(2025,2,3,10,30,45)
print(dt)
dts= datetime.now()
print(f"year -->{dts.year}")
print(f"month -->{dts.month}")
print(f"date -->{dts.day}")
print(f"hour -->{dts.hour}")
print(f"sec -->{dts.second}")
print(f"ms -->{dts.microsecond}")
print(dts.strftime("%A"))


#class and constructor

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def getdetails(self):
        print(f"hii {self.name} and ur {self.age} years old")

per = person('haritha',22)
per.getdetails()


#encapsulation

class bank_account:
    def __init__(self,owner,balance=0):
        self.owner= owner
        self.__balance = balance
    def deposit(self,amount):
        if(amount>0):
            self.__balance = self.__balance + amount
            print(f"The new balance is {self.__balance}")
        else:
            print("Amount should be >0")
    def withdraw(self,amount):
        if(amount>self.__balance):
            print("Amount is > balance ")
        else:
            self.__balance = self.__balance - amount
            print(f"amount after withdrawal is {self.__balance}")
me = bank_account('haritha')
me.deposit(500)
me.withdraw(100)
print(me._bank_account__balance)


#bank account:


class bank_acc:
    def __init__(self,owner,balance = 0):
        self.owner= owner
        self.__balance = balance
        print(f"hello {self.owner} and ur balance is {balance}")
    def deposit(self,amount):
        if(amount>0):
            self.__balance += amount
            print(f"Amount of rs{amount} has been credited")
        else:
            print("Invalid Deposit")
    def withdrawal(self,amount):
        if amount >self.__balance:
            print("Amount cannot be withdrawn")
        else:
            self.__balance -= amount
            print(f"available balance is {self.__balance}")
class interest(bank_acc):
    def __init__(self, owner, balance=0,interest_rate = 0.2):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    def interest_cal(self):
        interest = self.__balance*self.interest_rate
        self.__balance += interest
        print(f"interest of rs{interest} has been credited and new balance is {self.__balance}")


first = interest('Haritha',500)
first.withdrawal(100)
first.interest_cal()
sec = interest('Haritha')
sec.interest_cal()
    

#library management

class book:
    def __init__(self,book_name,book_author,no_of_copies):
        self.book_name = book_name
        self.book_author = book_author
        self.no_of_copies = no_of_copies
        print(f"{book_name} by {book_author} is available --> {no_of_copies}")

    def borrow(self):
        self.no_of_copies-=1
        print(f"there are only {self.no_of_copies} available")  

    def return_book(self):
        self.no_of_copies+=1
        print(f"there are only {self.no_of_copies} available") 

book = book("Harry potter","J.K Rowling",10)
book.borrow()
book.borrow()
book.return_book()

#Hospital Management

class Patient:
    def __init__(self,pa_name,disease):
        self.pa_name = pa_name
        self.disease = disease
        print (f"Hello {pa_name}.. Welcome!")
    def get_disease(self):
        return self.disease
    
class doctor(Patient):
    def __init__(self,pa_name,disease,doc_name,specialist):
        super().__init__(pa_name,disease)
        self.doc_name = doc_name
        self.specialist = specialist
        print(f"doctor_name --> {doc_name}\n specialist -->{specialist}")
    def choose_doc(self):
        print(f"{self.disease} can only be treated by Dr.{self.doc_name}")

dis = doctor("Hari","Minor","Haritha","Cardiologist")
dis.choose_doc()

#exception handling

try:
    file = open ("C:\\Users\\Haritha\\Desktop\\python\\practise\\sample.txt","r")
    content = file.read()
except FileNotFoundError:
    print("File not found")
else:
    print("file read")
finally:
    print("closing file")
    if 'file' in locals() and not file.closed:
        file.close()

file = open("C:\\Users\\Haritha\\Desktop\\python\\practise\\sample.txt","r")
print(file.tell())
file.read(10)
print(type(file.tell()))
print(f"current position -->{file.tell()}")
file.seek(5)
print(file.tell())
print(file.read(1))
file.seek(0)
print(f"current position --> {file.tell()}")
file.seek(7)
file.seek(3)
print(f"current --> {file.tell()}")
print(file.readlines()) 
file = open("C:\\Users\\Haritha\\Desktop\\python\\practise\\sample.txt","w")
file.writelines(["New addition using writelines()"])
file.write("buffer")
file.flush()
file = open("C:\\Users\\Haritha\\Desktop\\python\\practise\\sample.txt","r")
print(file.readlines())
print(file.fileno())