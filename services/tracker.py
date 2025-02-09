from models.transaction import Transaction
from services.data_handler import DataHandler
from models.category import Category
from datetime import datetime

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

