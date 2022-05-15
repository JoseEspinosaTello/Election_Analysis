# Election_Analysis

## Overview of Election Audit

Seth and Tom, two Colorado Board of Elections employees have contracted us to help audit the recent congressional election. They would like our company to develop a python script that will run through the election results and return the follow results.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Get a list of the total counties.
4. Calculate the total number of votes each candidate received.
5. Calculate the voter turnout per county.
6. Calculate the percentage of votes from each county.
7. Calculate the percentage of votes each candidate won.
8. Determine which county had the highest voter turnout.
9. Determine the winner of the election based on popular vote.
10. Print the results to a text file.

## Rescources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code, 1.67.1
- Results File: election_analysis

## Election-Audit Results
The analysis of the election show that:
- There was a total of 369,711 votes cast in the election.
- Votes per county:
	- Jefferson: 10.5% (38,855)
	- Denver: 82.8% (306,055)
	- Arapahoe: 6.7% (24,801)
- The county with the largest vote turnout was:
	- Denver, with a total of 306,055 votes.
- The candidates were:
	- Charles Casper Stockham
	- Diana DeGette
	- Raymon Anthony Doane
- The candidate results were:
	- Charles Casper Stockham: 23.0% (85,213)
	- Diana DeGette: 73.8% (272,892)
	- Raymon Anthony Doane: 3.1% (11,606)
- The winner of the election was:
	- Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.


![total_results](https://github.com/JoseEspinosaTello/Election_Analysis/blob/main/Resources/total_results.png?raw=true)


## Election-Audit Summary

This script will take a .csv file named “election_results” out of the designated path and use it for the election audit. If the election commission wishes to use this script for future congressional elections two changes must be made.

The two changes that must be made willtake place on lline 9 of the scrip.

![file_path](https://github.com/JoseEspinosaTello/Election_Analysis/blob/main/Resources/file_path.png?raw=true)

1. The path will need to be changed to the current path your file is currently located on your computer.
	
	If the path is not altered the script will look for the file in the current path linsted in the code. THis will result in an 	error as your current system will not have th e exant file path as listed in the code.