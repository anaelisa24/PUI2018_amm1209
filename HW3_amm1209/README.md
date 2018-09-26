# README for HW3

## Part 1: perform instructions on deleteData.md

First, I created a test.csv file in the HW3_amm1209 folder

![test csv](https://github.com/anaelisa24/PUI2018_amm1209/blob/master/HW3_amm1209/screen%20shots/commands%20to%20remove%20csv.png)

![test csv history](https://github.com/anaelisa24/PUI2018_amm1209/blob/master/HW3_amm1209/screen%20shots/test%20csv%20history.png)

Then, I pulled it from the terminal and then ran the commands:

`git filter-branch --force --index-filter \'git rm --cached --ignore-unmatch HW3_amm1209/test.csv --prune-empty --tag-name-filter cat -- --all`

`git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch HW3_amm1209/test.csv' --prune-empty --tag-name-filter cat -- --all`

`git push origin --force --all`

The first command had an error, the second one was the correct one. After doing all this, the test.csv file was removed along with all of its history

![commands to remove csv](https://github.com/anaelisa24/PUI2018_amm1209/blob/master/HW3_amm1209/screen%20shots/commands%20to%20remove%20csv.png)

![history without csv](https://github.com/anaelisa24/PUI2018_amm1209/blob/master/HW3_amm1209/screen%20shots/history%20without%20csv.png)


## Part 2: Read CSV files with pandas and use NYC open data portal

For this part of the assignment I used the NYC infant mortality data. The steps where:

1. Make sure the environment variable PUIDATA was already installed. In my case I already had it in the bash_profile so it didn't get created again.
1. Download the data as a csv file using !curl and then move it to the PUIDATA directory.
1. Read the data and remove all but three columns. In the instructions said to remove all but tow columns but since this data was filtered by race, I kept that column to make the appropriate plots.
1. Make scatter plots for each of the races.

## Part 3: Tracking each vehicle for a bus line

In this part I created a python script that takes 2 arguments as input. The MTA API key and the bus line. The terminal command looks like this:

`python python show_bus_locations_amm1209.py API_KEY BUS_LINE`

The output from the file looks like this:

Bus line: M102
Number of buses: 13
Bus 1 is at latitude: 40.747979 and longitude: -73.97646
Bus 2 is at latitude: 40.810216 and longitude: -73.943782
Bus 3 is at latitude: 40.739001 and longitude: -73.983018
Bus 4 is at latitude: 40.798979 and longitude: -73.942487
Bus 5 is at latitude: 40.755897 and longitude: -73.972794
Bus 6 is at latitude: 40.787477 and longitude: -73.947653
Bus 7 is at latitude: 40.802689 and longitude: -73.949284
Bus 8 is at latitude: 40.801366 and longitude: -73.948153
Bus 9 is at latitude: 40.730268 and longitude: -73.989372
Bus 10 is at latitude: 40.769992 and longitude: -73.962512
Bus 11 is at latitude: 40.763685 and longitude: -73.967113
Bus 12 is at latitude: 40.810867 and longitude: -73.943142
Bus 13 is at latitude: 40.767285 and longitude: -73.964485

## Part 4: Getting the next stop information

In this last part, I created a python script that takes 3 arguments: MTA API key, the bus line and the name of the output csv file to write data in.

`python get_bus_info_amm1209.py API_KEY BUS_LINE BUS_LINE.csv`

The output is a csv file that looks like this:

![mta csv](https://github.com/anaelisa24/PUI2018_amm1209/blob/master/HW3_amm1209/screen%20shots/mta%20csv.png)
