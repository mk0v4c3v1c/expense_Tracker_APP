from datetime import datetime
from collections import defaultdict

class BudgetManager:
    def __init__(self):
        self.budgets = {}
    #Monthly budget
    def set_budget(self, month, amount):
        self.budgets[month] = amount
        print(f"Budget set {month} for {amount:.2f} EUR.")

    #Check if the limit are overloaded for budget
    def check_budget(self, transactions):
        if not transactions:
            print("No transactions.")
            return

        #Group expense per month
        monthly_expenses = defaultdict(float)
        for t in transactions:
            month_year = datetime.strptime(t.date, "%Y-%m-%d").strftime("%Y-%m")
            monthly_expenses[month_year] += t.amount

        # Chech budget
        for month, total in monthly_expenses.items():
            budget = self.budgets.get(month, None)
            if budget is not None:
                if total > budget:
                    print(f"Run out of budget {month}! Expenses: {total:.2f} EUR (Budget: {budget:.2f} EUR)")
                else:
                    print(f"Budget for {month} is in line: {total:.2f} EUR (Budget: {budget:.2f} EUR)")
            else:
                print(f"Bugdet {month} is not set!")