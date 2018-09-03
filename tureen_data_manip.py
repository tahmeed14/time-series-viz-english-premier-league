## SI 330 Final Project
## Code File 3 of 3

## Name: Tahmeed R. Tureen
## SI 330: Data Manipulation
## University of Michigan, Ann Arbor

## Purpose: Combining all the newly created datasets from tureen_txt_manip.py and tureen_csv_manip.py to create .db or Database
## The resulting database can then be used to visualize the trend of wins for all the English Premier League Teams for each season
## from Season 2000-2001 to Season 2016-2017

# Import modules
import csv
import petl as etl
import sqlite3

# Needed for Windows encoding, otherwise will not print appropriate symbols
import codecs
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)


# Convert CSV files to etl format for further data manipulation
chelsea_data = etl.fromcsv('chelseaResults.csv', encoding = 'utf-8')
manu_data = etl.fromcsv('manunitedResults.csv', encoding = 'utf-8')
mancity_data = etl.fromcsv('mancityResults.csv',  encoding = 'utf-8')
arsenal_data = etl.fromcsv('arsenalResults.csv', encoding = 'utf-8')
tottenham_data = etl.fromcsv('tottenhamResults.csv', encoding = 'utf-8')
liverpool_data = etl.fromcsv('liverpoolResults.csv',  encoding = 'utf-8')
everton_data = etl.fromcsv('evertonResults.csv',  encoding = 'utf-8')


print(chelsea_data)

## Connect to Sqlite and Initialize a database
conn = sqlite3.connect('epl_teamWins.db')
cur = conn.cursor()


## Create Table for Chelsea F.C.
createCFC = """CREATE TABLE IF NOT EXISTS Chelsea (Year int primary key not null, ChelseaWins int)"""
cur.execute(createCFC)
# dump data from csv
chelsea_data.todb(conn, 'Chelsea')

## Create Table for Manchester United
createMUFC = """CREATE TABLE IF NOT EXISTS ManchesterUnited (Year int primary key not null, ManchesterUnitedWins int)"""
cur.execute(createMUFC)
# dump data from csv
manu_data.todb(conn, 'ManchesterUnited')

## Create Table for Manchester City
createMCity = """CREATE TABLE IF NOT EXISTS ManchesterCity (Year int primary key not null, ManchesterCityWins int)"""
cur.execute(createMCity)
# dump data from csv
mancity_data.todb(conn, 'ManchesterCity')

## Create Table for Arsenal F.C.
createARS = """CREATE TABLE IF NOT EXISTS Arsenal (Year int primary key not null, ArsenalWins int)"""
cur.execute(createARS)
# dump data from csv
arsenal_data.todb(conn, 'Arsenal')

## Create Table for Tottenham Hotspurs
createSPURS = """CREATE TABLE IF NOT EXISTS Tottenham (Year int primary key not null, TottenhamWins int)"""
cur.execute(createSPURS)
# dump data from csv
tottenham_data.todb(conn, 'Tottenham')

## Create Table for Liverpool
createLFC = """CREATE TABLE IF NOT EXISTS Liverpool (Year int primary key not null, LiverpoolWins int)"""
cur.execute(createLFC)
# dump data from csv
liverpool_data.todb(conn, 'Liverpool')

## Create Table for Everton F.C.
createEFC = """CREATE TABLE IF NOT EXISTS Everton (Year int primary key not null, EvertonWins int)"""
cur.execute(createEFC)
# dump data from csv
everton_data.todb(conn, 'Everton')

## Commit the new changes
conn.commit()



## Combine all of the databases into one single database that includes all seven Premier League Teams
## This database can then be used to easily visualize a time-series analysis of each team's win performance via RStudio's ggplot2 package

## Do this bit by bit, by creating small databases at a time

# Create Chelsea and ManU data database
createCM = """CREATE TABLE IF NOT EXISTS ChelseaManU (Year int primary key not null, ChelseaWins int, ManchesterUnitedWins int)"""
cur.execute(createCM)

## Join Chelsea and ManU data

query1 = "SELECT Chelsea.Year, Chelsea.ChelseaWins, ManchesterUnited.ManchesterUnitedWins FROM Chelsea LEFT JOIN ManchesterUnited ON (Chelsea.Year = ManchesterUnited.Year)"

read_db = etl.fromdb(conn, query1)
print(read_db)

read_db.todb(conn, 'ChelseaManU')

# for tup in read_db:
# 	cur.execute('INSERT INTO ChelseaManU(Year, ChelseaWins, ManchesterUnitedWins) VALUES (?,?,?)', (tup[0], tup[1], tup[2]))

conn.commit()

# Create Arsenal Tottenham database
createAT = """CREATE TABLE IF NOT EXISTS ArsTot (Year int primary key not null, ArsenalWins int, TottenhamWins int)"""
cur.execute(createAT)

query2 = "SELECT Arsenal.Year, Arsenal.ArsenalWins, Tottenham.TottenhamWins FROM Arsenal LEFT JOIN Tottenham ON (Arsenal.Year = Tottenham.Year)"

read_db = etl.fromdb(conn, query2)
#print(read_db)
read_db.todb(conn, 'ArsTot')

conn.commit()

# Create Liverpool Everton database
createLE = """CREATE TABLE IF NOT EXISTS LivEve (Year int primary key not null, LiverpoolWins int, EvertonWins int)"""
cur.execute(createLE)

query3 = "SELECT Liverpool.Year, Liverpool.LiverpoolWins, Everton.EvertonWins FROM Liverpool LEFT JOIN Everton ON (Liverpool.Year = Everton.Year)"

read_db = etl.fromdb(conn, query3)
#print(read_db)
read_db.todb(conn, 'LivEve')

conn.commit()

## Now Join Man City with ChelseaManU db
createCMM = """CREATE TABLE IF NOT EXISTS FirstHalf (Year int primary key not null, ChelseaWins int, ManchesterUnitedWins int, ManchesterCityWins int)"""
cur.execute(createCMM)

# Join the 3 teams
query4 = "SELECT ChelseaManU.Year, ChelseaManU.ChelseaWins, ChelseaManU.ManchesterUnitedWins, ManchesterCity.ManchesterCityWins FROM ChelseaManU LEFT JOIN ManchesterCity ON (ChelseaManU.Year = ManchesterCity.Year)"

read_db = etl.fromdb(conn, query4)
#print(read_db)
read_db.todb(conn, 'FirstHalf')

conn.commit()

## Now Combine ArsTot and LivEve databases
createATLE = """CREATE TABLE IF NOT EXISTS SecondHalf (Year int primary key not null, ArsenalWins int, TottenhamWins int, LiverpoolWins int, EvertonWins int)"""
cur.execute(createATLE)

# Join the 4 teams
query5 = "SELECT ArsTot.Year, ArsTot.ArsenalWins, ArsTot.TottenhamWins, LivEve.LiverpoolWins, LivEve.EvertonWins FROM ArsTot LEFT JOIN LivEve ON (ArsTot.Year = LivEve.Year)"

read_db = etl.fromdb(conn, query5)
#print(read_db)
read_db.todb(conn, 'SecondHalf')

conn.commit()

## NOW, combine the two halves into a database for all seven big premier league teams
createTeamWins = """CREATE TABLE IF NOT EXISTS TeamWins (Year int primary key not null, ChelseaWins int, ManchesterUnitedWins int, ManchesterCityWins int, ArsenalWins int, TottenhamWins int, LiverpoolWins int, EvertonWins int)"""
cur.execute(createTeamWins)

# Join all seven teams
query6 = "SELECT FirstHalf.Year, FirstHalf.ChelseaWins, FirstHalf.ManchesterUnitedWins, FirstHalf.ManchesterCityWins, SecondHalf.ArsenalWins, SecondHalf.TottenhamWins, SecondHalf.LiverpoolWins, SecondHalf.EvertonWins FROM FirstHalf LEFT JOIN SecondHalf ON (FirstHalf.Year = SecondHalf.Year)"

read_db = etl.fromdb(conn, query6)
#print(read_db)
read_db.todb(conn, 'TeamWins')
conn.commit()


## Now Read the Champions CSV file into a Database
champs_data = etl.fromcsv('eplChampions.csv', encoding = 'utf-8')

## Create Table for Champions for each Season
createChamps = """CREATE TABLE IF NOT EXISTS Champs (Year int primary key not null, Champions text)"""
cur.execute(createChamps)
# dump data from csv
champs_data.todb(conn, 'Champs')





# Close database connection
conn.close()