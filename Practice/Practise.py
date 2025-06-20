age = 20
price = 19.225
first_name = "haritha"
true_false = False
print(type(age),type(price),type(first_name),type(true_false))
print(age,price,first_name,true_false)

name = input("What is your name")
print("Hello" + name)

birth_year = int(input("enter year"))
age =2025-birth_year
print(age)

first = float(input("first number"))
second =float(input("sec number"))
add=first+second
print(f"add {add}")

name = 'python for beginererd'
print(name.upper())
print(name.find('y'))
print(name.find(' '))
print(name.replace('python ','c++'))
print('python' in name)

x=10*5+2
print(x)

x=3>2
print(x)

price = 20
print(price >10 and price<90)

i=1
while i<=5:
    print(i)
    i+=1

names= ['john','hari','keerthi','regii','babb','hhhauyt']
names[1]='karthik'
names[-2]='hockey'
print(names)
names.append('cricket')
print(names)
for i in range(len(names)):
    if names[i]=='hari':
        names[i]='hockey'
print(names)
names.remove('regii')
print(names)
names.pop()
print(names)
tuplee=('hii','hello','help')
print(tuplee[1])
my_list=list(tuplee)
print(my_list)

tuplee=('apple','prange','mango','banana')
my_list1=[]
for i in tuplee:
    my_list1.append(i)
print(my_list1)

students={"name":"haritha",
          "age":21}
print(students["age"])

import time
print("start")
time.sleep(2)
print("end")

from datetime import datetime
timestamp = 1623548790
dt=datetime.fromtimestamp(timestamp)
print (dt)

def func1():
    print("my name is haritha")
func1()

z=lambda x: x**2
print(z(6))

add =lambda a,b:a+b
print(add(3,5))

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