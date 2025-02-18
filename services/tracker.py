from models.transaction import Transaction
from services.data_handler import DataHandler
from models.category import Category
from datetime import datetime
from utils.csv_handler import CSVHandler
from utils.chart import Chart
from utils.monthly_analysis import MonthlyAnalysis
from utils.daily_analysis import DailyAnalysis
from utils.category_analysis import CategoryAnalysis
from utils.visualization import ExpenseVisualization






class ExpenseTracker:
    def __init__(self):
        self.transactions = DataHandler.load_transactions()
    #Delete transaction per index
    def delete_transaction(self, index: int):
        if 0 <= index < len(self.transactions):
            deleted_transaction = self.transactions.pop(index)
            DataHandler.save_transactions(self.transactions)
            print(f"Transaction deleted: {deleted_transaction.to_dict()}")
        else:
            print("Invalid transaction index. Please try again.")
    #Add new transaction if it's valid
    def add_transaction(self, amount: float, category: str, description: str = ""):
        if not Category.is_valid(category):
            raise ValueError("Not a valid category!")
        #Transactions per description
        transaction = Transaction(amount, category, description=description)
        self.transactions.append(transaction)
        DataHandler.save_transactions(self.transactions)
        print(f"Added Transaction: {transaction.to_dict()}")
    #List transactions
    def list_transactions(self):
        if not self.transactions:
            print(" No transactions recorded yet.")
            return

        print("\n Transaction List:")
        for t in self.transactions:
            print(f"{t.date} | {t.category} | {t.amount} RSD | {t.description}")

    def calculate_balance(self):
        return sum(t.amount for t in self.transactions)

    #Filter transaction per category or date
    def filter_transactions(self, category: str = None, date: str = None):
        filtered = self.transactions

        if category:
            filtered = [t for t in filtered if t.category.lower() == category.lower()]

        if date:
            filtered = [t for t in filtered if t.date == date]

        if not filtered:
            print("There are no transactions recorded yet.")
            return

        for t in filtered:
            print(f"{t.date} | {t.category} | {t.amount} RSD | {t.description}")

    # Export transaction into CSV file
    def export_transactions(self, filename="transactions.csv"):
        CSVHandler.export_to_csv(self.transactions, filename)

    # Show pie chart expenses per categories
    def show_expense_chart(self):
        Chart.generate_pie_chart(self.transactions)

    # Show and analyze monthly expenses
    def analyze_monthly_expenses(self):
        MonthlyAnalysis.analyze_monthly_expenses(self.transactions)

    # Calculate and show average daily expense
    def calculate_average_daily_expense(self):
        DailyAnalysis.calculate_average_daily_expense(self.transactions)

    # Analyze expenses by category
    def analyze_expense_by_category(self):
        CategoryAnalysis.analyze_expense_by_category(self.transactions)

    #Show monthly expense graphs
    def plot_monthly_expenses(self):
        ExpenseVisualization.plot_monthly_expenses(self.transactions)