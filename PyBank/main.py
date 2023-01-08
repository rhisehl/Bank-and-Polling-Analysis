# # # Pybank Coding Challenge

# Import modules
import os, csv

print(os.getcwd())
# Identify variables
months = 0
total_profit = 0
average_change = 0
greatest_increase = []
greatest_decrease = []

# Import the budget data
#csvpath = 'C:/Users/rhise/Documents/GitHub/python-challenge/PyBank/Resources/budget_data.csv'
csvpath = os.path.join("","Resources","budget_data.csv")

with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
# Determine number of months in dataset
    for row in csvreader:
        months += 1
# Determine net total amount of profit / losses over entire period

# Determine changes in profit / losses over entire period

# Determine average change in profit / losses

# Determine greatest increase in profits (date and amount) over the entire period

# Determine greatest decrease in profits (date and amount) over the entire period

# Print analysis to screen
print("Financial Analysis /n  ----------------------------")
print(f"Total months: {months}") #insert variable for total # months
print("Total: ") #insert total profit/loss
print("Average Change: ") #insert variable of average change
print("Greatest Increase in Profits: ") #insert Mon-dd ($xxxxxx)
print("Greatest Decrease in Profits: ") #insert Mon-dd ($xxxxxx)
#### consolidate all print statements into a single line with /n statements