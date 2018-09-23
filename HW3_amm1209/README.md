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
