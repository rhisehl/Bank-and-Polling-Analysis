# PyPoll Python Challenge

# Import modules
import os, csv

# Identify variables
total_votes = 0
candidates = {}
candidate_percentages = {}
max_votes = 0
winner = "unknown"

# Import the budget data
csvpath = os.path.join("","Resources","election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

# Determine total number of votes cast
    for row in csvreader:
        total_votes += 1
# Determine complete list of candidates who received votes and total number of votes won
        if row[2] in candidates:
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1
# Determine percentage of votes each candidate won
    candidate_percentages = candidates.copy()
    for x in candidate_percentages:
        candidate_percentages[x] = float(round((100 * candidate_percentages[x] / total_votes),3))
# Determine winner of election based on popular vote
        if candidate_percentages[x] > max_votes:
            max_votes = candidate_percentages[x]
            winner = x
# Set up Text Output for list of candidates with votes and percentages

# Create Text File
analysis_pathway = os.path.join("","Analysis","analysis.txt")
with open(analysis_pathway, 'w') as f:
    f.write("Election results \n-------------------------")
    f.write(f"\nTotal Votes: {total_votes}")
    f.write(f"\n-------------------------")
    for x in candidate_percentages:
        f.write(f"\n{x}: {candidate_percentages[x]}% ({candidates[x]})")
    # f.write(f"\n")
    f.write(f"\n-------------------------")
    f.write(f"\nWinner: {winner}")
    f.write(f"\n-------------------------")
# Print analysis to screen
with open(analysis_pathway,'r') as text:
    lines = text.read()
    print(lines)
