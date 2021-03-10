# Election_Analysis

## Overview of Election Audit
I was given a dataset of a recent local congressional election in Colorado to complete the audit of results:
- calculate the total number of votes
- get a complete list of candidates and counties
- calculate the total number of votes for each candidate and county
- calculate the percentage of votes each candidate and county
- determine the winner of the election based on popular vote and the county which had a largest number of votes
I've used Python 3.8.0 and Visual Studio Code to conduct the analysis.

## Election-Audit Results
I wrote a python script which retrieves data from [election_results.csv](https://github.com/angkohtenko/Election_Analysis/blob/main/Resources/election_results.csv) and saves the result of analysis to [election_analysis.txt](https://github.com/angkohtenko/Election_Analysis/blob/main/Analysis/election_analysis.txt) :

![](https://github.com/angkohtenko/Election_Analysis/blob/main/Analysis/election_analysis_screenshot.png)

The analysis of the election shows that:
- There were 369,711 cast votes in this congressional election.
- Votes were counted in three counties:
  * Jefferson. There are 38,885 votes or 10,5% of the total votes.
  * Denver. There are 306,055 votes or 82,8% of the total votes.
  * Arapahoe. There are 24,801 votes or 6,7% of the total votes.
- The majority of votes were in Denver - 82,8%.
- The candidates were:
  * Charles Casper Stockham
  * Diana DeGette
  * Raymon Anthony Doane
- The candidate results were:
  * Charles Casper Stockham received 23,0% of the vote and 85,213 number of votes.
  * Diana DeGette received 73,8% of the vote and 272,892 number of votes.
  * Raymon Anthony Doane received 3,1% of the vote and 11,606 number of votes.
- The winner of the election was Diana DeGette who received 73,8% of the vote and 272,892 number of votes.


## Election Audit Summary
The current script can be used to extend the analysis of election results.
For example, we can count how many votes the candidate has in the every county by creating a dictionary with multiple keys - county and candidate name - and
adding the next code in the for loop:
```
# Create a dictionary to count votes for a candidate in the county
candidate_in_county = {}
...
    # Print each row in the CSV file.
    for row in file_reader:
    ...
        # If candidate is not listed in the county
        if (county,candidate_name) not in candidate_in_county.keys():
            # Add the candidate_name to the candidate list in the county
            candidate_in_county[(county,candidate_name)] = 0

        # Add a vote to that candidate's vote count in a county
        candidate_in_county[(county,candidate_name)] += 1

# Print the county results for each candidate in the every county
print(candidate_in_county)
```
Actually, the script can be used for any election where votes for a candidate are recorded row by row. The only change that should be done in the code is choosing the appropriate column based on the source file to retrieve candidate name and county.
```
# Retrieve the candidate name from each row
candidate_name = row[2]        # change the column number in the brackets here to get candidate name

# Extract the county name from each row.
county = row[1]                # change the column number in the brackets here to get county name
````
It's important to remember that index counting begins from 0, so to get data from 3rd column we need to write [2] as an index. 

```
