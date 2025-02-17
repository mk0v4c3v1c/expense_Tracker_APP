from collections import defaultdict
from datetime import datetime

class CategoryAnalysis:
    @staticmethod
    #Analyze transaction expense by category
    def analyze_expense_by_category(transactions):
        if not transactions:
            print(" No transactions found. ")
            return

        # Group by month and category
        category_totals = defaultdict(lambda: defaultdict(float))
        for t in transactions:
            month_year = datetime.strptime(t.date, "%Y-%m-%d").strftime("%Y-%m")
            category_totals[month_year][t.category] += t.amount

        # Print results
        print("\n Consumption by category on a monthly basis:")
        for month, categories in sorted(category_totals.items()):
            print(f"\n {month}:")
            for category, total in categories.items():
                print(f"  - {category}: {total:.2f} EUR")