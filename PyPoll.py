# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

#import datetime as dt
#now = dt.datetime.now()
#print(now)
import csv
file_to_load = "d:/bc/repos/election_analysis/resources/election_results.csv"
file_variable = open(file_to_load,"r")

