# Assignment 1

For this assigment I used the pandas and pandasql libraries in python to manipulate dataframes and query them with SQL syntax. Steps were as follow:

1. Download the PLUTO data and moved it into the PUIDATA folder and unzipped it.
2. Read Manhattan and Brooklyn CSV files into separate variables.
3. Drop all columns except LandUse and ZipCode for both dataframes.
4. For each dataframe group by LandUse code and count the amount of rows for each group.
5. Merge both tables together.
6. Create a dictionary with the LandUse code and its corresponding string value and use it to change the values in the dataframe.
7. Calculate the ratio of Manhattan buildings/Brooklyn buildings
8. Calculate for which LandUse codes Manhattan has more buildings than Brooklyn.
