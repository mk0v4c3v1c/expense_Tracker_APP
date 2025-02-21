from services.tracker import ExpenseTracker

def main():
    tracker = ExpenseTracker()

    while True:
        print("\n1. Add transaction\n2. Show transactions\n3. Show bilance\n4. Delete transaction\n5. Filtering transactions\n6. Export into CSV\n7. Show statistics\n8. Analyze monthly expenses\n9. Calculate daily expenses\n10 Analysis per categories\n11. Visualized expenses\n12. Set budget\n13. Check budget\14. Cost predicition\n15. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter the amount: "))
            category = input("Enter the category: ")
            description = input("Description (optional): ")
            tracker.add_transaction(amount, category, description)
        elif choice == "2":
            tracker.list_transactions()
        elif choice == "3":
            print(f"Current bilance: {tracker.calculate_balance()} EUR")
        elif choice == "4":
            tracker.list_transactions()
            index = int(input("Enter the transaction index for deletion : "))
            tracker.delete_transaction(index)
        elif choice == "5":
            category = input("Enter the category (or press the Enter to skip): ").strip()
            date = input("Enter the date (YYYY-MM-DD, or press the Enter to skip): ").strip()
            tracker.filter_transactions(category or None, date or None)
        elif choice == "6":
            filename = input("Enter the filename (or press the Enter to skip): ").strip() or "transactions.csv"
            tracker.export_transactions(filename)
        if choice == "7":
            tracker.show_expense_chart()
        if choice == "8":
            tracker.analyze_monthly_expenses()
        if choice == "9":
            tracker.calculate_average_daily_expense()
        if choice == "10":
            tracker.analyze_expense_by_category()
        if choice == "11":
            tracker.plot_monthly_expenses()
        if choice == "12":
            month = input("Enter month: (YYYY-MM): ")
            amount = float(input("Enter budget: "))
            tracker.set_budget(month, amount)
        elif choice == "13":
            tracker.check_budget()
            break
        if choice == "14":
            tracker.predict_next_month_expense()
        else:
            print("Unknown choice!")

if __name__ == "__main__":
    main()
