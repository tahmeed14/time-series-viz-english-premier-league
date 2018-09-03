## SI 330 Final Project
## Code File 2 of 3

## Name: Tahmeed R. Tureen
## SI 330: Data Manipulation
## University of Michigan, Ann Arbor

## Purpose: Read .txt files of League Tables from Seasons 00-01 to 16-17. Then strip data from the txt on who the Champion was for
## each season using Regular Expressions

# Import Modules
import re
import csv

txt_fileList = ['2000_01.txt', '2001_02.txt', '2002_03.txt', '2003_04.txt', '2004_05.txt', '2005_06.txt', '2006_07.txt', '2007_08.txt', '2008_09.txt', '2009_10.txt', '2010_11.txt', '2011_12.txt', '2012_13.txt', '2013_14.txt', '2014_15.txt', '2015_16.txt', '2016_17.txt']
epl_champsList = []
leagueYear = 2001

for fileName in txt_fileList:
	# Read the txt files, then convert to Python string
	leagueTable_file = open(fileName, 'r')
	leagueTable_text = leagueTable_file.read()

	# Use RegEx to strip the #1 teams from each English League (Not just the English Premier League)
	desired_str = re.search(r'\b1\.(\w+) | \b1\.(\w+\s\w+)' , leagueTable_text)
	epl_champion = desired_str.group()

	if (epl_champion == "1.Chelsea "):
		epl_champion = epl_champion[2:-1] # Getting rid of the "#1."
	
	elif (epl_champion == "1.Arsenal "):
		epl_champion = epl_champion[2:-1]

	else:
		epl_champion = epl_champion[3:]

	temp_tuple = (leagueYear, epl_champion)
	epl_champsList.append(temp_tuple)
	leagueYear += 1

## Write the Python Data Structures to a CSV file output
with open('eplChampions.csv', 'w', newline = "") as champions_output:
	champions_writer = csv.writer(champions_output)
	champions_writer.writerow(['Year', 'Champions'])

	for champion in epl_champsList:
		champions_writer.writerow(champion)