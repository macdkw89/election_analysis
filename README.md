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
This analysis using Python was a success! The process is completely automated and the script doesn't use any district specific information allowing us to use this script on a different district's tabulated votes and have equal success.

However, if we wanted to use this script on a different type of election that uses different criteria, we would have to make some modifications. 
### Example 1
Say we want to take this to the national level and use the Electoral College system. We would have to define a dictionary in python that contains each state's electoral votes.
```
state_electoral_votes = {
    "Alabama": 9,
    "Alaska": 3, 
    "Arizona": 11,
    "Arkansas": 6,
    ....
}
```

