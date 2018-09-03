library("RSQLite") # Required for using SQL in R

driver <-  dbDriver("SQLite") # Initialize driver
conn2 <-  dbConnect(driver, dbname = "epl_teamWins.db") # Connect to SQL database

query = "SELECT * FROM TeamWins"

dt.teamWins <- dbGetQuery(conn2, query)

plot(dt.teamWins$Year, dt.teamWins$ChelseaWins, type = 'l', ylim = c(0, 32))

library(ggplot2)

ggplot(dt.teamWins, aes(Year)) + geom_line(aes(y = dt.teamWins$ChelseaWins, color = 'blue'), size = 1) + 
    geom_line(aes(y = dt.teamWins$ManchesterUnitedWins, colour = 'red'), size = 1) +
    geom_line(aes(y = dt.teamWins$ManchesterCityWins, color = 'skyblue2'), size = 1) +
    geom_line(aes(y = dt.teamWins$ArsenalWins, color = 'firebrick'), size = 1) +
    geom_line(aes(y = dt.teamWins$TottenhamWins, color = 'black'), size = 1) +
    geom_line(aes(y = dt.teamWins$LiverpoolWins, color = 'darkmagenta'), size = 1) +
    geom_line(aes(y = dt.teamWins$EvertonWins, color = 'springgreen4'), size = 1) +
    ylab("Match Wins") + coord_cartesian(xlim = c(2001, 2017)) +
    labs(color = "Team Legend") +
    scale_color_manual(labels = c("Tottenham Hotspurs","Chelsea F.C.","Liverpool F.C.", "Arsenal F.C.",
                                  "Manchester United", "Manchester City", "Everton"),
                       values = c("black", "blue", "darkmagenta","firebrick", "red","skyblue2", "springgreen4")) #+
    #ggtitle("Time Series of EPL Team Wins") #+ 
    #scale_color_discrete(name = "Team Legend", labels = c("Manchester United", "Chelsea FC"))

