from openpyxl import Workbook
class students:
    def __init__(self):
        self.stu_name = input("Enter student name: ")
        self.roll_no = input("enter roll no: ")
        self.marks ={}

    def get_marks(self):
        subject = ["English","Tamil","Maths","Science","Social"]
        for i in subject:
            mark = int(input(f"Enter mark of {i} : "))
            self.marks[i] = mark

    def get_highest_sub(self):
        best_sub, best_score =  max(self.marks.items(), key = lambda x:x[1])
        return best_sub,best_score

class report:
    def __init__(self,students):
        self.students = students
    
    def calc_avg(self):
        total = sum(self.students.marks.values())
        avg = total/len(self.students.marks)

        if avg >90:
            return "A"
        elif avg>70:
            return "B"
        elif avg>50:
            return "C"
        else:
            return "Fail"
        
    def display(self):
        print(f"Name : {self.students.stu_name}")
        print(f"Roll no : {self.students.roll_no}")
        print("MARKS ARE AS FOLLOWS ")
        for subject, mark in self.students.marks.items():
            print(f"{subject}-->{mark}")
        
        avg = self.calc_avg()
        print(f"grade  -->{avg}")

        print(f"Has good knowledge in {self.students.get_highest_sub()}")

    def export(self,sheet):
        grade = self.calc_avg()
        best_sub,best_score = self.students.get_highest_sub()
        English = self.students.marks.get("English",0)
        Tamil = self.students.marks.get("Tamil",0)
        Maths = self.students.marks.get("Maths",0)
        Science = self.students.marks.get("Science",0)
        Social = self.students.marks.get("Social",0)

        sheet.append([
            self.students.stu_name,
            self.students.roll_no,
            English,
            Tamil,
            Maths,
            Science,
            Social,
            grade,
            f"{best_sub} ({best_score})"
        ])

students_list =[]
n = int(input("Enter no of students: "))
for i in range(n):
    print(f"Entering details of Student {i+1} -")
    stu = students()
    stu.get_marks()
    students_list.append(stu)

wb = Workbook()
sheet = wb.active
sheet.title = "Report Card"
sheet.append(["name","roll_no","English","Tamil","Maths","Science","Social","grade","best"])
for stu in students_list:
    rep = report(stu)
    rep.display()
    rep.export(sheet)

file_name = "Student_report.xlsx"
wb.save(file_name)
print("Report Successfully created")
