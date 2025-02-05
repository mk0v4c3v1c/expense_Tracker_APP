from models.transaction import Transaction
from services.data_handler import DataHandler
from models.category import Category

class ExpenseTracker:
    def __init__(self):
        self.transactions = DataHandler.load_transactions()

    #Add new transaction if it's valid
    def add_transaction(self, amount: float, category: str, description: str = ""):
        if not Category.is_valid(category):
            raise ValueError("Nevažeća kategorija!")

        transaction = Transaction(amount, category, description=description)
        self.transactions.append(transaction)
        DataHandler.save_transactions(self.transactions)
        print(f"Dodata transakcija: {transaction.to_dict()}")

    #Show all transactions
    def list_transactions(self):
        for t in self.transactions:
            print(f"{t.date} | {t.category} | {t.amount} RSD | {t.description}")

    #Calculate current balance
    def calculate_balance(self):
        return sum(t.amount for t in self.transactions)
