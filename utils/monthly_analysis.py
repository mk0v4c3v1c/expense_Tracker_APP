from collections import defaultdict
from datetime import datetime

class MonthlyAnalysis:
    @staticmethod
    def analyze_monthly_expenses(transactions):
        if not transactions:
            print("No transactions found for monthly analysis")
            return

        # Group by month
        monthly_totals = defaultdict(float)
        for t in transactions:
            month_year = datetime.strptime(t.date, "%Y-%m-%d").strftime("%Y-%m")
            monthly_totals[month_year] += t.amount

        # Print by month expenses
        print("\n Analize expenses by month:")
        for month, total in sorted(monthly_totals.items()):
            print(f"{month}: {total:.2f} EUR")