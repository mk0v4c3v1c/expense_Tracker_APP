import matplotlib.pyplot as plt
from collections import defaultdict

class Chart:
    @staticmethod
    #Generate pie chart expense per categories
    def generate_pie_chart(transactions):
        if not transactions:
            print("There is no transactions to plot.")
            return

        # Group by categories
        category_totals = defaultdict(float)
        for t in transactions:
            category_totals[t.category] += t.amount

        # Prepare data for graphs
        labels = list(category_totals.keys())
        values = list(category_totals.values())

        # Draw pie chart
        plt.figure(figsize=(7, 7))
        plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=140)
        plt.title("Distribution of costs by category")
        plt.show()