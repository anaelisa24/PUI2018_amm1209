# Assignment 1

1. Read in the data used for HW11
2. Plot the time series
3. Sum the data along the ride type axis to get a 600x194 matrix, containing the amount of rides per station.
4. Plot the FFT for each of the 600 time series to see the periodicity of the data. I plotted the data both in months and in weeks.

# Assignment 2

1. Download data for each zip code for a total of 21 files.
2. Download the zip code shape file for NYC and only kept the colums for zip code and geometry.
3. Merged zip code files with the shape file and only kept the columns for number of establishments. This merged took care of getting rid of the rows from other locations other than NYC.
4. Got rid of the nan rows.
5. Converted the zip code column to the index column.
6. Calculated the standardized values for the data.
7. Made sure shape, mean and std coincided with what those values had to be.
8. Performed KMeans clustering for 3, 4, and 5 clusters.
9. Performed Agglomerative clustering for 5 and 10 clusters.
10. Compared results based on the NYC Choropleth.
