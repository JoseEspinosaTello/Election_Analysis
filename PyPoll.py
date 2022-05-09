#The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based onn popular vote


# Import the datetime class from the datetime module.

import csv
import datetime as dt

# Assign a variable for the file to load and the path.

file_to_load ='Resources/election_results.csv'

# Use the now() attribute on the datetime class to get the present time.

now = dt.datetime.now()

# Print the present time.

print("The time right now is ", now)

dir(csv)
#print(dir({'Arapahoe':422829,'Denver':463353,'Jefferson':432438}))
#print(dir(str))

#print(dir(int))
#print(dir(float))
#print(dir(bool))
#print(dir(list))
#print(dir(tuple))
#print(dir(dict))
#print(dir(dt))

with open(file_to_load) as election_data:

	# To do: perform analysis.
	print(election_data)