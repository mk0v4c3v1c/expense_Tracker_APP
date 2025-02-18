import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime

class ExpenseVisualization:
    @staticmethod
    #Visualize montly expenses
    def plot_monthly_expenses(transactions):
        if not transactions:
            print("No transactions found")
            return

        # Group by month
        monthly_totals = defaultdict(float)
        for t in transactions:
            month_year = datetime.strptime(t.date, "%Y-%m-%d").strftime("%Y-%m")
            monthly_totals[month_year] += t.amount

        # Preparing data for graphs
        months = sorted(monthly_totals.keys())
        totals = [monthly_totals[m] for m in months]

        # Create graphs
        plt.figure(figsize=(10, 5))
        plt.plot(months, totals, marker='o', linestyle='-', color='b', label="Monthly Expenses")
        plt.xlabel("Month")
        plt.ylabel("Expenses (EUR)")
        plt.title("📈 Monthly Expenses")
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid()
        plt.show()