"""
This is codes for PyPoll
"""
# Modules
import os
import csv

# Lists to store "Voter ID" and "Candidate" values, respectively
# To stay on the safe side, use "Voter ID" to calculate total votes in case voters did not vote for any candidate
# In this case, every voter made a choice as "voter_id" and "candidate" have exactly the same length after appending values. Cool!
voter_id = []
candidate = []

# List to store unique candidate
candidate_cleaned = []

# Dictionary to store the number of votes for each candidate
Count_result = {}

# Set path for the location of original csv file
election_path = os.path.join("Resources", "election_data.csv")

# Open the csv file
with open(election_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)

    # Loop through csvreader
    for row in csvreader:
        # Append all "Voter ID" values to "voter_id" list
        voter_id.append(row[0])
        # Append all "Candidate" values to "candidate" list
        candidate.append(row[2])
    # Remove duplicate in list "candidate" and save the result to a new list called "candidate_cleaned"
    candidate_cleaned = list(set(candidate))

    # Loop through candidates that have been voted
    for name in candidate_cleaned:
        # Variable used to store the number of votes each candidate has received during iteration
        # Counter value has been reset to 0 before votes for each candidate is to be counted
        name_count = 0

        # Loop through the long list of candidate counts for each candidate
        for namepool in candidate:

            # Determine if current iterated vote is for the candidate name being checked
            if namepool == name:
                # If statement returns true, add 1 to the counter
                name_count += 1
                # Add candidate's votes to dictionary "Count_result" after looping through the long candidate count list
                Count_result[name] = name_count
    
    # Sort the dictionary "Count_result" by values in descending order and store the sorted keys (candidate's name) in a new list called "candidate_sorted_by_count"
    candidate_sort_by_count = sorted(Count_result, key=Count_result.get, reverse=True)

    # Analysis output
    print("Election Results")
    print("----------------------------")
    # The total number of votes cast is actually the length of "voter_id" list
    print(f"Total Votes: {len(voter_id)}")
    print("----------------------------")
    # Print the candidate voting results in descending order by votes
    # Note that name in "candidate_sort_by_count" can also be found as key in dictionary "Cound_result"
    for name in candidate_sort_by_count:
        print(str(name) + ': ' + "{0:.3%}".format(Count_result[name] / len(voter_id)) + " (" + str(Count_result[name]) + ")")
    print("----------------------------")
    # Print the winner of the election based on popularity
    print(f"Winner: {candidate_sort_by_count[0]}")
    print("----------------------------")

# Set path for the location of report txt file
output_path = os.path.join("Resources", "vote_analysis.txt")

# write the summary of analysis to 'vote_analysis.txt"
outfile = open(output_path, "w")
outfile.write("Election Results\n")
outfile.write("----------------------------\n")
outfile.write(f"Total Votes: {len(voter_id)}\n")
outfile.write("----------------------------\n")
for name in candidate_sort_by_count:
        outfile.write(str(name) + ': ' + "{0:.3%}".format(Count_result[name] / len(voter_id)) + " (" + str(Count_result[name]) + ")\n")
outfile.write("----------------------------\n")
outfile.write(f"Winner: {candidate_sort_by_count[0]}\n")
outfile.write("----------------------------")
outfile.close()