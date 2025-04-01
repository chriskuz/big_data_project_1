# NBA Shot Data README

This will explain how to use the program to answer the questions of:

- for each pair of players (A,B), we define the fear score of A when facing B is the hit rate, such that B is closest defender when A is shooting. Based on the fear score, for each player, please find out who is his "most unwanted defender"
- for each player, we define the comfortable zone of shooting as a matrix of {SHOT_DIST, CLOSE_DEF_DIST, SHOT_CLOCK}. Develop a MapReduce-based algorithm to classify each player's records into 4 comfortable zones. Considering the hit rate, which zone is the best for James Harden, Chris Paul, Stephen Curry, and Lebron James. 

# Installation
This project requires the need of making a new directory in the "mapreduce-test" directory of your cluster. Once such directory is made within this hierarchy, cd into it and perform a git clone of the github: https://github.com/chriskuz/big_data_project_1

Furthermore, this project requires the need for a Kaggle API key stored within the elevated root user directory of your cluster. 

When successfully downloaded, cd into src and then into the nba directory. 

Provide elevated access to all shell scripts by running chmod +x <SHELL_FILE_NAME>

Begin by running the get_data.sh to pull the data with you eligible API key. 

Once the data is downloaded and all shell scripts are eligible to be used, run either the unwanted_defender.sh (question 1), all_comfort_zones.sh (question 2), or filtered_comfort_zones.sh (question 3) to answer any of the questions. 