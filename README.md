# sqlalchemy-challenge

Contents:

(dir) SurfsUp

  (dir) Resources

    hawaii.sqlite

    hawaii_measurements.csv

    hawaii_stations.csv

  app.py

  surfsup_schema.ipynb


Summary:
The "Surfs" directory contains all the files 

The "Resources" directory contains the sqlite and csv files used in the project

"app.py" contains the script that runs the app. 

"surfsup_schema.ipynb" contains the script the reflects tables into SQLAlchemy ORM

Purpose:

The purpose of this challenge is to analyze data using Python and SQLAlchemy and then vizualizing that same data through the use of a Flask API.

Part 1: Analyze and Explore the Climate Data

The purpose of Part 1 is to analyze weather data using Python and SQLAlchemy. Specifically, i'll use SQLAlchemy ORM queries, Pandas, and Matplotlib. 

Use the SQLAlchemy create_engine() function to connect to your SQLite database.

Use the SQLAlchemy automap_base() function to reflect your tables into classes, and then save references to the classes named station and measurement.

Link Python to the database by creating a SQLAlchemy session.

Perform a precipitation analysis and then a station analysis.

Precipitation Analysis:

Find the most recent date in the dataset.

Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.

Select only the "date" and "prcp" values.

Load the query results into a Pandas DataFrame. Explicitly set the column names.

Sort the DataFrame values by "date".

Plot the results by using the DataFrame plot method.

Use Pandas to print the summary statistics for the precipitation data.

Station Analysis:

Design a query to calculate the total number of stations in the dataset.

Design a query to find the most-active stations (that is, the stations that have the most rows). To do so, complete the following steps:

  List the stations and observation counts in descending order.

  Answer the following question: which station id has the greatest number of observations?

Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.

Design a query to get the previous 12 months of temperature observation (TOBS) data. To do so, complete the following steps:

  Filter by the station that has the greatest number of observations.

  Query the previous 12 months of TOBS data for that station.

  Plot the results as a histogram with bins=12, as the following image shows:

Close your session.

Part 2: Design Your Climate App

Now that i've completed my initial analysis, i designed a Flask API based on the queries that I developed. To do so, I used Flask to create routes as follows:

1. /

Start at the homepage.

List all the available routes.

2. /api/v1.0/precipitation

Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.

Return the JSON representation of your dictionary.

3. /api/v1.0/stations

Return a JSON list of stations from the dataset.

4. /api/v1.0/tobs

Query the dates and temperature observations of the most-active station for the previous year of data.

Return a JSON list of temperature observations for the previous year.

5. /api/v1.0/<start> and /api/v1.0/<start>/<end>

Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.

For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.

For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.






