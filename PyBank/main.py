"""
Here are codes for PyBank
"""
# Modules
import os
import csv

# Lists to store "Date" and "Profit/Losses" values, respectively
date = []
profit_losses = []

# List to store changes of "Profit/Losses" amounts between two adjacent months
change = []

# Set path for the location of original csv file
budget_path = os.path.join("Resources", "budget_data.csv")

# Open the csv file
with open(budget_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)

    # Loop through csvreader
    for row in csvreader:

        # Append all "Date" values to "date" list
        date.append(row[0])
        # Append all "Profit/Losses" values to "profit_losses" list
        profit_losses.append(int(row[1]))

    # Loop through "profit_losses" list
    for i in range(len(profit_losses)):

        # Determine if current iterated value is the last one from "profit_losses" list and if true ...
        if i != len(profit_losses) - 1:

            # Add changes in "Profit/Losses" amount between two adjacent months to "change" list
            change.append(profit_losses[i + 1] - profit_losses[i])

    # Analysis output
    print("Financial Analysis")
    print("----------------------------")
    # The total number of months is actually the length of "date" list (or "profit_losses" list)
    print(f"Total Months: {len(date)}")
    # The net total amount of "Profit/Losses" over the entire period is the sum of values stored in "profit_losses" list
    print(f"Total: ${sum(profit_losses)}")
    # The average of the changes in "Profit/Losses" over the entire period is the sum of element values in list "change" divided by its list length
    print(f"Average Change: ${round(sum(change) / len(change), 2)}")
    # A financial record should have the same index for its values appended to "date" and "profit_losses" lists
    # Note that the index "i" in "date" and "profit_losses" is reflected as "i-1" for index in "change" list
    print(f"Greatest Increase in Profits: {date[change.index(max(change))+1]} (${max(change)})")
    print(f"Greatest Decrease in Profits: {date[change.index(min(change))+1]} (${min(change)})")

# Set path for the location of report txt file
output_path = os.path.join("Resources", "budget_analysis.txt")

# write the summary of analysis to 'budget_analysis.txt"
outfile = open(output_path, "w")
outfile.write("Financial Analysis\n")
outfile.write("----------------------------\n")
outfile.write(f"Total Months: {len(date)}\n")
outfile.write(f"Total: ${sum(profit_losses)}\n")
outfile.write(f"Average Change: ${round(sum(change) / len(change), 2)}\n")
outfile.write(f"Greatest Increase in Profits: {date[change.index(max(change))+1]} (${max(change)})\n")
outfile.write(f"Greatest Decrease in Profits: {date[change.index(min(change))+1]} (${min(change)})")
outfile.close()