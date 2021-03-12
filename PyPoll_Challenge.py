# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
# Create an empty list of cadidates
candidate_options =[]
# Create an emplty dictionary for calculating votes
candidate_votes = {}

# Create a county list and county votes dictionary
county_options = []
county_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Track the largest county and county voter turnout
largest_county = ""
largest_county_turnout = 0

candidate_in_county = {} #---------------------------------------------

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Read the header row.
    header = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes +=1

        # Retrieve the candidate name from each row
        candidate_name = row[2]

        # Extract the county name from each row.
        county = row[1]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # Write an if statement that checks that the county does not match any existing county in the county list
        if county not in county_options:
            # Add the existing county to the list of counties
            county_options.append(county)
            # Begin tracking the county's vote count
            county_votes[county] = 0

        # Add a vote to that county's vote count
        county_votes[county] +=1
#----------------------------------------------------------------------------------
        # If candidate is not listed in the county
        if (county,candidate_name) not in candidate_in_county.keys():
            # Add the candidate_name to the candidate list in the county
            candidate_in_county[(county,candidate_name)] = 0

        # Add a vote to that candidate's vote count in a county
        candidate_in_county[(county,candidate_name)] += 1
#----------------------------------------------------------------------------------

print(candidate_in_county) #----------------------------------

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
    )
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    print("County Votes:\n")
    txt_file.write("County Votes:\n")

    # Write a for loop to get the county from the county dictionary.
    for county in county_votes:

        # Retrieve the county vote count.
        cnty_vote = county_votes[county]

        # Calculate the percentage of votes for the county.
        cnty_vote_percentage = (float(cnty_vote)/float(total_votes))*100

        # Print the county results to the terminal.
        county_results = (f"{county}: {cnty_vote_percentage:.1f}% ({cnty_vote:,})\n")
        print(county_results)

        # Save the county votes to a text file.
        txt_file.write(county_results)

        # Write an if statement to determine the winning county and get its vote count.
        if cnty_vote > largest_county_turnout:
            largest_county_turnout = cnty_vote
            largest_county = county

    # Print the county with the largest turnout to the terminal.
    largest_county_results = (
        f"-------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"-------------------------\n")

    print(largest_county_results)

    # Save the county with the largest turnout to a text file.
    txt_file.write(largest_county_results)

    # Determine the percentage of votes for each candidate
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes
        vote_percentage = (float(votes)/float(total_votes))*100

        ##print out each candidate's name, vote count, and percentage
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)

        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)