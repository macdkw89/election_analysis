#Below changes my working directory to the appropriate repository
import os
import csv
import datetime as dt
now = dt.datetime.now()
print(now)
os.chdir('D:/BC/repos/election_analysis')

# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Assign a variable for the file to load, and the path
file_to_load = os.path.join('resources','election_results.csv')

# Open the election results and read the file
with open(file_to_load) as election_data:

    # To do: perform analysis
    print(election_data)

# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join('analysis','election_analysis.txt')

# Using the open() function with the "w" mode we will write data to the file
outfile = open(file_to_save, "w")

# Write some data to the file.
outfile.write('Hello world!')
outfile.close()

outfile.close






