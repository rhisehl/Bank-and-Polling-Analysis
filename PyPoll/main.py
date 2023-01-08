# PyPoll Python Challenge

# Import modules
import os, csv

# Identify variables
total_votes = 0
candidates = {}
candidate_percentages = {}
# Import the budget data
csvpath = os.path.join("","Resources","election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

# Determine total number of votes cast
    for row in csvreader:
        total_votes += 1
# Determine complete list of candidates who received votes
        if row[2] in candidates:
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1
# Determine percentage of votes each candidate won
    candidate_percentages = candidates.copy()
    for x in candidate_percentages:
        candidate_percentages[x] = float(candidate_percentages[x] / total_votes)
#Determine total number of votes each candidate won

# Determine winner of election based on popular vote

# Print results to screen
print("Election results \n -------------------------")
print(f"Total Votes: {total_votes}") # add variable for total votes
print("-------------------------")
print("") # add name: percent of votes (total votes) ie Jane: 50% (55)
## for the percentages do print(str(float(variable * 100)) + '%')
print("-------------------------")
print("Winner: ") # add winner name
print("-------------------------")
#### Consolidate print statements to one line using \n 