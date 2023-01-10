# # # Pybank Coding Challenge

# Import modules
import os, csv

print(os.getcwd())
# Identify variables
months = 0
total_profit = 0
average_change = 0
greatest_increase = ["Mon-dd",0]
greatest_decrease = ["Mon-dd",0]
old_row = 0
new_row = 0
change = 0


# Import the budget data
csvpath = os.path.join("","Resources","budget_data.csv")
output_path = os.path.join("","output_csv.csv")

with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    with open(output_path,'w') as csvfile:
        csvwriter = csv.writer(csvfile,delimiter=',')
        csvwriter.writerow(csv_header)
# Determine number of months in dataset
        for row in csvreader:
            months += 1
# Determine net total amount of profit / losses over entire period
            total_profit = total_profit + int(row[1])
# Determine changes in profit / losses over entire period
            if old_row == 0:
                csvwriter.writerow([row[0],row[1],0])
                old_row = int(row[1])
            else:
                new_row = int(row[1])
                change = new_row - old_row
                csvwriter.writerow([row[0],row[1],change])
                average_change += change
                old_row = new_row
                new_row = 0
# Determine greatest increase in profits (date and amount) over the entire period
            if change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = change
# Determine greatest decrease in profits (date and amount) over the entire period
            if change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = change
# Determine average change in profit / losses
        average_change = round((average_change / (months -1)),2)
        
# Create Text File
analysis_pathway = os.path.join("","Analysis","analysis.txt")
with open(analysis_pathway, 'w') as f:
    f.write("Financial Analysis \n---------------------------- ")
    f.write(f"\nTotal months: {months}")
    f.write(f"\nTotal: ${total_profit}")
    f.write(f"\nAverage Change: ${average_change}")
    f.write(f"\nGreatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
    f.write(f"\nGreatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]}) ")
# print analysis to screen
with open(analysis_pathway,'r') as text:
    lines = text.read()
    print(lines)

