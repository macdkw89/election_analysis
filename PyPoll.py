# Election Analysis Module for UT Data Bootcamp - Kevin MacDonald

import os
import csv
import datetime as dt

#now = dt.datetime.now()
#print(now)

#Below changes my working directory to the appropriate repository --- !!!! Fixed - but keeping code here just in case
#os.chdir('D:/BC/repos/election_analysis')

# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Assign a variable for the file to load from a path
file_to_load = os.path.join('resources','election_results.csv')
# Assign a variable to save the file to a path
file_to_save = os.path.join('analysis','election_analysis.txt')

# Open the election results and read the file
with open(file_to_load) as election_data:
    
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print each row in the CSV file
    #for row in file_reader:
        #print(row)
    
    #print the header row
    headers = next(file_reader)
    print(headers)

    

