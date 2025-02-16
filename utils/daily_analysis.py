from collections import defaultdict
from datetime import datetime

#Calculate daily average
class DailyAnalysis:
    @staticmethod
    def calculate_average_daily_expense(transactions):
        if not transactions:
            print("No transactions found")
            return

        # Group by days
        daily_totals = defaultdict(float)
        for t in transactions:
            date = datetime.strptime(t.date, "%Y-%m-%d").strftime("%Y-%m-%d")
            daily_totals[date] += t.amount

        # Average expense per day
        total_days = len(daily_totals)
        total_expense = sum(daily_totals.values())

        average_expense = total_expense / total_days if total_days else 0

        # Results
        print("\n📊 Average Daily Expense:")
        print(f"Total days: {total_days}")
        print(f"Total expese: {total_expense:.2f} EUR")
        print(f"Average daily expense: {average_expense:.2f} EUR")