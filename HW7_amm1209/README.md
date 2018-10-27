# Assignment 1 census geospatial analysis

To run this notebook please create a python script called censusAPI.py with the variable myAPI containing a string with your API key.

## Using the Public Use Microdata Area (PUMA) data

1. Downloaded the data from the NYC Open Data API and opened it with GeoPandas
2. Plotted the data using the function provided by Dr. Bianco

## American Fact Finder data on percentage of houses with broadband internet access

1. Downloaded the data from AFF with API
2. Used the key 'B28002_001E' to get all households with internet and the key 'B28002_004E' to get those housholds with any type of broadband access
3. Created the file containing myAPI key
4. Downloaded both datasets and then created a new column containing the percentage of housholds with any type of broadband access
5. Downloaded the table called PERCENT OF HOUSEHOLDS WITH A BROADBAND INTERNET SUBSCRIPTION and compared the data to the one obtained through the AFF. The result shows that they are both very similar.

## Plot a choropleth of NYC broadband access

1. Merged the Broadband users table with the GeoPandasDataframe
2. Plotted a choropleth based on the percentage of people with broadband internet access per PUMA region

## Assess whether the locations of the linkNYC stations are supplying internet where it is needed

1. Download data from Dr. Bianco's repo
2. Zipped the longitude and latitude into one column
3. Created a geometry column
4. Converted the pandas dataframe into a geopandas dataframe

## Find the number of linkNYC locations per person by PUMA

1. Used the key 'B00001_001E' to get the total population by puma
2. Then flattened the data in both the pumashp and the NYClocations frames
3. Merged both data frames grouped by count 'puma'
