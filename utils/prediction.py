from collections import defaultdict
from datetime import datetime

class ExpensePrediction:
    @staticmethod
    def predict_next_month_expense(transactions):
        #Predicts expenses for the next month based on the average of previous months.
        if not transactions:
            print("No transactions")
            return

        # Group expenses per month
        monthly_totals = defaultdict(float)
        for t in transactions:
            month_year = datetime.strptime(t.date, "%Y-%m-%d").strftime("%Y-%m")
            monthly_totals[month_year] += t.amount

        # Calculate average monthly expenses
        months = sorted(monthly_totals.keys())
        if len(months) < 2:
            print("No data for this month")
            return

        average_expense = sum(monthly_totals.values()) / len(months)

        # Forecasting expenses for the next month
        last_month = months[-1]
        next_month = datetime.strptime(last_month, "%Y-%m").replace(day=1).month + 1
        next_year = datetime.strptime(last_month, "%Y-%m").year
        if next_month > 12:
            next_month = 1
            next_year += 1
        next_month_str = f"{next_year}-{str(next_month).zfill(2)}"

        print(f"\n Predicted expense {next_month_str}: {average_expense:.2f} EUR")