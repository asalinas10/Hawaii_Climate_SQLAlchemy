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

The purpose of this challenge is analyze weather data using Python and SQLAlchemy. Specifically, i'll use SQLAlchemy ORM queries, Pandas, and Matplotlib. 

Use the SQLAlchemy create_engine() function to connect to your SQLite database.

Use the SQLAlchemy automap_base() function to reflect your tables into classes, and then save references to the classes named station and measurement.

Link Python to the database by creating a SQLAlchemy session.

Perform a precipitation analysis and then a station analysis.

Precipitation Analysis:

Find the most recent date in the dataset.

Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.


Load the query results into a Pandas DataFrame. Explicitly set the column names.

Sort the DataFrame values by "date".

Plot the results by using the DataFrame plot method.

Use Pandas to print the summary statistics for the precipitation data.





