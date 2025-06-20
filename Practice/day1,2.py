1. check list for odd or even

list =[50,24,33,69,20,19]
for i in list :
    if(i%2==0):
        print(f'{i} is even')
    else:
        print(f'{i} is odd')

2. using break

for i in range(1,4):
    print(f'checking {i}')
    if(i==4):
        break
else:
    print("no break")

3. nested if 

x= int(input("enter a number"))
if(x>10):
    if(x<20):
        print("x is between 10 and 20")
    else:
        print("x is greater than 20")
else:
    print("x is less than 10")

4. age and license
 
age = int(input('enter age '))
license = input('do u have license (true/fale) ')
if license=="true":
    has_license = True
else:
    has_license = False
if age>=18 and has_license:
    print('u can drive')
else:
    print(' resticted to drive ')

5. factorial
number = int(input("enter number"))
fact=1
for i in range(1,number+1):
    fact=fact*i
print(fact)

6. fact recursion
def fact(x):
    if x==0 or x==1:
        return 1
    else:
        return x*fact(x-1)
number = int(input("enter number"))
print(fact(number))

7. fibonocci
number = int(input("enter n"))
a,b=0,1
for i in range(number):
    print(a)
    a,b=b,a+b

raw =" charanya "
clean = raw.strip().title()
print(clean)

str="helloooo"
v="aeiou"
count =0
for i in str:
    if i in v:
        print(i)
        count+=1
print(count)

--------------------------------------------DAY 2
------------------------------list

fruits=['apple','banana','mango','strawberry']
print("original",fruits)
fruits.append("dates")
print(fruits)
fruits.remove('apple')
print(fruits)

fruits[-1]='hello'
print(fruits)
print(len(fruits))
for f in fruits:
    print("-"+f)

--------------------------tuple

point=(3,4)
print(point)
for i in point:
    print(i)
print(point[-1])
t2 = point + (5,)
print(t2)

t3 = t2*2
print(t3)


--------------------dictionary

employee={"name":"lokesh","age":22,"dept":"frnd"}
print(employee)
employee["dept"]="bff"
print(employee["dept"])
employee["city"]="madurai"
print(employee)
print(employee.keys())
print(employee.values())
for i,v in employee.items():
    print(f"{i}-->{v}")


----------------------set 
numbers={2,2,45,4}
print(numbers)
numbers.add(15)
print(numbers)
numbers.discard(45)
print(numbers)
numbers.add(1)
print(numbers)
print("membership test: 3 in numbers?",2 in numbers)

set_a = {1,2,3}
set_b={4,2,6}
print(set_a|set_b)
print(set_a&set_b)
print(set_b - set_a)


# ------------------- CLASS
class company:
    name : "Harith"
    turnover = 5000
    revenue = 4000
    num_emp = 500
    @classmethod
    def productivity(cls):
        return cls.turnover/cls.num_emp
c=company()
print(company.productivity())

