import json
import os
from models.transaction import Transaction

DATA_FILE = "data/transactions.json"

#Load transaction from JSON file
class DataHandler:
    @staticmethod
    def load_transactions():
        if not os.path.exists(DATA_FILE):
            return []

        try:
            with open(DATA_FILE, "r") as file:
                data = json.load(file)
                return [Transaction.from_dict(t) for t in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    #Save transaction into JSON file
    @staticmethod
    def save_transactions(transactions):
        with open(DATA_FILE, "w") as file:
            json.dump([t.to_dict() for t in transactions], file, indent=4)
