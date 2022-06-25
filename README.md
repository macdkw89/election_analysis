# Election Analysis


## Overview of Election Audit
This analysis was to help Colorado Board of Elections employee, Tom, in an election audit of the tabulated results for a US Congressional precinct in Colorado. I am tasked with reporting the following:

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

 Tom's Manager wants to automate the process with Python to be used with other types of elections. 

 ## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 1.68.1

## Election-Audit Results
* There were 369,711 votes cast in the election

* County Votes:
  * Jefferson: 10.5% (38,855)
  * Denver: 82.8% (306,055)
  * Arapahoe: 6.7% (24,801)

* Largest County Turnout: Denver (306,055)

* Results by Candidate 
  * Charles Casper Stockham: 23.0% (85,213)
  * Diana DeGette: 73.8% (272,892)
  * Raymon Anthony Doane: 3.1% (11,606)

* Winner: Diana DeGette
  * Winning Vote Count: 272,892
  * Winning Percentage: 73.8%

An image of the analysis text file output:

![analysis text](/resources/results_txt.png)

An image of the analysis text file output:

![analysis terminal](/resources/results_terminal.png)

## Election-Audit Summary
This analysis using Python was a success! The process is completely automated and the script doesn't use any district specific information. This allows us to use this script on a different district's tabulated votes and have equal success, as long as the data source uses an identical format.

However, if we wanted to use this script on a different type of election that uses different criteria, we would have to make some modifications. 

### Example 1
If we were to use this code to run a primary election, we would have to include variables for the different political parties involved. Voters in Colorado are usually affiliated with a major or minor political party, or they can vote as unaffiliated. When voting unaffiliated, they can vote across party lines in the primary election, this will undoubtedly change the format of tabulated votes. We would also need variables to state Republican and Democrat winners as well as non-party-affiliated positions such as mayor and city counsel. 

### Example 2
Say we want to take this to the national level and use the Electoral College system. We would start by running the code we already have for each precinct in each state, then create a new output that contains each of the nation's 176,933 precincts' total votes (as opposed to each individual vote) in rows along with the corresponding state. We would then tally the precinct totals of candidate votes in each state using a similar format to this module with for loops and conditional statements to arrive at the popular vote winner of each state. I would then define 2 dictionaries in python that contains each state's electoral votes, and each state's winners, and award those votes to the correct candidate.
Example snippet of code:
```
candidate_list = ["Bush", "Gore"]
state_list = ['AL', 'AK', 'AZ', 'AR']
state_electoral_votes = {
    "AL": 9,
    "AK": 3, 
    "AZ": 11,
    "AR": 6,
}
state_winners = {
    'AL': 'Bush',
    'AK': 'Gore',
    'AZ': 'Gore',
    'AR': 'Bush'
}

for c in candidate_list:
    candidate_electoral_votes = 0
    for s in state_list:
        if state_winners[s] == c:
            candidate_electoral_votes += state_electoral_votes[s]
    print(f"{c}: {candidate_electoral_votes}")
```
This would return an outcome of:
```
Bush: 15
Gore: 14
```

