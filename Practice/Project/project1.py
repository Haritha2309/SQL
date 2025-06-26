from datetime import datetime
class monthly_expense_tracker:
    def __init__(self,income,savings = 500):
        self.income = income
        self.savings = savings
        self.expense= {}
        print(f"U have a monthly income of rs {income}")
        self.expenses()

    def expenses(self):
        print("Enter mandatory expenses: ")
        self.expense['Groceries'] = float(input("Enter the amount for Grocery: "))
        self.expense['Milk'] = float(input("Enter the amount for Milk: "))
        self.expense['Cable conn'] = float(input("Enter the amount for cable: "))
        self.expense['Current'] =  float(input("Enter the amount for Current: "))
        additional = input("Any other expense (Yes/NO) ").lower()
        if additional == 'yes':
            n = int(input("No of expenses:"))
            for i in range(n):
                category = input("Enter the category: ")
                amount = int(input("Enter the amount: "))
                self.expense[category]= amount
        self.total_expense()

    def total_expense(self):
        total = sum(self.expense.values())
        print(f"U have spend Rs.{total}")
        
        if total >self.income:
            spent = total - self.income
            print(f"U have spent Rs.{spent} more than income")
            print("u have spent more..!")
        elif total < self.income:
            saved = self.income - total
            print(f"Savings for this month = {saved}")
            if saved > self.savings:
                great = saved - self.savings
                print(f"U have saved RS.{great} more than previous month")
dts = datetime.now()
print(f"{dts.strftime("%B")} - {dts.year} Expenses")
inc = float(input("Enter your income for this month: "))
ex = monthly_expense_tracker(inc)



