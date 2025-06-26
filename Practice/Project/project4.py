class quiz:
    def __init__(self):
        self.quiz = {
            "1. What is the capital of india?":(("A. Paris","B. France ","C. Delhi","D. Agra"),"C"),
            "2. 2+2*5=? ":(("A. 12","B. 10","C. 14","D. 94"),"A"),
            "3. Tree comes unde.? ": (("A. Linear","B. Non Linear","C. Static","D. Dynamic"),"B")
        }
        self.score = 0
        self.total_qs = len(self.quiz)

    def qs(self,questions,options,answer):
        print(f"{questions}")
        for opt in options:
            print(opt)
        opted = input("enter your answer : ").upper()
        if opted == answer:
            print("Hurray!!! Correct ")
            self.score+=1
        else:
            print("oopss!! Wrong answer ")
    
    def start(self):
        print("Welcome to quiz")
        for ques ,(opt,ans) in self.quiz.items():
            self.qs(ques,opt,ans)

        print(F"Final Score is {self.score}/{self.total_qs}")

quizz = quiz()
quizz.start() 