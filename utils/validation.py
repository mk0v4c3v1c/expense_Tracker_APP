from datetime import datetime

class Validation:
    @staticmethod
    def is_valid_amount(amount):
        return amount > 0

    #Check if there is date in current format YYYY-MM-DD
    @staticmethod
    def is_valid_date(date_str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False