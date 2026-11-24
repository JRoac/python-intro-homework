import os
import csv
import datetime

if os.path.exists("data/expenses.csv"):
    with open("data/expenses.csv", "r") as file:
        records = list(csv.DictReader(file)) 

    for record in records:
        record["amount"] = float(record["amount"])

    food_expenses = [record for record in records if record['category'] == "Food"]
    food_total = sum(record["amount"] for record in food_expenses)

    today = datetime.date.today().strftime("%B %d, %Y")
    
    with open("food_report.txt", "w") as report:
        report.write(f"Food Expense Report - generated {today}\n")
        for record in food_expenses:
            report.write(f"{record['date']}: ${record['amount']:.2f}\n")
            
        report.write(f"Total: ${food_total:.2f}\n")

else:
    print("Sorry, file doesn't exist.")
    exit()


