## Part 1 - NY Parking Violations
Analyzing Parking Violation data to answer these questions: 

• When are tickets most likely to be issued?
• What are the most common years and types of cars to be ticketed?
• Where are tickets most commonly issued?
• Which color of the vehicle is most likely to get a ticket?


## Installation
To get this project working, you need to create a new directory to house the github in the already made "mapreduce-test" directory.
Once the new directory is created, a git clone command is required. This github page houses all the necessary mappers, reducers, and shell scripts for running all parts of the project. 

#### Link to the github: https://github.com/chriskuz/big_data_project_1

To get the data required for the MapReduce jobs, you need to traverse into big_data_project_1/src/parking. 
Once you are in this directory, run the grab_data.sh shell script. 
This shell script uses an API key to get the data directly from the source. It will then create a new directory called data, and store a file called data.csv in that directory. 
This is the data that will be used in the MapReduce jobs. 

Once you have the data and are ready to start the jobs, travel back into src/parking. 
Here you will find 4 different shell scripts, all beginning with parking and then a number 1-4 corresponding to the job. 
Running these shell scripts will output the desired results for each question. 
If you receive a permission denied error, type in the following - chmod +x "file name". 
After running this command, you should be able to run the script with no issues. 

