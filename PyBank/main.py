# Import the dependencies for os.path.join()
import os
import csv

# Read budget_data.csv
budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')

# Count total number of months (records) in the dataset
total_months = len(budget_csv)
print(f"Total Months: {total_months}")

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
      
    # Find net total profit/loss
    amount = 0
    profit = 0
    loss = 0
    total = 0    

    for row in csvreader:
        amount = int(row[1])
        if amount > 0:
            profit = profit + amount
        elif amount < 0:
            loss = loss + amount
    total = profit + loss
    print(f"Total: {total}")







