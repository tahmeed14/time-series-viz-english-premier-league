## SI 330 Final Project
## Code File 1 of 3

## Name: Tahmeed R. Tureen
## SI 330: Data Manipulation
## University of Michigan, Ann Arbor

# Import modules
import csv

# Needed for Windows encoding, otherwise will not print appropriate symbols
import codecs
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

# Create a List of filenames for future iteration purposes
epl_files = ['epl_data0_1.csv','epl_data1_2.csv','epl_data2_3.csv','epl_data3_4.csv','epl_data4_5.csv','epl_data5_6.csv','epl_data6_7.csv',
	'epl_data7_8.csv', 'epl_data8_9.csv', 'epl_data9_10.csv', 'epl_data10_11.csv', 'epl_data11_12.csv', 'epl_data12_13.csv', 'epl_data13_14.csv',
		'epl_data14_15.csv', 'epl_data15_16.csv', 'epl_data16_17.csv']


### *********************************************************************************************************************** ###
## Data Manipulation for CHELSEA F.C. (My favorite team)

# Initialize a List that will contain tuples of Chelsea's win performance for each year starting from year 2000
chelseaHistory = []
# Initialize the league year at 2000
chelsea_leagueYear = 2001

for file in epl_files:
	with open(file, 'rU') as input_file:
		epl_data = csv.DictReader(input_file)

		chelsea_wincounter = 0

		for row in epl_data:
			if (row['HomeTeam'] == 'Chelsea' and int(row['FTHG']) > int(row['FTAG'])):
				chelsea_wincounter += 1

			if (row['AwayTeam'] == 'Chelsea' and int(row['FTHG']) < int(row['FTAG'])):
				chelsea_wincounter += 1

		chelseaYearResult = (chelsea_leagueYear, chelsea_wincounter)
		chelsea_leagueYear += 1
		chelseaHistory.append(chelseaYearResult)


#print(chelseaHistory)

with open('chelseaResults.csv', 'w', newline = "") as chelsea_output:
	#chelsea_writer = csv.DictWriter(chelsea_output, fieldnames = ["YEAR", "WINS"], extrasaction = "ignore", delimiter =",", quotechar ='"')
	chelsea_writer = csv.writer(chelsea_output)
	chelsea_writer.writerow(['Year', 'ChelseaWins'])

	for result in chelseaHistory:
		chelsea_writer.writerow(result)


### *********************************************************************************************************************** ###
## Data Manipulation for Manchester United (Historically One of the greatest teams)

# Initialize a List that will contain tuples of ManUnited's win performance for each year starting from year 2000
manU_History = []
# Initialize the league year at 2000
manU_leagueYear = 2001

for file in epl_files:
	with open(file, 'rU') as input_file:
		epl_data = csv.DictReader(input_file)

		wincounter = 0

		for row in epl_data:
			if (row['HomeTeam'] == 'Man United' and int(row['FTHG']) > int(row['FTAG'])):
				wincounter += 1

			if (row['AwayTeam'] == 'Man United' and int(row['FTHG']) < int(row['FTAG'])):
				wincounter += 1

		yearResult = (manU_leagueYear, wincounter)
		manU_leagueYear += 1
		manU_History.append(yearResult)

# Write CSV File for Manchester United
with open('manunitedResults.csv', 'w', newline = "") as output:
	team_writer = csv.writer(output)
	team_writer.writerow(['Year', 'ManchesterUnitedWins'])

	for result in manU_History:
		team_writer.writerow(result)


### *********************************************************************************************************************** ###
## Data Manipulation for Manchester City

# Initialize a List that will contain tuples of ManCity's win performance for each year starting from year 2000
manCity_History = []
# Initialize the league year at 2000
manCity_leagueYear = 2001

for file in epl_files:
	with open(file, 'rU') as input_file:
		epl_data = csv.DictReader(input_file)

		wincounter = 0

		for row in epl_data:
			if (row['HomeTeam'] == 'Man City' and int(row['FTHG']) > int(row['FTAG'])):
				wincounter += 1

			if (row['AwayTeam'] == 'Man City' and int(row['FTHG']) < int(row['FTAG'])):
				wincounter += 1

		yearResult = (manCity_leagueYear, wincounter)
		manCity_leagueYear += 1
		manCity_History.append(yearResult)

# Write CSV File for Manchester United
with open('mancityResults.csv', 'w', newline = "") as output:
	team_writer = csv.writer(output)
	team_writer.writerow(['Year', 'ManchesterCityWins'])

	for result in manCity_History:
		team_writer.writerow(result)



### *********************************************************************************************************************** ###
## Data Manipulation for Arsenal F.C.

# Initialize a List that will contain tuples of Arsenal's win performance for each year starting from year 2000
arsenal_History = []
# Initialize the league year at 2000
arsenal_leagueYear = 2001

for file in epl_files:
	with open(file, 'rU') as input_file:
		epl_data = csv.DictReader(input_file)

		wincounter = 0

		for row in epl_data:
			if (row['HomeTeam'] == 'Arsenal' and int(row['FTHG']) > int(row['FTAG'])):
				wincounter += 1

			if (row['AwayTeam'] == 'Arsenal' and int(row['FTHG']) < int(row['FTAG'])):
				wincounter += 1

		yearResult = (arsenal_leagueYear, wincounter)
		arsenal_leagueYear += 1
		arsenal_History.append(yearResult)

# Write CSV File for Arsenal
with open('arsenalResults.csv', 'w', newline = "") as output:
	team_writer = csv.writer(output)
	team_writer.writerow(['Year', 'ArsenalWins'])

	for result in arsenal_History:
		team_writer.writerow(result)


### *********************************************************************************************************************** ###
## Data Manipulation for Tottenham Hotspurs

# Initialize a List that will contain tuples of Tottenham's win performance for each year starting from year 2000
tottenham_History = []
# Initialize the league year at 2001
tottenham_leagueYear = 2001

for file in epl_files:
	with open(file, 'rU') as input_file:
		epl_data = csv.DictReader(input_file)

		wincounter = 0

		for row in epl_data:
			if (row['HomeTeam'] == 'Tottenham' and int(row['FTHG']) > int(row['FTAG'])):
				wincounter += 1

			if (row['AwayTeam'] == 'Tottenham' and int(row['FTHG']) < int(row['FTAG'])):
				wincounter += 1

		yearResult = (tottenham_leagueYear, wincounter)
		tottenham_leagueYear += 1
		tottenham_History.append(yearResult)

# Write CSV File for Tottenham
with open('tottenhamResults.csv', 'w', newline = "") as output:
	team_writer = csv.writer(output)
	team_writer.writerow(['Year', 'TottenhamWins'])

	for result in tottenham_History:
		team_writer.writerow(result)


### *********************************************************************************************************************** ###
## Data Manipulation for Liverpool F.C. (Historically one of the greatest teams)

# Initialize a List that will contain tuples of Tottenham's win performance for each year starting from year 2000
liverpool_History = []
# Initialize the league year at 2001
liverpool_leagueYear = 2001

for file in epl_files:
	with open(file, 'rU') as input_file:
		epl_data = csv.DictReader(input_file)

		wincounter = 0

		for row in epl_data:
			if (row['HomeTeam'] == 'Liverpool' and int(row['FTHG']) > int(row['FTAG'])):
				wincounter += 1

			if (row['AwayTeam'] == 'Liverpool' and int(row['FTHG']) < int(row['FTAG'])):
				wincounter += 1

		yearResult = (liverpool_leagueYear, wincounter)
		liverpool_leagueYear += 1
		liverpool_History.append(yearResult)

# Write CSV File for Tottenham
with open('liverpoolResults.csv', 'w', newline = "") as output:
	team_writer = csv.writer(output)
	team_writer.writerow(['Year', 'LiverpoolWins'])

	for result in liverpool_History:
		team_writer.writerow(result)


### *********************************************************************************************************************** ###
## Data Manipulation for Everton

# Initialize a List that will contain tuples of Tottenham's win performance for each year starting from year 2000
everton_History = []
# Initialize the league year at 2001
everton_leagueYear = 2001

for file in epl_files:
	with open(file, 'rU') as input_file:
		epl_data = csv.DictReader(input_file)

		wincounter = 0

		for row in epl_data:
			if (row['HomeTeam'] == 'Everton' and int(row['FTHG']) > int(row['FTAG'])):
				wincounter += 1

			if (row['AwayTeam'] == 'Everton' and int(row['FTHG']) < int(row['FTAG'])):
				wincounter += 1

		yearResult = (everton_leagueYear, wincounter)
		everton_leagueYear += 1
		everton_History.append(yearResult)

# Write CSV File for Tottenham
with open('evertonResults.csv', 'w', newline = "") as output:
	team_writer = csv.writer(output)
	team_writer.writerow(['Year', 'EvertonWins'])

	for result in everton_History:
		team_writer.writerow(result)


