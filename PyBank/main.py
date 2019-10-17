# Dependencies
import csv
import os

# Read csv file
budget_csv = os.path.join('Resources/budget_data.csv')

# Output txt file
output_file = os.path.join('Analysis/budget_analysis.txt')

# Define financial parameters for calculations
#_____________________________________________________________

# 1 The total number of months included in the dataset
total_months = 0

# 2 The net total amount of "Profit/Losses" over the entire period
net_total = 0

# 3 The average of the changes in "Profit/Losses" over the entire period
# 3a List: date of "Profit/Losses" month to month
change_date = []
# 3b List: amount of "Profit/Losses" from month to month.
change_amount = [] 
# 3c The sum of this list divided by number of months (86) will give average of changes.

# 4 The greatest increase in profits (change_date and change_amount) over the entire period
greatest_increase = ["", 0]

# 5 The greatest increase in profits (change_date and change_amount) over the entire period
greatest_decrease = ["", 999999999999999]

#______________________________________________________________

# Read budget_csv and convert to list of dictionaries
with open(budget_csv) as financial_data:
    reader = csv.reader(financial_data)

    # Skip header row
    header = next(reader)

    # Skip first row of data for change_amount list
    first_row = next(reader)
    
    # Start count of total_months
    total_months = total_months + 1

    # Start sum of rows for net_total
    net_total = net_total + int(first_row[1])

    # Identify rows to be subtracted for average of changes
    subtracted_row = int(first_row[1])

    for row in reader:
        # 1 Track total_months
        total_months = total_months + 1

        # 2 Track net_total
        net_total = net_total + int(row[1])

        # 3 Track the month to month changes
        month_change = int(row[1]) - subtracted_row
        subtracted_row = int(row[1])
        change_amount = change_amount + [month_change]
        change_date = change_date + [row[0]]

        # 4 Find greatest increase
        if month_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = month_change

        # 5 Find greatest decrease
        if month_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = month_change

# Calculate the average of the changes over the entire period
change_average = sum(change_amount) / len(change_amount)

# Print calculations
print(f"Financial Analysis")
print(f"-----------------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${change_average:.2f}")
print(f"Greatest Increase in Profits: ${greatest_increase[1]}")
print(f"Greatest Decrease in Profits: ${greatest_decrease[1]}")

# Export calculations .txt file
with open(output_file, "w") as txt_file:
    txt_file.write(f"Financial Analysis, -----------------------------------------------------, Total Months: {total_months}, Total: ${net_total}, Average Change: ${change_average:.2f}, Greatest Increase in Profits: ${greatest_increase[1]}, Greatest Decrease in Profits: ${greatest_decrease[1]}")
    