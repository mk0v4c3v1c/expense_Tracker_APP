import csv
from models.transaction import Transaction

class CSVHandler:
    @staticmethod
    #Exporting to CSV file
    def export_to_csv(transactions, filename="transactions.csv"):
        if not transactions:
            print("No transactions found")
            return

        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])

            for t in transactions:
                writer.writerow([t.date, t.category, t.amount, t.description])

        print(f"✅ Data are succesfully savd in  {filename}")