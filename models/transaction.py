from datetime import datetime

class Transaction:
    def __init__(self, amount: float, category: str, date: str = None, description: str = ""):
        self.amount = amount
        self.category = category
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")
        self.description = description

    #Converting object into dict for JSON saving
    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "description": self.description
        }

    #Create object from dict when we read from JSON
    @staticmethod
    def from_dict(data: dict):
        return Transaction(
            amount=data["amount"],
            category=data["category"],
            date=data["date"],
            description=data["description"]
        )
